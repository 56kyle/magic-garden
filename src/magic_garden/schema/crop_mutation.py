"""Module defining crop mutations in Magic Garden."""
from typing import ClassVar

from pydantic import BaseModel
from pydantic import ConfigDict

from magic_garden.constants import DEFAULT_PYDANTIC_CONFIG_FROZEN


class CropMutation(BaseModel):
    """Model representing a crop mutation in Magic Garden."""
    model_config: ClassVar[ConfigDict] = DEFAULT_PYDANTIC_CONFIG_FROZEN

    name: str
    multiplier: int


CROP_MUTATION_WET: CropMutation = CropMutation(name="wet", multiplier=2)
CROP_MUTATION_CHILLED: CropMutation = CropMutation(name="chilled", multiplier=2)
CROP_MUTATION_FROZEN: CropMutation = CropMutation(name="frozen", multiplier=6)
CROP_MUTATION_THUNDERSTRUCK: CropMutation = CropMutation(name="thunderstruck", multiplier=5)
CROP_MUTATION_DAWNLIT: CropMutation = CropMutation(name="dawnlit", multiplier=4)
CROP_MUTATION_AMBERLIT: CropMutation = CropMutation(name="amberlit", multiplier=6)
CROP_MUTATION_DAWNBOUND: CropMutation = CropMutation(name="dawnbound", multiplier=7)
CROP_MUTATION_AMBERBOUND: CropMutation = CropMutation(name="amberbound", multiplier=10)
CROP_MUTATION_GOLD: CropMutation = CropMutation(name="gold", multiplier=25)
CROP_MUTATION_RAINBOW: CropMutation = CropMutation(name="rainbow", multiplier=50)
