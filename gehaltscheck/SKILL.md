---
name: gehaltscheck
description: Ermittelt aus Job, Ort und Berufserfahrung den realistischen Marktwert eines Gehalts in Deutschland und liefert ihn als "Gegenangebot" für die Gehaltsverhandlung (Spanne, Vergleich mit dem aktuellen Gehalt, Sätze fürs Gespräch, Quellen). Zieht echte Daten aus dem Entgeltatlas der Bundesagentur für Arbeit, aus Gehaltsportalen und aus aktuellen Stellenanzeigen. Immer nutzen, wenn jemand wissen will, was er verdienen sollte oder kann, ob er unterbezahlt ist, was in seinem Beruf üblich ist, wie viel er bei der Gehaltsverhandlung oder im Bewerbungsgespräch fordern soll, oder wenn Begriffe wie Gehaltscheck, Marktwert, Durchschnittsgehalt, Gehaltsvergleich, Gegenangebot oder "Sixt-Methode" fallen. Auch dann, wenn nur Job und Stadt genannt werden.
---

# Gehaltscheck

## Worum es geht

Wer zum Chef geht und sagt "ich will mehr Geld", bekommt die Frage "wofür?". Wer sagt "der Markt zahlt für meine Stelle X", hat einen Vergleich auf dem Tisch, und über einen Vergleich lässt sich schlechter hinwegreden als über einen Wunsch. Normalerweise holt man sich dafür ein echtes Gegenangebot von einer anderen Firma. Dieser Skill ersetzt das: Er baut aus öffentlichen Daten eine belastbare Marktzahl für genau diese Person.

Das Ergebnis muss zwei Dinge aushalten: Der Nutzer muss es in zwei Minuten verstehen, und sein Chef darf es nicht mit einer Rückfrage zerlegen können. Deshalb zählt jede Zahl nur mit Quelle, und geschätzte Zahlen werden als Schätzung benannt.

## Der Ton: eine Einschätzung, kein Urteil

Was hier herauskommt, ist eine Orientierung aus öffentlichen Durchschnittsdaten. Sie kennt die Firma nicht, die genaue Aufgabe nicht und nicht die Leistung der Person. Das echte Gehalt kann deshalb spürbar darüber oder darunter liegen, ohne dass jemand etwas falsch macht. Wer das Ergebnis liest, soll das merken, sonst geht er mit einer Scheinsicherheit ins Gespräch und ist enttäuscht oder verärgert, wenn es anders kommt.

Daraus folgt für jede Ausgabe:

- Von "Orientierungswert" und "Einschätzung" sprechen, nicht von dem, was jemandem "zusteht" oder was er "bekommen wird". Keine Zusagen, keine Garantien.
- Befunde vorsichtig formulieren: "liegt nach diesen Daten unter dem Schnitt" statt "du bist unterbezahlt", "spricht dafür" statt "ist so".
- Immer die Spanne nennen, nie nur die eine Zahl.
- Der Hinweis am Ende der Vorlage ("Bitte beachten") gehört in jedes Ergebnis, wörtlich und ungekürzt, auch bei Nachfragen mit neuen Zahlen.
- Keine Ratschläge zu Kündigung, Klage oder ähnlich weitreichenden Schritten. Bei Rechtsfragen (Mindestlohn, Tarif, Eingruppierung) auf Betriebsrat, Gewerkschaft oder eine Beratungsstelle verweisen.

## Wo der Skill läuft

Vollständig arbeitet der Skill dort, wo Claude Befehle ausführen und frei ins Internet darf: in Claude Code und in der Desktop-App (Cowork, Code). Dort holt das Skript die Zahlen direkt bei der Arbeitsagentur.

Im normalen Chat (Web oder Handy) ist das Skript oft nicht nutzbar, weil die Umgebung dort keine Verbindung zur Arbeitsagentur aufbauen darf, und ohne aktivierte Websuche geht gar keine Recherche. Deshalb:

