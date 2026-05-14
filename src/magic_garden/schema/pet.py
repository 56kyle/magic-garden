"""Module defining pets in Magic Garden."""
from pydantic import BaseModel

from magic_garden.schema.pet_ability import PetAbility
from magic_garden.schema.pet_mutation import PetMutation
from magic_garden.schema.pet_species import PetSpecies


class Pet(BaseModel):
    """Model representing a pet in Magic Garden."""
    species: PetSpecies
    mutation: PetMutation
    abilities: set[PetAbility]
