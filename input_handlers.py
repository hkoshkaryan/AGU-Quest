from typing import Optional  # type hinting, optional denotes none possible

import tcod.event  # importing tcod's event system only.

from actions import Action, EscapeAction, MovementAction  # imports from the actions.py file


class EventHandler(tcod.event.EventDispatch[Action]):  # create EventHandler, send event to proper method based on input
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:  # exits when hitting exit button in top right
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:  # take in keypress, return a method or none
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action
