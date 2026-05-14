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


def teleport_to_buy() -> None:
    """Teleports the player to the buying shops."""


def teleport_to_garden() -> None:
    """Teleports the player to their garden."""
    tap_key(hotkey="shift+2")


def teleport_to_sell() -> None:
    """Teleports the player to the selling shops."""
    tap_key(hotkey="shift+3")


def toggle_inventory() -> None:
    """Toggles the player's inventory open or closed."""
    tap_key(hotkey="e")


def move_character(direction: GameDirection, amount: int = 1) -> None:
    """Move the character in the given direction."""
    for _ in range(amount):
        tap_key(hotkey=direction.value)


def tap_interaction() -> None:
    """Taps the interact key for a random duration that activates tap based interactions in Magic Garden"""
    tap_key(hotkey="space")


def hold_interaction() -> None:
    """Holds down the interact key for a random duration that activates hold based interactions in Magic Garden."""
    hold_key_varied(hotkey="space", min_duration=HOLD_INTERACT_MIN, max_duration=HOLD_INTERACT_MAX)


def tap_key(hotkey: Hotkey) -> None:
    """Taps the provided hotkey for a random duration that resembles a quick tap."""
    hold_key_varied(hotkey=hotkey, min_duration=QUICK_TAP_MIN, max_duration=QUICK_TAP_MAX)


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
