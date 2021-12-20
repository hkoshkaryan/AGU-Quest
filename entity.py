from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char  # character used to represent the entity
        self.color = color  # color used to draw the entity (x,y,z) format

    def move(self, dx: int, dy: int) -> None:
        self.x += dx  # move the entity by a given amount
        self.y += dy