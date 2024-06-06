import numpy as np
import math as m


class Sphere:

    def __init__(self, radius, center=(0, 0, 0)):
        self.r = radius
        self.h = center[0]
        self.j = center[1]
        self.k = center[2]

    def get_r(self):
        return self.r

    def get_h(self):
        return self.h

    def get_j(self):
        return self.j

    def get_k(self):
        return self.k

    def get_center(self):
        center = (self.get_h(), self.get_j(), self.get_k())
        return center

    def pos_on_xy_cross_section_as_func_of_theta(self, theta):
        x = (self.get_r() * m.cos(theta)) + self.get_h()
        y = (self.get_r() * m.sin(theta)) + self.get_j()
        z = 0
        return np.array([[x], [y], [z]])

    def pos_on_xz_cross_section_as_func_of_theta(self, theta):
        x = (self.get_r() * m.cos(theta)) + self.get_h()
        y = 0
        z = (self.get_r() * m.sin(theta)) + self.get_k()
        return np.array([[x], [y], [z]])

    def pos_on_yz_cross_section_as_func_of_theta(self, theta):
        x = 0
        y = (self.get_r() * m.sin(theta)) + self.get_j()
        z = (self.get_r() * m.cos(theta)) + self.get_k()
        return np.array([[x], [y], [z]])



