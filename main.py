#!urs/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80  # variables for screen size
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD  # Telling tcod what font to use
    )

    event_handler = EventHandler()  # instance of our EventHandler() class

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(  # codeblock that creates the screen
            screen_width,
            screen_height,
            tileset=tileset,
            title="AGU Quest",
            vsync=True,
    ) as context:  # console which we draw to
        root_console = tcod.Console(screen_width, screen_height, order="F")  # "F" makes numpy access arrays in x,y
        while True:  # game loop, won't end until we close the game.
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":  # boilerplate code that stops the user from accidentally invoking the script
    main()
