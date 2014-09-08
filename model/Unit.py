from math import *


class Unit:
    def __init__(self, id, mass, radius, x, y, speed_x, speed_y, angle, angular_speed):
        self.id = id
        self.mass = mass
        self.radius = radius
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.angle = angle
        self.angular_speed = angular_speed

    def get_angle_to(self, x, y):
        absolute_angle_to = atan2(y - self.y, x - self.x)
        relative_angle_to = absolute_angle_to - self.angle

        while relative_angle_to > pi:
            relative_angle_to -= 2.0 * pi

        while relative_angle_to < -pi:
            relative_angle_to += 2.0 * pi

        return relative_angle_to

    def get_angle_to_unit(self, unit):
        return self.get_angle_to(unit.x, unit.y)

    def get_distance_to(self, x, y):
        return hypot(x - self.x, y - self.y)

    def get_distance_to_unit(self, unit):
        return self.get_distance_to(unit.x, unit.y)