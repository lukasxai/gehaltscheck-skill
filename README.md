# Gehaltscheck-Skill für Claude

Ein Skill, mit dem Claude einschätzt, was dein Job am Markt wert ist. Du nennst Job, Ort und Berufserfahrung, Claude sucht die Zahlen zusammen und gibt dir einen Orientierungswert mit Spanne, den Abstand zu deinem aktuellen Gehalt und zwei, drei Sätze für das Gespräch mit deinem Chef.

Die Idee dahinter: Wer nur sagt „ich will mehr Geld“, bekommt die Frage „wofür?“. Wer einen Vergleich mitbringt, hat ein Argument. Normalerweise holt man sich dafür ein Gegenangebot von einer anderen Firma. Der Skill ersetzt das durch öffentliche Daten.

Aus dem Video von [@lukasxai](https://www.instagram.com/lukasxai/).

## Bitte beachten

Das Ergebnis ist eine Einschätzung aus öffentlich zugänglichen Durchschnittsdaten. Es ist keine Garantie und keine Beratung. Dein tatsächlicher Marktwert kann deutlich abweichen, je nach Firma, Aufgabe, Qualifikation und Verhandlung. Alle Zahlen sind ohne Gewähr. Prüf die Quellen, die Claude dir verlinkt, bevor du dich darauf berufst.

## Wo der Skill läuft

Am besten in **Claude Code** oder in der **Claude Desktop-App** (Cowork oder Code). Dort holt der Skill die amtlichen Zahlen direkt bei der Bundesagentur für Arbeit.

Im normalen Chat im Browser oder am Handy kommt Claude an diese Zahlen nicht heran. Der Skill läuft dann trotzdem, stützt sich aber nur auf Gehaltsportale und sagt dir, dass das Ergebnis gröber ist. Die Websuche muss dafür eingeschaltet sein.

## Installieren

1. Lade [gehaltscheck-skill.zip](../../releases/latest/download/gehaltscheck-skill.zip) herunter. Im Browser von Instagram oder TikTok startet der Download nicht, öffne die Seite dafür in Safari oder Chrome.
2. Öffne in Claude die Einstellungen, geh zu den Skills und lade die ZIP-Datei dort hoch.
3. Schreib in einem Gespräch zum Beispiel: „Gehaltscheck: Industriekaufmann in Mainz, 6 Jahre Erfahrung, aktuell 44.000 brutto im Jahr.“

In Claude Code legst du stattdessen den Ordner `gehaltscheck` nach `~/.claude/skills/`.

## Woher die Zahlen kommen

- **Entgeltatlas der Bundesagentur für Arbeit:** gemeldete Löhne aller Vollzeitbeschäftigten, nach Bundesland und für elf Großstädte. Das ist die wichtigste Quelle.
- **Gehaltsportale** wie Stepstone oder gehalt.de, für die Einordnung nach Berufserfahrung.
- **Aktuelle Stellenanzeigen**, wenn eine Firma darin selbst ein Gehalt nennt. Das ist in Deutschland selten.

## Grenzen

- Nur Deutschland und nur Angestellte.
- Der Entgeltatlas kennt keine Berufserfahrung und keine Firmengröße. Die Einordnung nach Erfahrung ist deshalb eine Faustregel.
- Bei sehr hohen Gehältern ist die amtliche Statistik nach oben abgeschnitten.
- Bei tarifgebundenen Stellen zählt die Tariftabelle mehr als jeder Durchschnitt.

## Was drin ist

- [`gehaltscheck/SKILL.md`](gehaltscheck/SKILL.md): die Anleitung für Claude.
- [`gehaltscheck/scripts/entgeltatlas.py`](gehaltscheck/scripts/entgeltatlas.py): holt die Zahlen aus dem Entgeltatlas. Braucht nur Python, keinen Login.
