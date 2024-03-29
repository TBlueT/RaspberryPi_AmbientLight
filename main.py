from .Models import *
from .Servers import *

class main:
    def __init__(self):
        self.DisplayM = DisplayModel()
        self.LandAreaM = LandAreaModel()

        self.ConsoleS = ConsoleServer()

        self.DisplayS = DiasplayServer(self)



if __name__ == "__main__":
    pass