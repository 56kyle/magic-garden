"""Module containing functionalities that enable interacting with the Magic Garden app."""
import random
import time

import keyboard

from magic_garden._types import GameDirection
from magic_garden._types import Hotkey
from magic_garden.window import requires_magic_garden_active_window


QUICK_TAP_MIN: float = 0.01
QUICK_TAP_MAX: float = 0.06

HOLD_INTERACT_MIN: float = 0.5
HOLD_INTERACT_MAX: float = 0.6


@requires_magic_garden_active_window
def move_character(direction: GameDirection) -> None:
    """Move the character in the given direction."""
    hold_key_varied(hotkey=direction.value, min_duration=QUICK_TAP_MIN, max_duration=QUICK_TAP_MAX)


@requires_magic_garden_active_window
def interact_tap() -> None:
    """Have the Magic Garden character interact with the current space."""
    hold_key_varied(hotkey="space", min_duration=QUICK_TAP_MIN, max_duration=QUICK_TAP_MAX)


@requires_magic_garden_active_window
def interact_hold() -> None:
    """Have the Magic Garden character interact with the current space by holding space."""
    hold_key_varied(hotkey="space", min_duration=HOLD_INTERACT_MIN, max_duration=HOLD_INTERACT_MAX)


@requires_magic_garden_active_window
def hold_key_varied(hotkey: Hotkey, min_duration: float, max_duration: float) -> None:
    """Press and release the provided hotkey for a random duration within the bounds set."""
    altered_duration: float = random.uniform(a=min_duration, b=max_duration)
    hold_key(hotkey=hotkey, duration=altered_duration)


@requires_magic_garden_active_window
def hold_key(hotkey: Hotkey, duration: float) -> None:
    """Press and release the provided hotkey for the duration set."""
    try:
        keyboard.press(hotkey=hotkey)
        time.sleep(duration)
    finally:
        keyboard.release(hotkey=hotkey)
