from math import *
from model.ActionType import ActionType


class MyStrategy:
    def move(self, me, world, game, move):
        move.speed_up = -1.0
        move.turn = pi
        move.action = ActionType.STRIKE