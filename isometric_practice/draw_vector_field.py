import pygame  # importing modules
import numpy
import sys
import sympy

SIZE = 800
WIDTH = SIZE
HEIGHT = SIZE

SPACING = SIZE / 10

pygame.init()  # initiating pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creating the display surface
clock = pygame.time.Clock()  # creating the game clock

while True:  # Game Loop
    for event in pygame.event.get():  # checking for user input
        if event.type == pygame.QUIT:  # input to close the game
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

    screen.fill((217, 217, 217))  # background color
    pygame.display.update()  # rendering the frame
    clock.tick(120)  # limiting the frames per second to 120


