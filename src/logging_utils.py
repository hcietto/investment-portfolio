# src/logging_utils.py

"""
Description: Utility functions to manage pipeline logging lifecycle.

Last update:
    Date: 12-16-2025
    Updated by: Cietto
    Changes made:
        - Creation
"""

import logging
from pathlib import Path
from datetime import datetime
import shutil

LOG_DIR = Path("logs")
HISTORY_DIR = LOG_DIR / "history"
LOG_FILE = LOG_DIR / "pipeline.log"

def close_logging_handlers():

    # Closes all active logging handlers to release file locks (Windows fix).
    for handler in logging.root.handlers[:]:
        handler.close()
        logging.root.removeHandler(handler)

def rotate_logs():

    # Moves the previous execution log to a history folder and prepares a clean log file for the new execution.
    LOG_DIR.mkdir(exist_ok=True)
    HISTORY_DIR.mkdir(exist_ok=True)

    if LOG_FILE.exists():
        close_logging_handlers()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archived_log = HISTORY_DIR / f"pipeline_{timestamp}.log"

        shutil.move(LOG_FILE, archived_log)


def setup_logging():

    # Configures logging for the current execution.
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True  # Ensures reconfiguration of logging
    )
