import math as m


def distance_formula(coord_1, coord_2):

    x1 = coord_1[0]
    x2 = coord_2[0]
    y1 = coord_1[1]
    y2 = coord_2[1]

    x_dif_sqr = (x2 - x1) ** 2
    y_dif_sqr = (y2 - y1) ** 2
    d = m.sqrt(x_dif_sqr + y_dif_sqr)

    return d
