#!/usr/bin/env python3
"""Gehaltsdaten aus dem Entgeltatlas der Bundesagentur fuer Arbeit.

Zwei Schritte:
  1) python3 entgeltatlas.py suche "Softwareentwickler"
       -> Berufe aus dem BERUFENET mit ihrem Berufsschluessel (KldB)
  2) python3 entgeltatlas.py entgelt 43414 --region "Rheinland-Pfalz" --region Deutschland
       -> Bruttomonatsentgelt (Vollzeit): unteres Viertel, Median, oberes Viertel

Nur Standardbibliothek, kein Login noetig. Ausgabe ist JSON.
"""
import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

EGA = "https://rest.arbeitsagentur.de/infosysbub/entgeltatlas/pc/v1"
BNET = "https://rest.arbeitsagentur.de/infosysbub/bnet/pc/v1"
NIVEAU = {"1": "Helfer", "2": "Fachkraft", "3": "Spezialist", "4": "Experte"}
ALTER = {"gesamt": 1, "u25": 2, "25-54": 3, "55+": 4}


def get(url, key):
    req = urllib.request.Request(url, headers={"X-API-Key": key, "User-Agent": "gehaltscheck/1.0"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))


def beruf_detail(bid):
    try:
        d = get(f"{BNET}/berufe/{bid}", "infosysbub-berufenet")
        d = d[0] if isinstance(d, list) else d
        kldb = (d.get("kldb2010") or "").replace("B", "").strip()
        return kldb
    except Exception:
        return ""


def cmd_suche(args):
    q = urllib.parse.quote(args.begriff)
    d = get(f"{BNET}/berufe?suchwoerter={q}", "infosysbub-berufenet")
    liste = (d.get("_embedded") or {}).get("berufSucheList") or []
    if not liste:
        print(json.dumps({"hinweis": "Kein Treffer. Offizielle deutsche Berufsbezeichnung probieren "
                                     "(z.B. 'Altenpfleger' statt 'Pflegefachkraft')."},
                         ensure_ascii=False, indent=1))
        return
    # Treffer kommen alphabetisch; die mit dem Suchwort im Namen nach vorn holen
    woerter = [w for w in args.begriff.lower().replace("-", " ").split() if w]

    def rang(b):
        name = (b.get("kurzBezeichnungNeutral") or "").lower().replace("-", " ")
        return (-sum(w in name for w in woerter), not name.startswith(woerter[0]) if woerter else 0, len(name))

    liste = sorted(liste, key=rang)[:60]
    with ThreadPoolExecutor(10) as ex:
        kldbs = list(ex.map(lambda b: beruf_detail(b["id"]), liste))
    # Nach Berufsschluessel buendeln: viele Berufe teilen sich einen, und nur der Schluessel zaehlt
    gruppen = {}
    for b, k in zip(liste, kldbs):
        if not k:
            continue
        g = gruppen.setdefault(k, {"kldb": k, "niveau": NIVEAU.get(k[-1:]), "berufe": [],
                                   "link": f"https://web.arbeitsagentur.de/entgeltatlas/beruf/{b['id']}"})
        g["berufe"].append(b.get("kurzBezeichnungNeutral"))
    out = []
    for g in list(gruppen.values())[: args.max]:
        n = len(g["berufe"])
        g["berufe"] = g["berufe"][:4] + ([f"... und {n - 4} weitere"] if n > 4 else [])
        out.append(g)
    if len(gruppen) > len(out):
        out.append({"hinweis": f"{len(gruppen) - len(out)} weitere Berufsgruppen nicht gezeigt. "
                               "Genaueren Begriff nehmen oder --max erhoehen."})
    print(json.dumps(out, ensure_ascii=False, indent=1))


def wert(v, bbg):
    """Negative Werte = keine Daten (zu wenige Faelle). Werte an der Bemessungsgrenze sind gedeckelt."""
    if v == -2 and bbg:  # -2 = liegt ueber der Beitragsbemessungsgrenze
        return f">{bbg}"
    if v is None or v < 0:
        return None
    if bbg and v >= bbg:
        return f">{bbg}"
    return v


