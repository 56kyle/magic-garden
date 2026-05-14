"""Module for measuring and interacting with the Magic Garden game state."""
from magic_garden.schema.weather import Weather


class GameState:
    """Class representing a particular instance in time of the Magic Garden game."""

    player_count: int
    weather: Weather
