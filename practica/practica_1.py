from math import *
class vector:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def len_vector(self):
        if (self.__dict__.get('x') is None) or (self.__dict__.get('y') is None):
            raise RuntimeError()
        return dist((0, 0), (self.x, self.y))

v = vector(3,4)
print(v.len_vector())