def cmd_entgelt(args):
    regionen = get(f"{EGA}/regionen", "infosysbub-ega")
    wunsch = args.region or ["Deutschland"]
    treffer, unbekannt = [], []
    for w in wunsch:
        m = [r for r in regionen if r["bezeichnung"].lower() == w.lower()]
        m = m or [r for r in regionen if w.lower() in r["bezeichnung"].lower()]
        (treffer.append(m[0]) if m else unbekannt.append(w))
    ergebnis = {"kldb": args.kldb, "niveau": NIVEAU.get(args.kldb[-1:]),
                "einheit": "Bruttomonatsentgelt in Euro, Vollzeit, inkl. Sonderzahlungen",
                "hinweis": "Der Schluessel deckt die ganze Berufsgruppe ab, nicht nur den einen Beruf. "
                           "Alle Altersgruppen sind enthalten, auch Beschaeftigte mit 25 Jahren im Betrieb.",
                "regionen": []}
    if unbekannt:
        ergebnis["unbekannte_regionen"] = unbekannt
        ergebnis["verfuegbare_regionen"] = [r["bezeichnung"] for r in regionen]
    for r in treffer:
        try:
            rows = get(f"{EGA}/entgelte/{args.kldb}?r={r['id']}", "infosysbub-ega")
        except urllib.error.HTTPError as e:
            ergebnis["regionen"].append({"region": r["bezeichnung"], "fehler": f"HTTP {e.code}"})
            continue
        bbg = r.get("beitragsBemessungsGrenze")
        eintrag = {"region": r["bezeichnung"], "gesamt": None, "nach_alter": {}, "nach_branche": {}}
        for x in rows:
            if x["gender"]["id"] != 1:
                continue
            z = {"q25": wert(x["entgeltQ25"], bbg), "median": wert(x["entgelt"], bbg),
                 "q75": wert(x["entgeltQ75"], bbg),
                 "beschaeftigte": x["besetzung"] if x["besetzung"] >= 0 else None}
            if z["median"] is None:
                continue
            a, b = x["ageCategory"], x["branche"]
            if a["id"] == 1 and b["id"] == 1:
                eintrag["gesamt"] = z
            elif b["id"] == 1:
                eintrag["nach_alter"][a["bezeichnung"]] = z
            elif a["id"] == 1:
                eintrag["nach_branche"][b["bezeichnung"]] = z
        if not eintrag["gesamt"]:
            eintrag["hinweis"] = "Keine Daten (zu wenige Beschaeftigte). Bundesland oder Deutschland nehmen."
        ergebnis["regionen"].append(eintrag)
    print(json.dumps(ergebnis, ensure_ascii=False, indent=1))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("suche", help="Beruf suchen und Berufsschluessel finden")
    s.add_argument("begriff")
    s.add_argument("--max", type=int, default=12)
    s.set_defaults(f=cmd_suche)
    e = sub.add_parser("entgelt", help="Entgelte zu einem Berufsschluessel")
    e.add_argument("kldb", help="5-stelliger Schluessel, letzte Ziffer = Niveau (2 Fachkraft, 3 Spezialist, 4 Experte)")
    e.add_argument("--region", action="append",
                   help="Bundesland, Grossstadt oder Deutschland; mehrfach moeglich")
    e.set_defaults(f=cmd_entgelt)
    a = p.parse_args()
    try:
        a.f(a)
    except (urllib.error.URLError, TimeoutError) as err:
        print(json.dumps({"fehler": f"Entgeltatlas nicht erreichbar: {err}",
                          "naechster_schritt": "Ohne Skript weitermachen, nur Websuche nutzen."},
                         ensure_ascii=False))
        sys.exit(2)


if __name__ == "__main__":
    main()
