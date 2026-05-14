"""Module containing types being used throughout the magic_garden package."""
import enum
from typing import TypeAlias


Hotkey: TypeAlias = int | str | list[int | list[int] | tuple[int, ...]] | tuple[int | list[int] | tuple[int, ...], ...]


class GameDirection(enum.Enum):
    """Enum defining a game direction."""
    UP = "w"
    DOWN = "s"
    RIGHT = "d"
    LEFT = "a"
