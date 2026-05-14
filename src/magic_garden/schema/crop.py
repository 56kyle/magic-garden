"""Module defining crops in Magic Garden."""
from typing import ClassVar

from pydantic import BaseModel
from pydantic import ConfigDict

from magic_garden.constants import DEFAULT_PYDANTIC_CONFIG_FROZEN


class Crop(BaseModel):
    """Model representing a crop in Magic Garden."""
    model_config: ClassVar[ConfigDict] = DEFAULT_PYDANTIC_CONFIG_FROZEN


