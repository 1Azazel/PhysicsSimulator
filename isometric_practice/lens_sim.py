import pygame  # importing modules
import numpy as np
import sys

from lens import Lens

WIDTH = 800
HEIGHT = 800

BACKGROUND_COLOR = (217, 217, 217)

i = np.matrix[[1], [0]]
j = np.matrix[[0], [1]]

i_vector_2 = pygame.Vector2(1, 0)
j_vector_2 = pygame.Vector2(0, 1)


class LightBeam:
    def __init__(self, start_pos, start_angle, velocity):


BEAM_LIST = []
def draw_beams():
    for beam in BEAM_LIST:




def main():
    pygame.init()  # initiating pygame
    screen = pygame.display.set_mode((800, 800))  # creating the display surface
    clock = pygame.time.Clock()  # creating the game clock

    while True:  # Game Loop
        for event in pygame.event.get():  # checking for user input
            if event.type == pygame.QUIT:  # input to close the game
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)  # background color
        pygame.display.update()  # rendering the frame
        clock.tick(120)  # limiting the frames per second to 120


if __name__ == "__main__":
    main()
