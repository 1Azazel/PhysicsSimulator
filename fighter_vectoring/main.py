import time
import pygame
import csv
import sys

from drawing_from_csv_functions import draw_coastline, read_coord_from_csv

WIDTH = 703
HEIGHT = 800
TICK = 120
PLAYER_SPEED = 300

LANDMASS_FILES = ["great_britain_trace.csv", "ireland_trace.csv", "normandy_trace.csv"]
MAP_ELEMENTS = ["fighter_bases.csv"]

THINGS_TO_DRAW = [LANDMASS_FILES, MAP_ELEMENTS,]

SCREEN_COLOR = "#FFEBD2"
COAST_COLOR = "#273248"
BOMBER_COLOR = "#AF4F41"
FIGHTER_COLOR = "#FFA364"
BASE_COLOR = "#FC7643"

COAST_WIDTH = 3


def init():
    pygame.init()  # initiating pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creating the display surface
    clock = pygame.time.Clock()  # creating the game clock
    origin = (WIDTH/2, HEIGHT/2)
    dt = clock.tick(TICK) / 1000
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_surface = pygame.image.load("jet_32p_final.png")
    return screen, clock, origin, dt, player_pos, player_surface


def give_map(map_str, map_bool):
    if map_bool is True:
        return map_str
    else:
        return -1

PLAYER_START = (0, 0)

def move(player_pos, dt, move_bool):
    if move_bool is True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            player_pos.y += PLAYER_SPEED * dt
        if keys[pygame.K_a]:
            player_pos.x -= PLAYER_SPEED * dt
        if keys[pygame.K_d]:
            player_pos.x += PLAYER_SPEED * dt

ELEMENT_LIST = []

class Element:
    def __init__(self, element_type, location):
        self.element_type = element_type
        self.element_location = location

    def get_location(self):
        return self.element_location


def place_element(element_type, event, element_bool):
    if element_bool is True:
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_element = Element(element_type, event.pos)
            ELEMENT_LIST.append(new_element)

ELEMENT_SIZE_DICT = {
    "base" : 7
}


def draw_element_as_circle(coord_list, element_color, element_size, screen, width=None):
    if width is None:
        for coord in coord_list:
            pygame.draw.circle(screen, element_color, coord, element_size)
    else:
        for coord in coord_list:
            pygame.draw.circle(screen, element_color, coord, element_size, width=width)


def draw_bases(coord_list, screen):
    draw_element_as_circle(coord_list, BASE_COLOR, 7, screen, width=2)
    draw_element_as_circle(coord_list, SCREEN_COLOR, 5, screen)




SAVE_PATH = ""


def save(save_item, save_name, format_str, save_bool):
    if save_bool is True:
        save_name = save_name + format_str
        if format_str == ".txt":
            with open(save_name, "w", newline="") as outfile:
                for item in save_item:
                    outfile.write(item)
        elif format_str == ".csv":
            with open(save_name, "w", newline="") as outfile:
                writer = csv.writer(outfile)
                for item in save_item:
                    writer.writerow(item)

        print(save_name + " was created")


def end(event, trace_bool, element_bool):
    if event.type == pygame.QUIT:  # input to close the game
        if trace_bool is True:
            save(TRACE_LIST, "new trace", ".csv", True)
        if element_bool is True:
            element_coord_list = []
            for element in ELEMENT_LIST:
                element_coord_list.append(element.get_location())
            save(element_coord_list, "new element group", ".csv", True)
        pygame.quit()
        sys.exit()


TRACE_LIST = []


def trace(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        TRACE_LIST.append(event.pos)


def main():

    element_type = "base"

    screen, clock, origin, dt, player_pos, player_surface = init()

    DISPLAY = False
    TRACE = False
    MAP = False
    PLAYER_MOVE = False
    SAVE = False
    ELEMENTS = False

    print("t : trace",
          "m : map",
          "f : free move",
          "p : place element")

    mode = input("select mode: ")
    if mode.lower() == "t":
        DISPLAY = True
        TRACE = True
        SAVE = True
    elif mode.lower() == "m":
        MAP = True
    elif mode.lower() == "f":
        MAP = True
        PLAYER_MOVE = True
    elif mode.lower() == "p":
        DISPLAY = True
        ELEMENTS = True
        SAVE = True

# Setup Phase
    if MAP is True:
        pass

    if ELEMENTS is True:
        element_type = input("enter element type: ")

    if SAVE is True:
        pass

    if PLAYER_MOVE is True:
        player_surface = pygame.image.load("jet_32p_final.png")
        screen.blit(player_surface, PLAYER_START)

    if DISPLAY is True:
        map_surface = pygame.image.load("resized_battle_of_britain_map.png")
        screen.blit(map_surface, (0, 0))

    while True:  # Game Loop

        for event in pygame.event.get():  # checking for user input
            end(event, TRACE, ELEMENTS)
            if TRACE is True:
                trace(event)
            if ELEMENTS is True:
                place_element(element_type, event, ELEMENTS)

        if MAP is True:
            screen.fill(SCREEN_COLOR)  # background color
            for item in LANDMASS_FILES:
                item = give_map(item, MAP)
                if item == -1:
                    pass
                else:
                    draw_coastline(screen, COAST_COLOR, read_coord_from_csv(item), width=COAST_WIDTH)
            for item in MAP_ELEMENTS:
                if item == "fighter_bases.csv":
                    draw_bases(read_coord_from_csv(item), screen)

        if TRACE is True:
            if len(TRACE_LIST) >= 2:
                draw_coastline(screen, COAST_COLOR, TRACE_LIST, width=COAST_WIDTH)

        if ELEMENTS is True:
            draw_bases(ELEMENT_LIST, screen)

        if PLAYER_MOVE is True:
            move(player_pos, dt, PLAYER_MOVE)
            screen.blit(player_surface, player_pos)

        pygame.display.update()  # rendering the frame
        clock.tick(TICK)  # limiting the frames per second to 120
        dt = clock.tick(TICK) / 1000


if __name__ == "__main__":
    main()