- Schlägt das Skript fehl oder gibt es kein Terminal: nicht mehrfach probieren, sondern mit Portalen und Websuche weitermachen und nach dem Abschnitt "Ohne Entgeltatlas" rechnen.
- Im Ergebnis dann offen sagen, dass die amtlichen Zahlen nicht abgerufen werden konnten, das Ergebnis deshalb deutlich gröber ist, und dass der Skill in Claude Code oder der Desktop-App genauer arbeitet.
- Gibt es weder Skript noch Websuche: keine Zahlen aus dem Gedächtnis als Ergebnis ausgeben. Dem Nutzer sagen, dass ohne Internetzugriff keine belastbare Einschätzung möglich ist, und ihn bitten, die Websuche einzuschalten oder den Skill in Claude Code oder der Desktop-App zu starten.

## 1. Eingaben klären

Gebraucht werden drei Angaben:

- **Job** (Berufsbezeichnung, gern mit Schwerpunkt)
- **Ort** (Stadt oder Region in Deutschland)
- **Erfahrung** (Jahre im Beruf)

Fehlt eine davon, einmal kurz nachfragen. In derselben Nachricht nach dem **aktuellen Bruttojahresgehalt** fragen, als freiwillige Angabe: Ohne sie gibt es nur die Marktzahl, mit ihr den Abgleich, und der ist der eigentliche Wert. Dabei gleich mitfragen, ob Weihnachts- und Urlaubsgeld in der Zahl stecken und ob es Vollzeit ist, weil der Vergleich sonst schief wird. Branche, Firmengröße und Personalverantwortung helfen, sind aber kein Grund für eine zweite Fragerunde. Wenn sie fehlen, mit dem Durchschnitt rechnen und das im Ergebnis sagen.

Stehen Job, Ort und Erfahrung schon in der Nachricht, nicht nachfragen, sondern loslegen. Ist beim genannten Gehalt offen, ob Sonderzahlungen drin sind, mit "inklusive, Vollzeit" rechnen und diese Annahme im Ergebnis nennen.

## 2. Daten holen

Drei Quellen, weil jede eine andere Schwäche hat. Erst zusammen ergeben sie eine Zahl, auf die man sich stützen kann.

### a) Entgeltatlas der Bundesagentur für Arbeit (der Anker)

Das sind gemeldete Löhne aller sozialversicherungspflichtig Vollzeitbeschäftigten, keine Umfrage. Kein Chef kann die Quelle als "irgendein Internetportal" abtun. Deshalb zuerst.

Das Skript liegt im Ordner dieses Skills unter `scripts/`. Mit dem vollen Pfad aufrufen oder vorher in den Skill-Ordner wechseln.

```bash
python3 scripts/entgeltatlas.py suche "Softwareentwickler"
python3 scripts/entgeltatlas.py entgelt 43414 --region "Rheinland-Pfalz" --region Deutschland
```

Schritt eins liefert die Berufsgruppen (Berufsschlüssel, KldB), in denen passende Berufe liegen, jeweils mit Beispielberufen. Die Gruppe wählen, deren Berufe inhaltlich am besten passen. Die letzte Ziffer des Schlüssels ist das Anforderungsniveau: 2 Fachkraft (Ausbildung), 3 Spezialist (Meister, Techniker, Bachelor), 4 Experte (Studium, Master). Sie lässt sich austauschen, wenn die Person klar auf einem anderen Niveau arbeitet als der gefundene Beruf (43412 → 43414).

Die Berufssuche ist wörtlich und kennt Alltagsbegriffe oft nicht ("Pflegefachkraft" findet nur Fachweiterbildungen). Passt kein Treffer, zwei, drei andere Wörter probieren: die offizielle Ausbildungsbezeichnung ("Altenpfleger", "Pflegefachmann"), die deutsche statt der englischen Bezeichnung, ein genauerer Begriff statt eines Oberbegriffs ("Onlinemarketing" statt "Marketing"). Stimmt bei einem Treffer der Beruf, aber nicht das Niveau, die letzte Ziffer tauschen. Passt auch dann nichts, die nächstliegende Berufsgruppe nehmen und im Ergebnis offen sagen, dass es eine Näherung ist.

