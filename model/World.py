class World:
    def __init__(self, tick, tick_count, width, height, players, hockeyists, puck):
        self.tick = tick
        self.tick_count = tick_count
        self.width = width
        self.height = height
        self.players = players
        self.hockeyists = hockeyists
        self.puck = puck

    def get_my_player(self):
        for player in self.players:
            if player.me:
                return player

        return None

    def get_opponent_player(self):
        for player in self.players:
            if not player.me:
                return player

        return None