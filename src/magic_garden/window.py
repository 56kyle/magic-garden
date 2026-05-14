"""Module for handling operations relating to application windows throughout the magic_garden package."""
from functools import wraps
from typing import Callable
from typing import Optional
from typing import ParamSpec
from typing import TypeVar

from pywinctl import getActiveWindow

from pywinctl import getAllWindows
from pywinctl._main import BaseWindow

from magic_garden.constants import MAGIC_GARDEN_WINDOW_TITLE
from magic_garden.exceptions import WindowNotActiveError
from magic_garden.exceptions import WindowNotFoundError


T = TypeVar("T")
P = ParamSpec("P")


def requires_magic_garden_active_window(fn: Callable[P, T]) -> Callable[P, T]:
    """Returns a decorator that validates that Magic Garden is the active window prior to the function running."""
    return requires_active_window(MAGIC_GARDEN_WINDOW_TITLE)(fn)


def requires_active_window(window_name: str) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Returns a decorator that validates a window with the provided title is active prior to the function running."""

    def decorator(fn: Callable[P, T]) -> Callable[P, T]:
        """Decorator that validates the correct window is active prior to running the function."""

        @wraps
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            """Wraps the original function with the desired window check."""
            window: Optional[BaseWindow] = getActiveWindow()
            if window is None:
                raise WindowNotFoundError(f"Could not find a window with title '{window_name}'.")

            if window_name not in window.title:
                raise WindowNotActiveError(f"Magic Garden window is not active, instead '{window.title}' is active.")

            if not window.isActive:
                raise WindowNotActiveError(f"Window containing '{window_name}' in title is not active.")
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def get_window_from_pid(pid: int) -> BaseWindow:
    """Run executable at the provided path and return its window."""
    for window in getAllWindows():
        if window.getPID() == pid:
            return window
    raise ValueError("Could not find window with given PID for the Launcher.")
