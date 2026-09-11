import sys
from datetime import datetime as d
from pathlib import Path as pa
import logging

def save_logfile(log_name=None):
    script_path = pa(sys.argv[0]).resolve().parent
    log_path = script_path / "logs"
    log_path.mkdir(parents=True, exist_ok=True)
    script_name = log_name or pa(sys.argv[0]).resolve().stem or f"log_"
    safe_name = "".join(c if c.isalnum() or c in (' ', '.', '_') else '_' for c in script_name)
    log_file = log_path / f"{safe_name}-{d.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    logging.basicConfig(
        level="INFO",
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding='ascii'),
            logging.StreamHandler()
        ],
        )
    return log_file

_log_file = save_logfile()

def write_log(message, level="info"):
    timestamp = d.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{level.upper()}] {message}"
    if _log_file is not None:
        logging.log(getattr(logging, level.upper(), logging.INFO), log_entry)
    else:
        print(log_entry)

    color = {
        "INFO": "\033[94m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "DEBUG": "\033[92m",
        "CRITICAL": "\033[95m",
        "ENDC": "\033[0m",
    }
    colored_log_entry = f"{color.get(level.upper(), '')}{log_entry}{color['ENDC']}"
    if _log_file is None:
        print(colored_log_entry)