Regionen: Es gibt Deutschland, alle Bundesländer (also auch Berlin, Hamburg, Bremen) und elf Großstädte (München, Köln, Frankfurt am Main, Stuttgart, Düsseldorf, Dortmund, Essen, Leipzig, Dresden, Hannover, Nürnberg). Für andere Orte das Bundesland nehmen. Deutschland immer mit abfragen, als Vergleich und als Ersatz, falls die Region zu wenige Fälle hat.

Was man über die Zahlen wissen muss:

- Es sind **Monatswerte brutto in Vollzeit, Sonderzahlungen schon eingerechnet**. Jahresgehalt also mal 12, nicht mal 13.
- `q25`, `median`, `q75`: Ein Viertel verdient weniger als q25, die Hälfte weniger als der Median, ein Viertel mehr als q75.
- Ein Wert wie `>8050` heißt: gedeckelt an der Beitragsbemessungsgrenze, der wahre Wert liegt darüber. Bei gut bezahlten Berufen ist der Entgeltatlas nach oben blind, dann zählen die anderen Quellen mehr.
- Erfahrung kennt der Entgeltatlas nicht, nur Altersgruppen und grobe Branchen. Beides mitnehmen, wenn es zur Person passt.
- Der Schlüssel steht für eine ganze Berufsgruppe, und im Median stecken alle Altersgruppen, auch Leute mit 25 Jahren im Betrieb. Im Ergebnis deshalb "Berufsgruppe" schreiben und den Median nicht mit "das verdient man nach fünf Jahren" gleichsetzen.
- Die Suche liefert zu jedem Beruf einen Link auf die Entgeltatlas-Seite. Der kommt als Quelle ins Ergebnis. Die Seite zeigt zuerst die Werte für Deutschland, die Region wählt man dort selbst. Das dazuschreiben, damit der Nutzer die Zahl wiederfindet.

Lässt sich das Skript nicht ausführen (kein Terminal, keine Verbindung), gibt es die Entgeltatlas-Zahlen nicht: Die Seite `web.arbeitsagentur.de/entgeltatlas` lässt sich per Seitenabruf nicht lesen und taucht in der Websuche nicht mit Werten auf. Nicht weiter danach suchen. Dann gilt der Abschnitt "Ohne Entgeltatlas" weiter unten.

### b) Gehaltsportale (für die Erfahrung)

Per Websuche zwei bis drei unabhängige Portale abfragen, etwa Stepstone, kununu, gehalt.de, Glassdoor, Indeed. Suchmuster: `Gehalt <Job> <Ort>` und `Gehalt <Job> <n> Jahre Berufserfahrung`. Gesucht sind Werte nach Erfahrungsstufe und für die Stadt.

Diese Zahlen sind Selbstauskünfte oder Hochrechnungen, also weicher als der Entgeltatlas. Sie zeigen dafür, was der Entgeltatlas nicht zeigt: wie stark das Gehalt mit den Jahren steigt. Immer festhalten, ob eine Zahl Jahres- oder Monatsgehalt ist und ob Boni drin sind.

### c) Aktuelle Stellenanzeigen (das eigentliche Gegenangebot)

Per Websuche nach offenen Stellen für diesen Job in dieser Region suchen, die ein Gehalt nennen (`<Job> <Ort> Stellenangebot Gehalt`, dazu Stepstone, Indeed, die Jobsuche der Arbeitsagentur, Karriereseiten). Zwei bis vier konkrete Anzeigen mit Firma, Spanne und Link sind das Stärkste im ganzen Ergebnis: "Firma Y sucht gerade jemanden wie mich und zahlt bis Z."

