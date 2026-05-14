"""Module containing constants used throughout the magic_garden package."""
import datetime
from pathlib import Path

from platformdirs import user_cache_path
from platformdirs import user_config_path
from platformdirs import user_data_path
from platformdirs import user_log_path
from platformdirs import user_runtime_path
from pydantic import ConfigDict
from pydantic_settings import SettingsConfigDict


_FILE_SAFE_DATETIME_FORMAT: str = "%Y-%m-%d_%H-%M-%S"


APP_NAME: str = "magic-garden"
APP_AUTHOR: str = "56kyle"
APP_START_TIME: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)

USER_CONFIG_FOLDER: Path = user_config_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)
USER_CACHE_FOLDER: Path = user_cache_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)
USER_DATA_FOLDER: Path = user_data_path(appname=APP_NAME, appauthor=APP_AUTHOR)
USER_RUNTIME_FOLDER: Path = user_runtime_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)
USER_LOG_FOLDER: Path = user_log_path(appname=APP_NAME, appauthor=APP_AUTHOR, ensure_exists=True)

DEFAULT_CONFIG_PATH: Path = USER_CONFIG_FOLDER / ".env"

DEFAULT_PYDANTIC_CONFIG: ConfigDict = ConfigDict(arbitrary_types_allowed=True)
DEFAULT_PYDANTIC_CONFIG_FROZEN: ConfigDict = ConfigDict(arbitrary_types_allowed=True, frozen=True)
DEFAULT_PYDANTIC_SETTINGS: SettingsConfigDict = SettingsConfigDict(
    arbitrary_types_allowed=True,
    env_nested_delimiter="__",
    env_prefix="MAGIC_GARDEN__"
)


MAGIC_GARDEN_WINDOW_TITLE: str = "#magic-garden"


REPO_ROOT: Path = Path(__file__).parent.parent.parent
