class Player:
    def __init__(self, id, me, name, goal_count, strategy_crashed, net_top, net_left, net_bottom, net_right, net_front,
                 net_back, just_scored_goal, just_missed_goal):
        self.id = id
        self.me = me
        self.name = name
        self.goal_count = goal_count
        self.strategy_crashed = strategy_crashed
        self.net_top = net_top
        self.net_left = net_left
        self.net_bottom = net_bottom
        self.net_right = net_right
        self.net_front = net_front
        self.net_back = net_back
        self.just_scored_goal = just_scored_goal
        self.just_missed_goal = just_missed_goal