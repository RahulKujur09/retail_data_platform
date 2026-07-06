import logging
from datetime import datetime

from src.common.paths import PROJECT_ROOT

LOG_DIR = PROJECT_ROOT/"logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_DIR_SUBFOLDER = LOG_DIR/datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
LOG_DIR_SUBFOLDER.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR_SUBFOLDER/"retail_data_platform.log"

logger = logging.getLogger("retail_data_platform")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)