Unterscheiden, ob die Firma die Spanne selbst nennt oder ob das Portal sie schätzt. Nur die erste Sorte ist ein Argument im Gespräch. In Deutschland nennen die wenigsten Firmen ein Gehalt, bei vielen Berufen findet sich also keine solche Anzeige. Eine Anzeige zählt nur, wenn sie sich öffnen lässt und das Gehalt dort wirklich steht. Was nur im Suchtreffer auftaucht, ist ungeprüft und wird so gekennzeichnet, abgelaufene Anzeigen fallen weg. Findet sich nichts, nach zwei, drei Suchen aufhören, das so sagen, höchstens zwei Portal-Schätzungen als grobe Orientierung zeigen (klar als Schätzung markiert) und keine Anzeige erfinden. Die Sätze für den Chef stützen sich dann allein auf den Entgeltatlas.

### d) Tarif, wenn die Branche danach riecht

Bei Metall und Elektro, Chemie, Banken, öffentlichem Dienst und Pflege kurz die passende Tariftabelle suchen, auch wenn der Nutzer keine Tarifbindung erwähnt. Ist der Arbeitgeber tarifgebunden, ist die Tabelle die Antwort (siehe Grenzen). Ist er es nicht oder ist es unklar, kommt sie als Vergleichszeile in die Tabelle, mit dem Hinweis, dass die Entgeltgruppe eine Annahme ist.

## 3. Rechnen

Die Regeln hier sind bewusst fest, damit zwei Durchläufe für dieselbe Person bei derselben Zahl landen. Ein Ergebnis, das je nach Tagesform 75.000 oder 87.000 heißt, ist als Argument wertlos.

1. Alles auf **Bruttojahresgehalt in Vollzeit** bringen. Bei Teilzeit mit der Vollzeit-Stundenzahl des Betriebs hochrechnen, ist sie unbekannt, mit 40 Stunden, und die Annahme nennen.
2. Die Basis wählen: Entgeltatlas-Werte der Region. Gibt es Werte für die passende Branche, diese nehmen (Agenturen, Beratungen, Personaldienstleister: "Erbringung wirtschaftl. Dienstleistungen"; Softwarefirmen und Medien: "Information und Kommunikation"; Industrie: "produzierendes Gewerbe ohne Bau"). Ist die Branche unklar, die Gesamtwerte nehmen.
3. Aus q25, Median und q75 fünf Stufen bilden:

   | Stufe | Wert |
   |---|---|
   | A | q25 |
   | B | Mitte zwischen q25 und Median |
   | C | Median |
   | D | Mitte zwischen Median und q75 |
   | E | q75 |

   Die Erfahrung bestimmt die Stufe. Weil im Median alle Altersgruppen stecken, liegt jemand mit wenigen Jahren darunter:
   - bis 2 Jahre: A
   - 3 bis 5 Jahre: B
   - 6 bis 10 Jahre: C
   - über 10 Jahre oder mit Personalverantwortung: D

   Firmengröße und Spezialisierung verschieben die Stufe nicht. Sie stehen als Hinweis im Ergebnis (Konzerne zahlen meist mehr, kleine Betriebe weniger).
4. Mit den Portalen abgleichen. Dafür zählen nur Portalwerte, die zur Erfahrung passen: eine ausgewiesene Erfahrungsstufe oder ein Titel mit passender Seniorität. Werte ohne Erfahrungsbezug stehen in der Tabelle, gehen aber nicht in die Rechnung ein. Dasselbe gilt für einen Portalwert, der bei drei oder mehr Jahren Erfahrung unter q25 liegt: Er widerspricht den gemeldeten Löhnen. Gibt es mehrere passende Werte, ihren Durchschnitt nehmen. Weicht der höchstens 15 % von der Stufe ab, bleibt der Zielwert die Stufe. Weicht er stärker ab, ist der Zielwert die Mitte zwischen beiden, und im Ergebnis steht ein Satz, warum die Quellen auseinanderliegen (Portale: eher Jüngere, oft ohne Sonderzahlungen).
5. Die drei Zahlen:
   - **Zielwert:** das Ergebnis aus Schritt 4
   - **untere Grenze:** eine Stufe unter der Stufe der Person. Bei Stufe A der Median der unter 25-Jährigen, fehlt er, 10 % unter q25.
   - **obere Grenze:** eine Stufe darüber.
   
   Ist q75 gedeckelt (">8050"), lässt sich D und E nicht berechnen. Dann als obere Grenze "über [Deckel mal 12] €" schreiben und dazusagen, dass die Statistik nach oben abgeschnitten ist.
