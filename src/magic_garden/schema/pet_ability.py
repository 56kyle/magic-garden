"""Module defining pet abilities in Magic Garden."""
import enum

from pydantic import BaseModel


class PetAbilityType(enum.Enum):
    """Enum defining types of pet abilities."""
    COIN_FINDER = "coin_finder"
    CROP_EATER = "crop_eater"
    CROP_REFUND = "crop_refund"
    CROP_SIZE_BOOST = "crop_size_boost"
    DAWN_CAPTURE = "dawn_capture"
    DOUBLE_HARVEST = "double_harvest"
    DOUBLE_HATCH = "double_hatch"
    EGG_GROWTH_BOOST = "egg_growth_boost"
    GRANTER = "granter"
    HATCH_XP_BOOST = "hatch_xp_boost"
    HUNGER_BOOST = "hunger_boost"
    HUNGER_RESTORE = "hunger_restore"
    MAX_STRENGTH_BOOST = "max_strength_boost"
    PET_MUTATION_BOOST = "pet_mutation_boost"
    PET_REFUND = "pet_refund"
    PLANT_GROWTH_BOOST = "plant_growth_boost"
    SEED_FINDER = "seed_finder"
    SELL_BOOST = "sell_boost"
    WEATHER_MUTATION_BOOST = "weather_mutation_boost"
    XP_BOOST = "xp_boost"


class PetAbility(BaseModel):
    """Model defining pet abilities in Magic Garden."""
    ability_type: PetAbilityType
    tier: int
