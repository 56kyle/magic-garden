"""Module defining seeds in Magic Garden."""
from typing import ClassVar

from pydantic import BaseModel
from pydantic import ConfigDict

from magic_garden.constants import DEFAULT_PYDANTIC_CONFIG_FROZEN


class Seed(BaseModel):
    """Model representing a seed in Magic Garden."""
    model_config: ClassVar[ConfigDict] = DEFAULT_PYDANTIC_CONFIG_FROZEN

    name: str




