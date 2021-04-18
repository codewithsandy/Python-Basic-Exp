from abc import ABCMeta, abstractmethod

class shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):


    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 5
        self.breadth = 6
    # def printarea(self):
    #     return self.length * self.breadth

rect1 = rectangle()

obj = shape()