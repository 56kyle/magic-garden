"""Module defining weather conditions in Magic Garden."""
import enum


class Weather(enum.Enum):
    """Enum defining weather conditions in Magic Garden."""
    CLEAR = 0
    RAIN = 1
    SNOW = 2
    THUNDER_STORM = 3
    DAWN = 4
    AMBER_MOON = 5


