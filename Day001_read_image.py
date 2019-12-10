# -*- coding: utf-8 -*-
"""
@Time    : Mon Dec  9 16:47:24 2019
@Author  : Jing-Ling, Wei
@Software: Spyder (Python 3.7)
"""  
import cv2

class Cv2Read():
    def __init__(self, IMG_PATH):
        self.IMG_PATH = IMG_PATH
        
        self.read_image()

    def read_image(self):
        # 以彩色圖片的方式載入
        IMG_COLOR = cv2.imread(self.IMG_PATH, cv2.IMREAD_COLOR)
        print(IMG_COLOR)
        
        # 以灰階圖片的方式載入
        IMG_GRAY = cv2.imread(self.IMG_PATH, cv2.IMREAD_GRAYSCALE)
        
        # 為了要不斷顯示圖片，所以使用一個迴圈
        while True:
            # 顯示彩圖
            cv2.imshow('bgr', IMG_COLOR)
            # 顯示灰圖
            cv2.imshow('gray', IMG_GRAY)
        
            # 直到按下 ESC 鍵才會自動關閉視窗結束程式
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()
                break
    
if __name__ == '__main__':
    IMG_PATH ='lena.png'
    
    Cv2Read(IMG_PATH)