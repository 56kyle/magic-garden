"""Module for interacting with the players garden in Magic Garden."""
import time

from magic_garden._types import GameDirection
from magic_garden.interact import move_character
from magic_garden.interact import teleport_to_garden


def home_garden_position() -> None:
    """Move the player to the top left corner of the garden regardless of starting position."""
    for _ in range(12):
        teleport_to_garden()
        move_character(direction=GameDirection.LEFT, amount=2)
        move_character(direction=GameDirection.UP)


if __name__ == "__main__":
    time.sleep(5)
    home_garden_position()
