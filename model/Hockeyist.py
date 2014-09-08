from model.Unit import Unit


class Hockeyist(Unit):
    def __init__(self, id, player_id, teammate_index, mass, radius, x, y, speed_x, speed_y, angle, angular_speed,
                 teammate, type, strength, endurance, dexterity, agility, stamina, state, original_position_index,
                 remaining_knockdown_ticks, remaining_cooldown_ticks, swing_ticks, last_action, last_action_tick):
        Unit.__init__(self, id, mass, radius, x, y, speed_x, speed_y, angle, angular_speed)

        self.player_id = player_id
        self.teammate_index = teammate_index
        self.teammate = teammate
        self.type = type
        self.strength = strength
        self.endurance = endurance
        self.dexterity = dexterity
        self.agility = agility
        self.stamina = stamina
        self.state = state
        self.original_position_index = original_position_index
        self.remaining_knockdown_ticks = remaining_knockdown_ticks
        self.remaining_cooldown_ticks = remaining_cooldown_ticks
        self.swing_ticks = swing_ticks
        self.last_action = last_action
        self.last_action_tick = last_action_tick