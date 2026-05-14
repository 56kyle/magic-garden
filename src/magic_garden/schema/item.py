"""Module defining items in Magic Garden."""
from pydantic import BaseModel


class ItemStack(BaseModel):
    """Model representing an Item in Magic Garden."""
    name: str
