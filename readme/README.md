# Liplog

A simple Python logging package for creating a log file in the project folder while also printing messages to the console.

## Language

- [README German](README-de.md)

## Features

- Automatic creation of a log folder
- Timestamped log files
- Console output in real time
- Simple API for quick integration

## Installation

Install from PyPI:

```bash
python -m pip install liplog
```

Install directly from GitHub:

```bash
git clone https://github.com/R0g3rT/liplog.git
cd liplog
python -m pip install .
```

Update:

```bash
python -m pip install --upgrade liplog
```

Uninstall:

```bash
python -m pip uninstall liplog
```

## Usage

```python
from liplog import write_log

write_log("API client started", "INFO")
write_log("Important warning", "WARNING")
write_log("An error occurred", "ERROR")
```

Sample output:

```text
[2026-09-14 12:00:00] [INFO] API client started
[2026-09-14 12:00:01] [WARNING] Important warning
[2026-09-14 12:00:02] [ERROR] An error occurred
```

## Supported Log Levels

- `INFO`
- `WARNING`
- `ERROR`
- `SUCCESS`
- `CRITICAL`
- `RUN`

## Note

By default, the log file is saved in a `logs` folder next to the script that was executed.