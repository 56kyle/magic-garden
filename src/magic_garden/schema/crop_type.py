"""Module defining types of crops in Magic Garden."""
import enum
from typing import ClassVar

from pydantic import BaseModel
from pydantic import ConfigDict

from magic_garden.constants import DEFAULT_PYDANTIC_CONFIG_FROZEN


class CropHarvestBehavior(enum.Enum):
    """Enum representing the harvest behavior for a crop type."""
    SINGLE_HARVEST = "SINGLE_HARVEST"
    MULTI_HARVEST = "MULTI_HARVEST"


class CropType(BaseModel):
    """Model representing a crop type in Magic Garden."""
    model_config: ClassVar[ConfigDict] = DEFAULT_PYDANTIC_CONFIG_FROZEN

    name: str
    harvest_behavior: CropHarvestBehavior
    harvest_amount: int




