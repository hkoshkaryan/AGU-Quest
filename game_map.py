from __future__ import annotations

from typing import Iterable, TYPE_CHECKING, Optional

import numpy as np  # type: ignore
from tcod.console import Console

import tile_types

if TYPE_CHECKING:
    from entity import Entity

class GameMap:
    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width, self.height=width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")
        """Line above creates a 2d array, fill with the same value of tile_types.floor"""

        self.visible = np.full((width, height), fill_value=False, order="F")  # Tiles that are visible
        self.explored = np.full((width, height), fill_value=False, order="F")  # Tiles that have been seen

    def get_blocking_entity_at_location(self, location_x: int, location_y: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.blocks_movement and entity.x == location_x and entity.y == location_y:
                return entity

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of the map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """Renders our map
        If a tile is in the "visible" array, draw it using "light" colors, if it isn't, but is in the
        explored array, draw using "dark", else draw using Shroud
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=[tile_types.SHROUD]
        )

        for entity in self.entities:
            # Only print entities in FoV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)