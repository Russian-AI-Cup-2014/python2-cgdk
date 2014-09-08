import socket
import struct
from model.ActionType import ActionType
from model.Game import Game
from model.Hockeyist import Hockeyist
from model.HockeyistState import HockeyistState
from model.HockeyistType import HockeyistType
from model.Move import Move
from model.Player import Player
from model.PlayerContext import PlayerContext
from model.Puck import Puck
from model.World import World


class RemoteProcessClient:
    LITTLE_ENDIAN_BYTE_ORDER = True

    BYTE_ORDER_FORMAT_STRING = "<" if LITTLE_ENDIAN_BYTE_ORDER else ">"

    SIGNED_BYTE_SIZE_BYTES = 1
    INTEGER_SIZE_BYTES = 4
    LONG_SIZE_BYTES = 8
    DOUBLE_SIZE_BYTES = 8

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self.socket.connect((host, port))
        self.cells = None
        self.cell_visibilities = None

    def write_token_message(self, token):
        self.write_enum(RemoteProcessClient.MessageType.AUTHENTICATION_TOKEN)
        self.write_string(token)

    def read_team_size_message(self):
        message_type = self.read_enum(RemoteProcessClient.MessageType)
        self.ensure_message_type(message_type, RemoteProcessClient.MessageType.TEAM_SIZE)
        return self.read_int()

    def write_protocol_version_message(self):
        self.write_enum(RemoteProcessClient.MessageType.PROTOCOL_VERSION)
        self.write_int(1)

    def read_game_context_message(self):
        message_type = self.read_enum(RemoteProcessClient.MessageType)
        self.ensure_message_type(message_type, RemoteProcessClient.MessageType.GAME_CONTEXT)
        return self.read_game()

    def read_player_context_message(self):
        message_type = self.read_enum(RemoteProcessClient.MessageType)
        if message_type == RemoteProcessClient.MessageType.GAME_OVER:
            return None

        self.ensure_message_type(message_type, RemoteProcessClient.MessageType.PLAYER_CONTEXT)
        return self.read_player_context()

    def write_moves_message(self, moves):
        self.write_enum(RemoteProcessClient.MessageType.MOVES)
        self.write_moves(moves)

    def close(self):
        self.socket.close()

    def read_game(self):
        if not self.read_boolean():
            return None

        return Game(
            self.read_long(), self.read_int(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(),
            self.read_int(), self.read_double(), self.read_double(), self.read_double(), self.read_int(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_int(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_int(), self.read_int(),
            self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(),
            self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(), self.read_int(),
            self.read_double(), self.read_double()
        )

    def write_game(self, game):
        if game is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(game.random_seed)
            self.write_int(game.tick_count)
            self.write_double(game.world_width)
            self.write_double(game.world_height)
            self.write_double(game.goal_net_top)
            self.write_double(game.goal_net_width)
            self.write_double(game.goal_net_height)
            self.write_double(game.rink_top)
            self.write_double(game.rink_left)
            self.write_double(game.rink_bottom)
            self.write_double(game.rink_right)
            self.write_int(game.after_goal_state_tick_count)
            self.write_int(game.overtime_tick_count)
            self.write_int(game.default_action_cooldown_ticks)
            self.write_int(game.swing_action_cooldown_ticks)
            self.write_int(game.cancel_strike_action_cooldown_ticks)
            self.write_int(game.action_cooldown_ticks_after_losing_puck)
            self.write_double(game.stick_length)
            self.write_double(game.stick_sector)
            self.write_double(game.pass_sector)
            self.write_int(game.hockeyist_attribute_base_value)
            self.write_double(game.min_action_chance)
            self.write_double(game.max_action_chance)
            self.write_double(game.strike_angle_deviation)
            self.write_double(game.pass_angle_deviation)
            self.write_double(game.pick_up_puck_base_chance)
            self.write_double(game.take_puck_away_base_chance)
            self.write_int(game.max_effective_swing_ticks)
            self.write_double(game.strike_power_base_factor)
            self.write_double(game.strike_power_growth_factor)
            self.write_double(game.strike_puck_base_chance)
            self.write_double(game.knockdown_chance_factor)
            self.write_double(game.knockdown_ticks_factor)
            self.write_double(game.max_speed_to_allow_substitute)
            self.write_double(game.substitution_area_height)
            self.write_double(game.pass_power_factor)
            self.write_double(game.hockeyist_max_stamina)
            self.write_double(game.active_hockeyist_stamina_growth_per_tick)
            self.write_double(game.resting_hockeyist_stamina_growth_per_tick)
            self.write_double(game.zero_stamina_hockeyist_effectiveness_factor)
            self.write_double(game.speed_up_stamina_cost_factor)
            self.write_double(game.turn_stamina_cost_factor)
            self.write_double(game.take_puck_stamina_cost)
            self.write_double(game.swing_stamina_cost)
            self.write_double(game.strike_stamina_base_cost)
            self.write_double(game.strike_stamina_cost_growth_factor)
            self.write_double(game.cancel_strike_stamina_cost)
            self.write_double(game.pass_stamina_cost)
            self.write_double(game.goalie_max_speed)
            self.write_double(game.hockeyist_max_speed)
            self.write_double(game.struck_hockeyist_initial_speed_factor)
            self.write_double(game.hockeyist_speed_up_factor)
            self.write_double(game.hockeyist_speed_down_factor)
            self.write_double(game.hockeyist_turn_angle_factor)
            self.write_int(game.versatile_hockeyist_strength)
            self.write_int(game.versatile_hockeyist_endurance)
            self.write_int(game.versatile_hockeyist_dexterity)
            self.write_int(game.versatile_hockeyist_agility)
            self.write_int(game.forward_hockeyist_strength)
            self.write_int(game.forward_hockeyist_endurance)
            self.write_int(game.forward_hockeyist_dexterity)
            self.write_int(game.forward_hockeyist_agility)
            self.write_int(game.defenceman_hockeyist_strength)
            self.write_int(game.defenceman_hockeyist_endurance)
            self.write_int(game.defenceman_hockeyist_dexterity)
            self.write_int(game.defenceman_hockeyist_agility)
            self.write_int(game.min_random_hockeyist_parameter)
            self.write_int(game.max_random_hockeyist_parameter)
            self.write_double(game.struck_puck_initial_speed_factor)
            self.write_double(game.puck_binding_range)

    def read_games(self):
        game_count = self.read_int()
        if game_count < 0:
            return None

        games = []

        for game_index in xrange(game_count):
            games.append(self.read_game())

        return games

    def write_games(self, games):
        if games is None:
            self.write_int(-1)
        else:
            self.write_int(games.__len__())

            for game in games:
                self.write_game(game)

    def read_hockeyist(self):
        if not self.read_boolean():
            return None

        return Hockeyist(
            self.read_long(), self.read_long(), self.read_int(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_boolean(), self.read_enum(HockeyistType), self.read_int(), self.read_int(),
            self.read_int(), self.read_int(), self.read_double(), self.read_enum(HockeyistState), self.read_int(),
            self.read_int(), self.read_int(), self.read_int(), self.read_enum(ActionType),
            self.read_int() if self.read_boolean() else None
        )

    def write_hockeyist(self, hockeyist):
        if hockeyist is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(hockeyist.id)
            self.write_long(hockeyist.player_id)
            self.write_int(hockeyist.teammate_index)
            self.write_double(hockeyist.mass)
            self.write_double(hockeyist.radius)
            self.write_double(hockeyist.x)
            self.write_double(hockeyist.y)
            self.write_double(hockeyist.speed_x)
            self.write_double(hockeyist.speed_y)
            self.write_double(hockeyist.angle)
            self.write_double(hockeyist.angular_speed)
            self.write_boolean(hockeyist.teammate)
            self.write_enum(hockeyist.type)
            self.write_int(hockeyist.strength)
            self.write_int(hockeyist.endurance)
            self.write_int(hockeyist.dexterity)
            self.write_int(hockeyist.agility)
            self.write_double(hockeyist.stamina)
            self.write_enum(hockeyist.state)
            self.write_int(hockeyist.original_position_index)
            self.write_int(hockeyist.remaining_knockdown_ticks)
            self.write_int(hockeyist.remaining_cooldown_ticks)
            self.write_int(hockeyist.swing_ticks)
            self.write_enum(hockeyist.last_action)
            if hockeyist.last_action_tick is None:
                self.write_boolean(False)
            else:
                self.write_boolean(True)
                self.write_int(hockeyist.last_action_tick)

    def read_hockeyists(self):
        hockeyist_count = self.read_int()
        if hockeyist_count < 0:
            return None

        hockeyists = []

        for hockeyist_index in xrange(hockeyist_count):
            hockeyists.append(self.read_hockeyist())

        return hockeyists

    def write_hockeyists(self, hockeyists):
        if hockeyists is None:
            self.write_int(-1)
        else:
            self.write_int(hockeyists.__len__())

            for hockeyist in hockeyists:
                self.write_hockeyist(hockeyist)

    def read_move(self):
        if not self.read_boolean():
            return None

        move = Move()

        move.speed_up = self.read_double()
        move.turn = self.read_double()
        move.action = self.read_enum(ActionType)
        if move.action == ActionType.PASS:
            move.pass_power = self.read_double()
            move.pass_angle = self.read_double()
        elif move.action == ActionType.SUBSTITUTE:
            move.teammate_index = self.read_int()

        return move

    def write_move(self, move):
        if move is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_double(move.speed_up)
            self.write_double(move.turn)
            self.write_enum(move.action)
            if move.action == ActionType.PASS:
                self.write_double(move.pass_power)
                self.write_double(move.pass_angle)
            elif move.action == ActionType.SUBSTITUTE:
                self.write_int(move.teammate_index)

    def read_moves(self):
        move_count = self.read_int()
        if move_count < 0:
            return None

        moves = []

        for move_index in xrange(move_count):
            moves.append(self.read_move())

        return moves

    def write_moves(self, moves):
        if moves is None:
            self.write_int(-1)
        else:
            self.write_int(moves.__len__())

            for move in moves:
                self.write_move(move)

    def read_player(self):
        if not self.read_boolean():
            return None

        return Player(
            self.read_long(), self.read_boolean(), self.read_string(), self.read_int(), self.read_boolean(),
            self.read_double(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_boolean(), self.read_boolean()
        )

    def write_player(self, player):
        if player is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(player.id)
            self.write_boolean(player.me)
            self.write_string(player.name)
            self.write_int(player.goal_count)
            self.write_boolean(player.strategy_crashed)
            self.write_double(player.net_top)
            self.write_double(player.net_left)
            self.write_double(player.net_bottom)
            self.write_double(player.net_right)
            self.write_double(player.net_front)
            self.write_double(player.net_back)
            self.write_boolean(player.just_scored_goal)
            self.write_boolean(player.just_missed_goal)

    def read_players(self):
        player_count = self.read_int()
        if player_count < 0:
            return None

        players = []

        for player_index in xrange(player_count):
            players.append(self.read_player())

        return players

    def write_players(self, players):
        if players is None:
            self.write_int(-1)
        else:
            self.write_int(players.__len__())

            for player in players:
                self.write_player(player)

    def read_player_context(self):
        if not self.read_boolean():
            return None

        return PlayerContext(self.read_hockeyists(), self.read_world())

    def write_player_context(self, player_context):
        if player_context is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_hockeyists(player_context.hockeyists)
            self.write_world(player_context.world)

    def read_player_contexts(self):
        player_context_count = self.read_int()
        if player_context_count < 0:
            return None

        player_contexts = []

        for player_context_index in xrange(player_context_count):
            player_contexts.append(self.read_player_context())

        return player_contexts

    def write_player_contexts(self, player_contexts):
        if player_contexts is None:
            self.write_int(-1)
        else:
            self.write_int(player_contexts.__len__())

            for player_context in player_contexts:
                self.write_player_context(player_context)

    def read_puck(self):
        if not self.read_boolean():
            return None

        return Puck(
            self.read_long(), self.read_double(), self.read_double(), self.read_double(), self.read_double(),
            self.read_double(), self.read_double(), self.read_long(), self.read_long()
        )

    def write_puck(self, puck):
        if puck is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_long(puck.id)
            self.write_double(puck.mass)
            self.write_double(puck.radius)
            self.write_double(puck.x)
            self.write_double(puck.y)
            self.write_double(puck.speed_x)
            self.write_double(puck.speed_y)
            self.write_long(puck.owner_hockeyist_id)
            self.write_long(puck.owner_player_id)

    def read_pucks(self):
        puck_count = self.read_int()
        if puck_count < 0:
            return None

        pucks = []

        for puck_index in xrange(puck_count):
            pucks.append(self.read_puck())

        return pucks

    def write_pucks(self, pucks):
        if pucks is None:
            self.write_int(-1)
        else:
            self.write_int(pucks.__len__())

            for puck in pucks:
                self.write_puck(puck)

    def read_world(self):
        if not self.read_boolean():
            return None

        return World(
            self.read_int(), self.read_int(), self.read_double(), self.read_double(), self.read_players(),
            self.read_hockeyists(), self.read_puck()
        )

    def write_world(self, world):
        if world is None:
            self.write_boolean(False)
        else:
            self.write_boolean(True)

            self.write_int(world.tick)
            self.write_int(world.tick_count)
            self.write_double(world.width)
            self.write_double(world.height)
            self.write_players(world.players)
            self.write_hockeyists(world.hockeyists)
            self.write_puck(world.puck)

    def read_worlds(self):
        world_count = self.read_int()
        if world_count < 0:
            return None

        worlds = []

        for world_index in xrange(world_count):
            worlds.append(self.read_world())

        return worlds

    def write_worlds(self, worlds):
        if worlds is None:
            self.write_int(-1)
        else:
            self.write_int(worlds.__len__())

            for world in worlds:
                self.write_world(world)

    def ensure_message_type(self, actual_type, expected_type):
        if actual_type != expected_type:
            raise ValueError("Received wrong message [actual=%s, expected=%s]." % (actual_type, expected_type))

    def read_enum(self, enum_class):
        byte_array = self.read_bytes(RemoteProcessClient.SIGNED_BYTE_SIZE_BYTES)
        value = struct.unpack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "b", byte_array)[0]

        for enum_key, enum_value in enum_class.__dict__.iteritems():
            if not str(enum_key).startswith("__") and value == enum_value:
                return enum_value

        return None

    def write_enum(self, value):
        self.write_bytes(struct.pack(
            RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "b", -1 if value is None else value
        ))

    def read_string(self):
        length = self.read_int()
        if length == -1:
            return None

        byte_array = self.read_bytes(length)
        return byte_array.decode("utf-8")

    def write_string(self, value):
        if value is None:
            self.write_int(-1)
            return

        byte_array = value.encode("utf-8")

        self.write_int(len(byte_array))
        self.write_bytes(byte_array)

    def read_boolean(self):
        byte_array = self.read_bytes(RemoteProcessClient.SIGNED_BYTE_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "b", byte_array)[0] != 0

    def read_boolean_array(self, count):
        byte_array = self.read_bytes(count * RemoteProcessClient.SIGNED_BYTE_SIZE_BYTES)
        unpacked_bytes = struct.unpack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + str(count) + "b", byte_array)

        return [unpacked_bytes[i] != 0 for i in xrange(count)]

    def write_boolean(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "b", 1 if value else 0))

    def read_int(self):
        byte_array = self.read_bytes(RemoteProcessClient.INTEGER_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "i", byte_array)[0]

    def write_int(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "i", value))

    def read_long(self):
        byte_array = self.read_bytes(RemoteProcessClient.LONG_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "q", byte_array)[0]

    def write_long(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "q", value))

    def read_double(self):
        byte_array = self.read_bytes(RemoteProcessClient.DOUBLE_SIZE_BYTES)
        return struct.unpack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "d", byte_array)[0]

    def write_double(self, value):
        self.write_bytes(struct.pack(RemoteProcessClient.BYTE_ORDER_FORMAT_STRING + "d", value))

    def read_bytes(self, byte_count):
        byte_array = ''

        while len(byte_array) < byte_count:
            chunk = self.socket.recv(byte_count - len(byte_array))

            if not len(chunk):
                raise IOError("Can't read %s bytes from input stream." % str(byte_count))

            byte_array += chunk

        return byte_array

    def write_bytes(self, byte_array):
        self.socket.sendall(byte_array)

    class MessageType:
        UNKNOWN = 0
        GAME_OVER = 1
        AUTHENTICATION_TOKEN = 2
        TEAM_SIZE = 3
        PROTOCOL_VERSION = 4
        GAME_CONTEXT = 5
        PLAYER_CONTEXT = 6
        MOVES = 7