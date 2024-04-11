import time, cv2
import numpy as np
class LandAreaServer:
    def __init__(self, parent=None):
        self.main = parent


    def detachment(self, range_width:float, img:list):
        w, h = self.main.DisplayM.displySize
        img_1 = cv2.rotate(img[0:w, 0:range_width], cv2.ROTATE_90_CLOCKWISE)
        img_2 = cv2.rotate(img[w - range_width:w, 0:h], cv2.ROTATE_180)
        img_3 = cv2.rotate(img[0:w, h - range_width:h], cv2.ROTATE_90_COUNTERCLOCKWISE)
        img_4 = img[0:range_width, 0:h]

        return [img_1, img_2, img_3, img_4]

    def partition_color(self, range_area:int, img):
        w, h, _ = np.shape(img)
        color = [[0, 0, 0] for _ in range(range_area)]
        for i in range(1,range_area+1):
            r = np.sum(img[w / range_area * (i - 1):w / range_area * i, :, 0])/np.size(img[w / range_area * (i - 1):w / range_area * i, :, 0])
            g = np.sum(img[w / range_area * (i - 1):w / range_area * i, :, 1])/np.size(img[w / range_area * (i - 1):w / range_area * i, :, 1])
            b = np.sum(img[w / range_area * (i - 1):w / range_area * i, :, 2])/np.size(img[w / range_area * (i - 1):w / range_area * i, :, 2])
            color[i] = [r, g, b]
        return color

if __name__ == "__main__":
    pass