6. Ist das aktuelle Gehalt bekannt: Abstand zum Zielwert in Euro pro Jahr und pro Monat, dazu die nötige Erhöhung in Prozent (Abstand geteilt durch das aktuelle Gehalt). Hat der Nutzer ein Monatsgehalt oder Teilzeit genannt, alle Zahlen zusätzlich in seiner Einheit angeben (im Monat, auf seine Stunden gerechnet), denn so steht es auf seiner Abrechnung.
7. **Forderung** für das Gespräch: Zielwert plus rund 5 %, gerundet. Das lässt Platz zum Verhandeln, ohne unseriös zu wirken.
8. Mindestlohn prüfen, wenn das aktuelle Gehalt niedrig ist: Stundenlohn ausrechnen (Monatsgehalt geteilt durch Wochenstunden mal 4,35). Liegt er in der Nähe des gesetzlichen Mindestlohns oder eines Branchenmindestlohns (Pflege, Gebäudereinigung, Bau und andere), den aktuellen Wert per Websuche holen. Liegt die Person darunter, kommt das im Ergebnis ganz nach oben: Das ist ein Anspruch und kein Verhandlungsthema. Keine rechtliche Bewertung abgeben, sondern auf Vertrag, Abrechnung und Gewerkschaft oder Beratungsstelle verweisen.

### Ohne Entgeltatlas

Fehlt der Anker, sind die Stufen oben nicht berechenbar. Dann gilt:

- Zielwert: Durchschnitt der Portalwerte, die zur Erfahrung passen. Gibt es sie nur bundesweit und nennt dasselbe Portal einen Wert für das Bundesland oder die Stadt, im selben Verhältnis anpassen. Keine eigenen Zuschläge schätzen.
- Spanne: vom niedrigsten bis zum höchsten verwendeten Wert.
- Das Ergebnis beginnt mit einem Satz, dass die amtlichen Zahlen hier nicht abrufbar waren und die Einschätzung deshalb deutlich gröber ist, und dass der Skill in Claude Code oder der Desktop-App genauer arbeitet. Hinter dem Orientierungswert steht "(grobe Schätzung)".
- Dem Nutzer anbieten, es genauer zu machen: Er öffnet https://web.arbeitsagentur.de/entgeltatlas/, sucht seinen Beruf, wählt seine Region und schreibt die drei Werte (unteres Viertel, Median, oberes Viertel) in den Chat. Damit dann normal nach den Stufen rechnen.
- In den Sätzen für den Chef keine Entgeltatlas-Zahl nennen, die nicht vorliegt. Stattdessen dazuschreiben, dass er den Median dort selbst nachschlagen und einsetzen sollte, weil eine Zahl der Arbeitsagentur im Gespräch mehr trägt als ein Portalwert.

Runde Zahlen nennen (auf 500 oder 1.000 Euro), aber nachvollziehbar herleiten. Scheingenauigkeit wie "57.384 €" wirkt ausgerechnet, ist es aber nicht.

Ehrlich bleiben, wenn das Ergebnis unbequem ist. Liegt die Person schon über dem Markt, steht das genau so da. Dann taugt der Marktvergleich nicht als Argument, und der Hebel ist ein anderer: mehr Verantwortung, eine andere Rolle, messbare Ergebnisse. Ein geschöntes Ergebnis würde im Gespräch mit dem Chef auffliegen, und zwar auf Kosten des Nutzers.

## 4. Ergebnis ausgeben

Direkt im Chat, in dieser Reihenfolge. Kurz halten, der Nutzer will eine Zahl und keinen Bericht.

