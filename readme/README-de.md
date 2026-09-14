# Liplog

Einfaches Python-Logging-Paket zum Erstellen einer Logdatei im Projektordner und gleichzeitig zur Ausgabe in der Konsole.

## Sprache

- [README English](README.md)

## Funktionen

- Automatische Erstellung eines Log-Ordners
- Logdatei mit Zeitstempel
- Ausgabe in der Konsole in Echtzeit
- Einfache API für schnelle Nutzung

## Installation

Installieren über PyPI:

```bash
python -m pip install liplog
```

Direkt von GitHub installieren:

```bash
git clone https://github.com/R0g3rT/liplog.git
cd liplog
python -m pip install .
```

Aktualisieren:

```bash
python -m pip install --upgrade liplog
```

Deinstallieren:

```bash
python -m pip uninstall liplog
```

## Verwendung

```python
from liplog import write_log

write_log("API client gestartet", "INFO")
write_log("Wichtige Warnung", "WARNING")
write_log("Ein Fehler ist aufgetreten", "ERROR")
```

Beispielausgabe:

```text
[2026-09-14 12:00:00] [INFO] API client gestartet
[2026-09-14 12:00:01] [WARNING] Wichtige Warnung
[2026-09-14 12:00:02] [ERROR] Ein Fehler ist aufgetreten
```

## Unterstützte Log-Level

- `INFO`
- `WARNING`
- `ERROR`
- `DEBUG`
- `CRITICAL`

## Hinweis

Die Logdatei wird standardmäßig im Ordner `logs` neben dem aufgerufenen Script gespeichert.
