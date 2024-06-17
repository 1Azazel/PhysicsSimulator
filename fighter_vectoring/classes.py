import pygame
import random as r
from useful_math_functions import distance_formula


VISION_RANGE = 1000


class Plane:
    def __init__(self, current_pos, air_wing, aircraft_type, vision=VISION_RANGE):
        self.pos, self.pos_vector = self.set_pos(current_pos)
        self.wing = air_wing
        self.aircraft_type = aircraft_type
        self.name = self.aircraft_type + " " + air_wing.get_designation()
        self.vision = vision
        self.flight_path = []
        self.spot_list = []
        self.incoming_transmissions = []

    def set_pos(self, pos):
        if pos.type is pygame.Vector2:
            self.pos_vector = pos
            self.pos = (pos.x, pos.y)
        else:
            self.pos = pos
            self.pos_vector = pygame.Vector2(pos)
        return self.pos, self.pos_vector

    def get_pos(self):
        return self.pos

    def get_aircraft_type(self):
        return self.aircraft_type

    def set_name(self):
        self.name = self.aircraft_type
        designation = self.wing.get_designation()
        if designation.isAlpha():
            self.name = self.aircraft_type + " " + designation
        elif designation.isNumeric():
            self.name = self.aircraft_type + " " + str(designation)




    def log_flight_path(self, location):
        self.flight_path.append(location)

    def spot_enemy(self, enemy):
        distance = distance_formula(self.get_pos(), enemy.get_pos())
        if self.vision > distance >= self.vision / 2:
            self.spot_list.append(enemy.spotted("long"))
            return 1
        elif self.vision / 2 > distance >= self.vision / 4:
            self.spot_list.append(enemy.spotted("mid"))
            return 1
        elif self.vision / 4 > distance:
            self.spot_list.append(enemy.spotted("close"))
            return 1
        else:
            return 0

    def nothing_spotted(self):
        self.spot_list.append("Nothing Spotted")

    def observe(self, enemy_list):
        visible_enemies = 0
        for enemy in enemy_list:
            visible_enemies += self.spot_enemy(enemy)
        if visible_enemies == 0:
            self.nothing_spotted()

    def spotted(self, spot_range):

        report = ""

        half_vision = str(VISION_RANGE / 2)
        quarter_vision = str(VISION_RANGE / 4)

        distance = "Distance: "
        distance_range = -1

        seen_at = "Spotted at: " + str(self.get_pos())

        aircraft_type = self.get_aircraft_type()
        aircraft = "Aircraft: " + str(aircraft_type)

        if spot_range == "long":
            distance_range = half_vision + " - " + str(VISION_RANGE)

        elif spot_range == "mid":
            distance_range = quarter_vision + " - " + half_vision

        elif spot_range == "close":
            distance_range = "0 - " + quarter_vision

        distance = distance + distance_range

        report_elements = [distance, seen_at, aircraft]
        for element in report_elements:
            report = element + "/n" + report

    def radio(self, message, recipient=None):
        if recipient is None:
            for plane in self.wing:
                plane.receive_transmission(message)
        else:
            recipient.recieve_transmission(message)

    def receive_transmission(self, message):
        self.incoming_transmissions.append(message)


