# Example file showing a circle moving on screen
import pygame
import numpy as np
import math as m

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
T = 8000  # Period is in milliseconds
RADIUS = 100

dt = 1/60


# so one full circuit should be completed every 2 seconds
# T = Period
# Frequency: 2pi / T
# t = time(current)
# theta = t * (2pi / T)
# f(x, y) = (r * cos(theta), r * sin(theta)
# player_pos = f(x, y)
# player_pos = pygame.Vector2(r * cos(t * (2pi / T)), r * sin(t * (2pi / T))

def shift_from_origin_to_center_of_screen(coord):
    new_x = (WIDTH / 2) + coord[0]
    new_y = (HEIGHT / 2) + coord[1]
    return pygame.Vector2(new_x, new_y)


def draw_ellipse_at_time_t(t):
    r = RADIUS
    theta = (2 * np.pi * t) / T
    left_top = (-r + (WIDTH / 2), (r * (m.sin(theta) ** 2)) + (HEIGHT / 2))
    width_height = (r, (r * m.sin(theta)))
    rect = pygame.Rect(left_top, width_height)
    print(left_top)
    print(width_height)
    pygame.draw.rect(screen, "black", rect, width=1)
    pygame.draw.ellipse(screen, "black", rect, width=1)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    time_now = pygame.time.get_ticks()
    draw_ellipse_at_time_t(time_now)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

    # limits FPS to 60
    # independent physics.

pygame.quit()
