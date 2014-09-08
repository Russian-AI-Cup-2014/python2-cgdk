from model.ActionType import ActionType


class Move:
    def __init__(self):
        self.speed_up = 0.0
        self.turn = 0.0
        self.action = ActionType.NONE
        self.pass_power = 1.0
        self.pass_angle = 0.0
        self.teammate_index = -1