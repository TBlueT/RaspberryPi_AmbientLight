import board
import neopixel
import time
'''
WS2812B LED 데이터시트 https://pdf1.alldatasheet.co.kr/datasheet-pdf/view/1134589/WORLDSEMI/WS2818A.html

X : 0 신호 함수 작성
X : 1 신호 함수 작성
X : RGB 24bit 생성 함수 작성
X : LED 갯수별 RGB 24bit 세트 생성 함수 생성
X : RGB data 쓰기 함수 작성

음...

라이브러리 최고!
'''

class WS2812B_AreaServer:
    def __init__(self):
        self.runStop: bool = False
        self.pixels = neopixel.NeoPixel(board.D18, 30)
    def write(self):
        self.pixels[0] = (255, 0, 0)
        self.pixels.show()


if __name__ == "__main__":
    pass