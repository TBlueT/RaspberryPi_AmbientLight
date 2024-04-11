from Models import *
from Servers import *

class main:
    def __init__(self):
        self.DisplayM = DisplayModel()
        self.LandAreaM = LandAreaModel()

        self.ConsoleS = ConsoleServer()

        self.DisplayS = DiasplayServer(self)
        self.LandAreaS = LandAreaServer(self)

        self.prev_time = 0
        self.FPS_set = 30

        self.average_height = 10
        self.led_count = 1

        self.thrdStart()
    def thrdStart(self):
        self.DisplayS.start()

    def run(self):
        while True:
            start_t = timeit.default_timer()

            current_time = start_t - self.prev_time
            if current_time > 1. / self.FPS_set:
                temp_img = self.DisplayS.stock_img()
                if temp_img != (0,):
                    self.DisplayM.img = temp_img
                    temp_detachment = self.LandAreaS.detachment(self.average_height, temp_img)
                    temp_partition_color_left = self.LandAreaS.partition_color(self.led_count, temp_detachment[0])
                    temp_partition_color_top = self.LandAreaS.partition_color(self.led_count, temp_detachment[1])
                    temp_partition_color_right = self.LandAreaS.partition_color(self.led_count, temp_detachment[2])
                    temp_partition_color_bown = self.LandAreaS.partition_color(self.led_count, temp_detachment[3])
                    print([temp_partition_color_left, temp_partition_color_top, temp_partition_color_right, temp_partition_color_bown])


                fps = int(1. / (self.prev_time - start_t))
                self.ConsoleS.shy(F">> img get FPS: {fps}")

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