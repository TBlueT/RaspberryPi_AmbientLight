import numpy as np
class DisplayModel:
    def __init__(self):
        self.__FPS:int = 0
        self.__img:list = []

        self.__displySize = [0,0]


    @property
    def FPS(self):
        return self.__FPS

    @FPS.setter
    def FPS(self, value:int):
        self.__FPS = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        w, h, _ = np.shape(value)
        self.displySize = [w, h]
        self.__img = value

    @property
    def displySize(self):
        return self.__displySize

    @displySize.setter
    def displySize(self, value):
        self.__displySize = value