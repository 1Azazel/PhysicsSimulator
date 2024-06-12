import inspect
import math
import pygame
import numpy as np

import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d


pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0.0, 900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

# containers
box_size = 200
w = screen.get_width()
h = screen.get_height()
for i in range(6):
    sw = pymunk.Segment(space.static_body, (0, i * box_size), (w, i * box_size), 1)
    sw.friction = 1
    sw.elasticity = 1
    sh = pymunk.Segment(
        space.static_body, (i * box_size, 0), (i * box_size, h - box_size), 1
    )
    sh.friction = 1
    sh.elasticity = 1
    space.add(sw, sh)


def add_ball(space, pos, box_offset):
    body = pymunk.Body()
    body.position = Vec2d(*pos) + box_offset
    shape = pymunk.Circle(body, 20)
    shape.mass = 1
    shape.friction = 0.7
    space.add(body, shape)
    return body


def add_bar(space, pos, box_offset):
    body = pymunk.Body()
    body.position = Vec2d(*pos) + box_offset
    shape = pymunk.Segment(body, (0, 40), (0, -40), 6)
    shape.mass = 2
    shape.friction = 0.7
    space.add(body, shape)
    return body

def add_lever(space, pos, box_offset):
    body = pymunk.Body()
    body.position = pos + Vec2d(*box_offset) + (0, -20)
    shape = pymunk.Segment(body, (0, 20), (0, -20), 5)
    shape.mass = 1
    shape.friction = 0.7
    space.add(body, shape)
    return body


def main():
    txts = {}
    mouse_joint = None
    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

