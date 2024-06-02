import pygame  # importing modules
import sys

pygame.init()  # initiating pygame
screen = pygame.display.set_mode((800, 800))  # creating the display surface
clock = pygame.time.Clock()  # creating the game clock

while True:  # Game Loop
    for event in pygame.event.get():  # checking for user input
        if event.type == pygame.QUIT:  # input to close the game
            pygame.quit()
            sys.exit()

    screen.fill((217, 217, 217))  # background color
    pygame.display.update()  # rendering the frame
    clock.tick(120)  # limiting the frames per second to 120

