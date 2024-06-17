import numpy as np
import PIL.ImageColor

R_WAVELENGTH = 610  # nm
G_WAVELENGTH = 532  # nm
B_WAVELENGTH = 467  # nm


class Pixel:

    INTEGER_VALUES = False
    PERCENT_VALUES = False

    def __init__(self, color_values):
        self.r = color_values[0]
        self.g = color_values[1]
        self.b = color_values[2]
        self.a = color_values[3]




