import pygame
import csv


def read_coord_from_csv(file_name):
    coord_list = []
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            x = int(row[0].strip("("))
            y = int(row[1].strip(")"))
            coord = (x, y)
            coord_list.append(coord)
    return coord_list


def draw_coastline(screen, color, coastal_points, width=1):
    if width == 1:
        pygame.draw.lines(screen, color, False, coastal_points, width=1)
    else:
        pygame.draw.lines(screen, color, False, coastal_points, width=width)
