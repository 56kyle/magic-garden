"""Module containing logic for logging used throughout the magic_garden package."""
from pathlib import Path

from loguru import logger

from magic_garden.constants import APP_START_TIME
from magic_garden.constants import USER_LOG_FOLDER
from magic_garden.constants import _FILE_SAFE_DATETIME_FORMAT


_FILE_SAFE_DATETIME_SLUG: str = APP_START_TIME.strftime(_FILE_SAFE_DATETIME_FORMAT)

LOG_PATH: Path = USER_LOG_FOLDER / f"log_{_FILE_SAFE_DATETIME_SLUG}.log"


logger.add(LOG_PATH, serialize=True)
