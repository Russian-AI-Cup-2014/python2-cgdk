from model.Unit import Unit


class Puck(Unit):
    def __init__(self, id, mass, radius, x, y, speed_x, speed_y, owner_hockeyist_id, owner_player_id):
        Unit.__init__(self, id, mass, radius, x, y, speed_x, speed_y, 0.0, 0.0)

        self.owner_hockeyist_id = owner_hockeyist_id
        self.owner_player_id = owner_player_id