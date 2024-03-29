class DisplayModel:
    def __init__(self):
        self.__FPS:int = 0
        self.__img:list = []


    @@property
    def FPS(self):
        return self.__FPS

    @FPS.setter
    def FPS(self, value:int):
        self.__FPS = value

    @@property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value