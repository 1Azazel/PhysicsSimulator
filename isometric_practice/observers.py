import numpy as np


class Observer:

    XY = False
    XYZ = False

    def __init__(self, pos):
        self.pos = self.set_pos(pos)

    def get_pos(self):
        return self.pos

    def set_pos(self, new_pos):
        if type(new_pos) is list:
            if len(new_pos) is 2:
                self.XY = True
                self.XYZ = False
            elif len(new_pos) is 3:
                self.XY = False
                self.XYZ = True
        elif type(new_pos) is np.matrix:


        if new_pos.type is np.matrix:
            new_pos_list = []
            for i, j in new_pos:
                new_pos_list.append((i, j))
            self.pos = new_pos_list
            self.pos_matrix = new_pos
        else:
            self.pos = new_pos
            self.pos_matrix = np.matrix(new_pos)
        return self.pos, self.pos_matrix









