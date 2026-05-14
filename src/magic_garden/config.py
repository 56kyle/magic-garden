"""Module responsible for handling config used throughout the magic_garden package."""
import os
from functools import lru_cache
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from magic_garden.constants import DEFAULT_CONFIG_PATH
from magic_garden.constants import DEFAULT_PYDANTIC_SETTINGS


class Config(BaseSettings):
    """The primary config for the magic_garden package."""
    model_config: ClassVar[SettingsConfigDict] = DEFAULT_PYDANTIC_SETTINGS


@lru_cache
def load_config(path: Path = DEFAULT_CONFIG_PATH) -> Config:
    """Load the config for the magic_garden package."""
    load_dotenv(path)
    return Config()
