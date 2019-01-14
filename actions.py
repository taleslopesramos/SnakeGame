from enum import Enum

class Action(Enum):
	DEFAULT = 0
	MOVE_RIGHT = 1
	MOVE_DOWN = 2
	MOVE_LEFT = 3
	MOVE_UP = 4
	EXIT = 5

class ActionType(Enum):
	DEFAULT = 0
	MOVE_ACTION = 1
	MENU_ACTION = 2