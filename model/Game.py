from math import *


class Game:
    def __init__(self, random_seed, tick_count, world_width, world_height, goal_net_top, goal_net_width,
                 goal_net_height, rink_top, rink_left, rink_bottom, rink_right, after_goal_state_tick_count,
                 overtime_tick_count, default_action_cooldown_ticks, swing_action_cooldown_ticks,
                 cancel_strike_action_cooldown_ticks, action_cooldown_ticks_after_losing_puck, stick_length,
                 stick_sector, pass_sector, hockeyist_attribute_base_value, min_action_chance, max_action_chance,
                 strike_angle_deviation, pass_angle_deviation, pick_up_puck_base_chance, take_puck_away_base_chance,
                 max_effective_swing_ticks, strike_power_base_factor, strike_power_growth_factor,
                 strike_puck_base_chance, knockdown_chance_factor, knockdown_ticks_factor,
                 max_speed_to_allow_substitute, substitution_area_height, pass_power_factor, hockeyist_max_stamina,
                 active_hockeyist_stamina_growth_per_tick, resting_hockeyist_stamina_growth_per_tick,
                 zero_stamina_hockeyist_effectiveness_factor, speed_up_stamina_cost_factor, turn_stamina_cost_factor,
                 take_puck_stamina_cost, swing_stamina_cost, strike_stamina_base_cost,
                 strike_stamina_cost_growth_factor, cancel_strike_stamina_cost, pass_stamina_cost, goalie_max_speed,
                 hockeyist_max_speed, struck_hockeyist_initial_speed_factor, hockeyist_speed_up_factor,
                 hockeyist_speed_down_factor, hockeyist_turn_angle_factor, versatile_hockeyist_strength,
                 versatile_hockeyist_endurance, versatile_hockeyist_dexterity, versatile_hockeyist_agility,
                 forward_hockeyist_strength, forward_hockeyist_endurance, forward_hockeyist_dexterity,
                 forward_hockeyist_agility, defenceman_hockeyist_strength, defenceman_hockeyist_endurance,
                 defenceman_hockeyist_dexterity, defenceman_hockeyist_agility, min_random_hockeyist_parameter,
                 max_random_hockeyist_parameter, struck_puck_initial_speed_factor, puck_binding_range):
        self.random_seed = random_seed
        self.tick_count = tick_count
        self.world_width = world_width
        self.world_height = world_height
        self.goal_net_top = goal_net_top
        self.goal_net_width = goal_net_width
        self.goal_net_height = goal_net_height
        self.rink_top = rink_top
        self.rink_left = rink_left
        self.rink_bottom = rink_bottom
        self.rink_right = rink_right
        self.after_goal_state_tick_count = after_goal_state_tick_count
        self.overtime_tick_count = overtime_tick_count
        self.default_action_cooldown_ticks = default_action_cooldown_ticks
        self.swing_action_cooldown_ticks = swing_action_cooldown_ticks
        self.cancel_strike_action_cooldown_ticks = cancel_strike_action_cooldown_ticks
        self.action_cooldown_ticks_after_losing_puck = action_cooldown_ticks_after_losing_puck
        self.stick_length = stick_length
        self.stick_sector = stick_sector
        self.pass_sector = pass_sector
        self.hockeyist_attribute_base_value = hockeyist_attribute_base_value
        self.min_action_chance = min_action_chance
        self.max_action_chance = max_action_chance
        self.strike_angle_deviation = strike_angle_deviation
        self.pass_angle_deviation = pass_angle_deviation
        self.pick_up_puck_base_chance = pick_up_puck_base_chance
        self.take_puck_away_base_chance = take_puck_away_base_chance
        self.max_effective_swing_ticks = max_effective_swing_ticks
        self.strike_power_base_factor = strike_power_base_factor
        self.strike_power_growth_factor = strike_power_growth_factor
        self.strike_puck_base_chance = strike_puck_base_chance
        self.knockdown_chance_factor = knockdown_chance_factor
        self.knockdown_ticks_factor = knockdown_ticks_factor
        self.max_speed_to_allow_substitute = max_speed_to_allow_substitute
        self.substitution_area_height = substitution_area_height
        self.pass_power_factor = pass_power_factor
        self.hockeyist_max_stamina = hockeyist_max_stamina
        self.active_hockeyist_stamina_growth_per_tick = active_hockeyist_stamina_growth_per_tick
        self.resting_hockeyist_stamina_growth_per_tick = resting_hockeyist_stamina_growth_per_tick
        self.zero_stamina_hockeyist_effectiveness_factor = zero_stamina_hockeyist_effectiveness_factor
        self.speed_up_stamina_cost_factor = speed_up_stamina_cost_factor
        self.turn_stamina_cost_factor = turn_stamina_cost_factor
        self.take_puck_stamina_cost = take_puck_stamina_cost
        self.swing_stamina_cost = swing_stamina_cost
        self.strike_stamina_base_cost = strike_stamina_base_cost
        self.strike_stamina_cost_growth_factor = strike_stamina_cost_growth_factor
        self.cancel_strike_stamina_cost = cancel_strike_stamina_cost
        self.pass_stamina_cost = pass_stamina_cost
        self.goalie_max_speed = goalie_max_speed
        self.hockeyist_max_speed = hockeyist_max_speed
        self.struck_hockeyist_initial_speed_factor = struck_hockeyist_initial_speed_factor
        self.hockeyist_speed_up_factor = hockeyist_speed_up_factor
        self.hockeyist_speed_down_factor = hockeyist_speed_down_factor
        self.hockeyist_turn_angle_factor = hockeyist_turn_angle_factor
        self.versatile_hockeyist_strength = versatile_hockeyist_strength
        self.versatile_hockeyist_endurance = versatile_hockeyist_endurance
        self.versatile_hockeyist_dexterity = versatile_hockeyist_dexterity
        self.versatile_hockeyist_agility = versatile_hockeyist_agility
        self.forward_hockeyist_strength = forward_hockeyist_strength
        self.forward_hockeyist_endurance = forward_hockeyist_endurance
        self.forward_hockeyist_dexterity = forward_hockeyist_dexterity
        self.forward_hockeyist_agility = forward_hockeyist_agility
        self.defenceman_hockeyist_strength = defenceman_hockeyist_strength
        self.defenceman_hockeyist_endurance = defenceman_hockeyist_endurance
        self.defenceman_hockeyist_dexterity = defenceman_hockeyist_dexterity
        self.defenceman_hockeyist_agility = defenceman_hockeyist_agility
        self.min_random_hockeyist_parameter = min_random_hockeyist_parameter
        self.max_random_hockeyist_parameter = max_random_hockeyist_parameter
        self.struck_puck_initial_speed_factor = struck_puck_initial_speed_factor
        self.puck_binding_range = puck_binding_range