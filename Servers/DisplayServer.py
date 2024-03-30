import cv2, threading, timeit
class DiasplayServer(threading.Thread):
    def __init__(self, parent=None):
        threading.Thread.__init__(self)
        self.daemon = True

        self.runStop: bool = False

        self.main = parent

        self.prev_time = 0
        self.FPS_set = 30

        self.HC100 = cv2.VideoCapture(0)

    def printf(self, stamp, value):
        try:
            self.main.ConsoleS.shy(F"{stamp} DiasplayS {value}")
        except:
            pass

    def stock_img(self):
        if self.HC100.isOpened():
            ret, img = self.HC100.read()
            if ret:
                return img
                # cv2.imshow("HC100", img)
                # if cv2.waitKey(1) != -1:
                #     break
            else:
                self.printf("!!", "HC100 No Get Img")
        else:
            self.printf("!!", "Not Open HC100")
        return (0,)

    def stock_fps(self, value:int):
        self.main.DisplayM.FPS = value

    def run(self):
        while not self.runStop:
            start_t = timeit.default_timer()

            current_time = start_t - self.prev_time
            if current_time > 1. / self.FPS_set:
                self.stock_img()
                fps = int(1. / (self.prev_time - start_t))
                self.stock_fps(fps)

if __name__ == "__main__":
    D = DiasplayServer()
    D.run()