```
## Dein Gegenangebot

**[Job], [Ort], [n] Jahre Erfahrung**

Orientierungswert: **rund [Zielwert] € brutto im Jahr**
Übliche Spanne: [untere Grenze] € bis [obere Grenze] €

[Wenn aktuelles Gehalt bekannt:]
Du bekommst aktuell [x] €. Das sind rund [y] € im Jahr ([z] € im Monat) [unter/über] dem Orientierungswert. Um aufzuschließen, wären etwa [p] % mehr nötig.

[Wenn nicht bekannt, stattdessen:]
Liegst du unter [untere Grenze] €, spricht viel dafür, dass du unter dem Üblichen liegst. Liegst du über [obere Grenze] €, taugt der Marktvergleich eher nicht als Argument.

### Woher die Zahl kommt
| Quelle | Wert | Was sie misst |
|---|---|---|
| Entgeltatlas (Bundesagentur für Arbeit), [Region] | ... | gemeldete Löhne, Vollzeit |
| [Portal] | ... | ... |
| [Portal] | ... | ... |

[Ein bis zwei Sätze: warum der Zielwert in der Spanne dort liegt, wo er liegt.]

### Wer gerade sucht
- [Firma], [Stelle], [Spanne], [Link]
- ...

### So sagst du es deinem Chef
[Zwei bis drei fertige Sätze zum Vorlesen, die den Vergleich nennen statt eines Wunschs,
mit Quelle und Zahl, am Ende die Forderung aus Schritt 7. Ohne Anzeigen stützen sich die Sätze nur
auf den Entgeltatlas. Ist das aktuelle Gehalt unbekannt, bleibt dafür eine Lücke: "[dein Gehalt]".]

### Was die Zahl nicht kann
[Ein bis zwei Sätze: Näherungen, fehlende Angaben, gedeckelte Werte. Nur was hier wirklich zutrifft.]

### Bitte beachten
Das ist eine Einschätzung aus öffentlich zugänglichen Durchschnittsdaten, keine Garantie und keine Beratung. Dein tatsächlicher Marktwert kann deutlich abweichen, je nach Firma, Aufgabe, Qualifikation und Verhandlung. Die Zahlen sind ohne Gewähr. Prüf die verlinkten Quellen selbst, bevor du dich im Gespräch darauf berufst.
```

Die Quellen als Links angeben. Die Sätze fürs Gespräch in der Du-Form und so, wie jemand wirklich redet: sachlich und klar, aber als Einstieg in ein Gespräch und nicht als Ultimatum. Der Vergleich trägt das Argument, Druck braucht es nicht. Dazusagen, dass es ein Vorschlag ist, den der Nutzer an seine Lage anpassen soll. Beispiel für den Ton:

> "Ich habe mir angeschaut, was der Markt für meine Stelle zahlt. Laut Entgeltatlas der Arbeitsagentur liegt der Median für Softwareentwickler in Rheinland-Pfalz bei rund 65.500 Euro, und zwei Firmen in Mainz suchen gerade für bis zu 75.000. Ich liege bei 58.000. Ich würde gern darüber sprechen, wie wir in Richtung 70.000 kommen."

## Grenzen

- Nur Deutschland. Für Österreich und die Schweiz gibt es den Entgeltatlas nicht, dort nur Portale und Stellenanzeigen nutzen und das sagen.
- Teilzeit: auf Vollzeit hochrechnen, vergleichen, zurückrechnen.
- Tarifgebundene Stellen (öffentlicher Dienst, Pflege nach TVöD, Metall): Die Tariftabelle schlägt jeden Durchschnitt. Entgeltgruppe und Stufe heraussuchen. Der Hebel ist dort die Eingruppierung, kaum der Betrag.
- Selbstständige und Freiberufler: Der Entgeltatlas kennt nur Angestellte. Tagessätze sind ein anderes Thema.
- Keine Steuer- oder Rechtsberatung, keine Nettoberechnung als Hauptergebnis. Brutto ist die Währung der Verhandlung.
