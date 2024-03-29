from Models import *
from Servers import *

class main:
    def __init__(self):
        self.DisplayM = DisplayModel()
        self.LandAreaM = LandAreaModel()

        self.ConsoleS = ConsoleServer()

        self.DisplayS = DiasplayServer(self)
        self.LandAreaS = LandAreaServer(self)


        self.thrdStart()
    def thrdStart(self):
        self.DisplayS.start()


if __name__ == "__main__":
    import cv2, time
    import numpy as np

    m = main()

    while True:
        img = m.DisplayM.img

        if np.shape(img) != (0,):
            cv2.imshow("a", img)

            if cv2.waitKey(1) != -1:
                break

        time.sleep(0.01)