class Action:
    pass


class EscapeAction(Action):  # exits our game
    pass


class MovementAction(Action):  # movement actions of the player
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx  # describes what direction the player is attempting to move.
        self.dy = dy
