import numpy as np
import pygame.draw
from sympy import *

SPEED_OF_LIGHT = 299792458  # Meters per Second
REFRACTIVE_INDEX_OF_VACUUM = 1

c = symbols("c")

"""
def place_lens(coord):
    places lens at coord
    
def look(coord):
    
    
def area_of_lens():
    overlap between circles 1 & 2
    
a perfectly rectangular lens would have |r1| == |r2|
(x-h)^2 + (y-k)^2 = r^2



"""



def get_absolute_refractive_index(phase_velocity_in_medium):
    return SPEED_OF_LIGHT / phase_velocity_in_medium


def relative_index_of_refraction_of_b_to_a(speed_in_a, speed_in_b):
    return speed_in_a / speed_in_b

def lens_makers_equation(s1, s2, focal_length):

    if s1 == "unknown":
        s2_reciprocal = 1 / s2
        f_reciprocal = 1 / focal_length
        s1_reciprocal = f_reciprocal - s2_reciprocal
        unknown = 1 / s1_reciprocal
        return unknown

    elif s2 == "unknown":
        s1_reciprocal = 1 / s1
        f_reciprocal = 1 / focal_length
        s2_reciprocal = f_reciprocal - s1_reciprocal
        unknown = 1 / s2_reciprocal
        return unknown

    elif focal_length == "unknown":
        s1_reciprocal = 1 / s1
        s2_reciprocal = 1 / s2
        f_reciprocal = s1_reciprocal + s2_reciprocal
        unknown = 1 / f_reciprocal
        return unknown

    else:
        print("check input:")
        print("1/" + str(s1) + " + 1/" + str(s2) + " = 1/" + str(f))
        return -1


n, r1, r2, d, f = symbols("n r1 r2 d f")
def expanded_lens_makers_equation(solve_for):
    solution = solve((n - 1)((1/r1) - (1/r2) + ((n-1) * d) / (n * r1 * r2)) - (1/f), solve_for)
    return solution

LENSE_TYPES = ["Biconvex",
               "Plano-convex",
               "Positive meniscus",
               "Negative meniscus",
               "Plano-concave",
               "Biconcave"]

CONVEX = "convex"
CONCAVE = "concave"
PLANE = "plane"

DEFAULT = CONVEX

LENS_DRAW_HEIGHT = 100
LENS_DRAW_WIDTH = 20


class Lens:

    FRONT = None
    BACK = None

    CONVERGING = False
    DIVERGING = False

    def __init__(self, focal_length, lens_width, lens_type, front_r, back_r, index_of_refraction=0, lens_pos=(0, 0)):
        self.focal_length = focal_length
        self.lens_width = lens_width
        self.check_lens_type(lens_type)
        self.index_of_refraction = index_of_refraction
        self.front_radius = front_r
        self.back_radius = back_r
        self.front_rect = self.get_front_rect()
        self.back_rect = self.get_back_rect()
        self.lens_pos = lens_pos

    def get_f(self):
        return self.focal_length

    def get_d(self):
        return self.lens_width

    def get_n(self):
        return self.index_of_refraction

    def check_lens_type(self, lens_type):
        if lens_type == "Biconvex":
            self.FRONT = CONVEX
            self.BACK = CONVEX
            self.CONVERGING = True
        elif lens_type == "Plano-convex":
            self.FRONT = CONVEX
            self.BACK = PLANE
        elif lens_type == "Positive meniscus":
            self.FRONT = CONVEX
            self.BACK = CONCAVE
        elif lens_type == "Negative meniscus":
            self.FRONT = CONVEX
            self.BACK = CONCAVE
        elif lens_type == "Plano-concave":
            self.FRONT = PLANE
            self.BACK = CONCAVE
        elif lens_type == "Biconcave":
            self.FRONT = CONCAVE
            self.BACK = CONCAVE
        else:
            print(f"Check Lens Type. Set to {DEFAULT} as Default")
            self.FRONT = DEFAULT
            self.BACK = DEFAULT


    def get_front_rect(self):
        return pygame.Rect()

    def get_back_rect(self):
        pass

    def draw_lens(self):


    def get_distance_from_object(self, image_distance):
        return lens_makers_equation("unknown", image_distance, self.get_f())

    def get_distance_from_image(self, object_distance):
        return lens_makers_equation(object_distance, "unknown", self.get_f())



