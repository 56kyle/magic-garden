"""Module containing exceptions specific to the magic_garden package."""


class MagicGardenError(Exception):
    """Base class for all exceptions raised by the magic_garden package."""
    error_code: int = 1000


class WindowError(MagicGardenError):
    """Error that indicates some issue relating to the Magic Garden window."""
    error_code: int = 2000


class WindowNotFoundError(WindowError):
    """Error that indicates that the specified window was not found."""
    error_code: int = 2001


class WindowNotActiveError(WindowError):
    """Error that indicates that the specified window exists but is not active."""
    error_code: int = 2002
