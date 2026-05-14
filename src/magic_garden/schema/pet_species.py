"""Module defining pet species in Magic Garden."""
from pydantic import BaseModel

from magic_garden.schema.pet_ability import PetAbility


class PetSpecies(BaseModel):
    """Model representing a pet species in Magic Garden."""
    name: str
    available_abilities: set[PetAbility]
