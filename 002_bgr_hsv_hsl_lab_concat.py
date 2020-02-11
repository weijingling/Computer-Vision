# -*- coding: utf-8 -*-
"""
@Time    : Tue Dec 17 17:07:12 2019
@Author  : Jing-Ling, Wei
@Software: Spyder (Python 3.7)
"""

import cv2
import numpy as np

class Cv2Read():
    def __init__(self, IMG_PATH):
        self.IMG_PATH = IMG_PATH
        self.IMG_BGR = 0
        self.IMG_HSV = 0
        self.IMG_HSL = 0
        self.IMG_LAB = 0
        self.IMG_COMB = 0
        
        self.read_image_change_space()
        self.concat_image()

    def read_image_change_space(self):
        # 以彩色圖片的方式載入
        self.IMG_BGR = cv2.imread(self.IMG_PATH, cv2.IMREAD_COLOR)
        
        # BGR -> HSV
        self.IMG_HSV = cv2.cvtColor(self.IMG_BGR, cv2.COLOR_BGR2HSV)
        
        # BGR -> HSL
        self.IMG_HSL = cv2.cvtColor(self.IMG_BGR, cv2.COLOR_BGR2HLS)
        
        # BGR -> LAB
        self.IMG_LAB = cv2.cvtColor(self.IMG_BGR, cv2.COLOR_BGR2LAB)


    def concat_image(self):
        self.IMG_COMB = np.hstack((self.IMG_BGR, self.IMG_HSV, self.IMG_HSL, self.IMG_LAB))
        
        # 為了要不斷顯示圖片，所以使用一個迴圈
        while True:
            # 圖片顯示
            cv2.imshow('BGR-HSV-HSL-LAB CONCAT', self.IMG_COMB)
        
            # 直到按下 ESC 鍵才會自動關閉視窗結束程式
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()
                break
    
if __name__ == '__main__':
    IMG_PATH ='lena.png'
    
    Cv2Read(IMG_PATH)
