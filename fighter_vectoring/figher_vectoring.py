import pygame  # importing modules
import csv
import sys

WIDTH = 703
HEIGHT = 800

BOMBER_SPEED = 5
FIGHTER_SPEED = 9

POLYGON_FILE = "great_britain_trace.csv"

SCREEN_COLOR = "#FFEBD2"
COAST_COLOR = "#273248"
BOMBER_COLOR = "#AF4F41"
FIGHTER_COLOR = "#FFA364"
AIRSTRIP_COLOR = "#FC7643"

COAST_WIDTH = 3

HALF_WIDTH = 1/2 * WIDTH
HALF_HEIGHT = 1/2 * HEIGHT
ORIGIN = (HALF_WIDTH, HALF_HEIGHT)

COAST_LEFT = (0, HALF_HEIGHT)
COAST_MIDDLE = (HALF_WIDTH, HALF_HEIGHT)
COAST_TOP = (HALF_WIDTH, 0)


def coord_as_fractions_of_screen(x_ratio, y_ratio):
    x = x_ratio * WIDTH
    y = y_ratio * HEIGHT
    coord = (x, y)
    return coord


BAY_1 = coord_as_fractions_of_screen(0, (12/16))
BAY_2 = coord_as_fractions_of_screen((2/16), (13/16))
BAY_3 = coord_as_fractions_of_screen((3/16), (10/16))
BAY_4 = coord_as_fractions_of_screen((5/16), (11/16))

DOVER_1 = coord_as_fractions_of_screen((7/16), (12/16))
DOVER_2 = coord_as_fractions_of_screen((10/16), (13/16))
DOVER_3 = coord_as_fractions_of_screen((13/16), (12/16))
DOVER_4 = coord_as_fractions_of_screen((12/16), (10/16))

SPIT_1 = coord_as_fractions_of_screen((10/16), (8/16))
SPIT_2 = coord_as_fractions_of_screen((10/16), (7/16))
SPIT_3 = coord_as_fractions_of_screen((9/16), (6/16))
SPIT_4 = coord_as_fractions_of_screen((8/16), (5/16))

HEAD_1 = coord_as_fractions_of_screen((9/16), (4/16))
HEAD_2 = coord_as_fractions_of_screen((10/16), (3/16))
HEAD_3 = coord_as_fractions_of_screen((12/16), (1/16))
HEAD_4 = coord_as_fractions_of_screen((12/16), 0)

COAST_VERTICES = [BAY_1, BAY_2, BAY_3, BAY_4,
                  DOVER_1, DOVER_2, DOVER_3, DOVER_4,
                  SPIT_1, SPIT_2, SPIT_3, SPIT_4,
                  HEAD_1, HEAD_2, HEAD_3, HEAD_4]


def read_coord_from_csv(file_name):
    coord_list = []
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            x = int(row[0].strip("("))
            y = int(row[1].strip(")"))
            coord = (x, y)
            print(coord)
            coord_list.append(coord)
    return coord_list


pygame.init()  # initiating pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creating the display surface
clock = pygame.time.Clock()  # creating the game clock
# map_surface = pygame.image.load("resized_battle_of_britain_map.png")
# screen.blit(map_surface, (0, 0))


class Aircraft:
    def __init__(self, speed, fuel_per_unit_time):
        self.speed = speed
        self.fuel_per_unit_time = fuel_per_unit_time


class RadarStation:
    def __init__(self, coord):
        self.coordinates = coord


class Airstrip:
    def __init__(self, coord):
        self.coordinates = coord
        self.fighters = []


def draw_coastline(coastal_points):
    pygame.draw.lines(screen, COAST_COLOR, False, coastal_points, width=COAST_WIDTH)


def plot_bomber_route(bomber):
    pass


coastline_coordinate_list = []


while True:  # Game Loop
    for event in pygame.event.get():  # checking for user input
        if event.type == pygame.QUIT:  # input to close the game
            for point in coastline_coordinate_list:
                # print(point)
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
            # coastline_coordinate_list.append(event.pos)
    screen.fill(SCREEN_COLOR)  # background color
    draw_coastline(read_coord_from_csv(POLYGON_FILE))
    # if len(coastline_coordinate_list) >= 2:
        # draw_coastline(coastline_coordinate_list)
    pygame.display.update()  # rendering the frame
    clock.tick(120)  # limiting the frames per second to 120

