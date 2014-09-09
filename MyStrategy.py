from math import *

from model.ActionType import ActionType
from model.Game import Game
from model.Hockeyist import Hockeyist
from model.Move import Move
from model.World import World



class MyStrategy:
    def move(self, me, world, game, move):
        """
        @type me: Hockeyist
        @type world: World
        @type game: Game
        @type move: Move
        """
        move.speed_up = -1.0
        move.turn = pi
        move.action = ActionType.STRIKE
