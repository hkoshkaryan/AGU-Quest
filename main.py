#!urs/bin/env python3
import tcod

from actions import EscapeAction, MovementAction  # importing from other files
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80  # variables for screen size
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD  # Telling tcod what font to use
    )

    event_handler = EventHandler()  # instance of our EventHandler() class

    with tcod.context.new_terminal(  # codeblock that creates the screen
            screen_width,
            screen_height,
            tileset=tileset,
            title="AGU Quest",
            vsync=True,
    ) as context:  # console which we draw to
        root_console = tcod.Console(screen_width, screen_height, order="F")  # "F" makes numpy access arrays in x,y
        while True:  # game loop, won't end until we close the game.
            root_console.print(x=player_x, y=player_y, string="@")  # control the initial position of the "@"

            context.present(root_console)  # updates the screen, required.

            root_console.clear()

            for event in tcod.event.wait():  # allows us to exit the program without crashing.
                action = event_handler.dispatch(event)  # send event to dispatch, return action to action

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":  # boilerplate code that stops the user from accidentally invoking the script
    main()
