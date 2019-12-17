# -*- coding: utf-8 -*-
"""
@Time    : Tue Dec 17 09:33:15 2019
@Author  : Jing-Ling, Wei
@Software: Spyder (Python 3.7)
"""

import cv2
import numpy as np

class Cv2Read():
    def __init__(self, IMG_PATH):
        self.IMG_PATH = IMG_PATH
        self.IMG_BGR = 0
        self.IMG_GRAY = 0
        self.IMG_CHANNEL = 0
        self.IMG_COMB = 0
        
        self.read_image()
        self.concat_image()

    def read_image(self):
        # 以彩色圖片的方式載入
        self.IMG_BGR = cv2.imread(self.IMG_PATH, cv2.IMREAD_COLOR)
        print(self.IMG_BGR)
        
        # 以灰階圖片的方式載入
        self.IMG_GRAY = cv2.imread(self.IMG_PATH, cv2.IMREAD_GRAYSCALE)
        print(self.IMG_GRAY)
        
        # 全Channel載入
        self.IMG_CHANNEL = cv2.imread(self.IMG_PATH, cv2.IMREAD_UNCHANGED)
        print(self.IMG_GRAY)
                
        # 為了要不斷顯示圖片，所以使用一個迴圈
        '''while True:
            # 顯示彩圖
            cv2.imshow('BGR', self.IMG_BGR)
            # 顯示灰圖
            cv2.imshow('GRAY', self.IMG_GRAY)
            
            # 直到按下 ESC 鍵才會自動關閉視窗結束程式
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()
                break'''

    def concat_image(self):
        rows_bgr, cols_bgr, channels_bgr = self.IMG_BGR.shape
        rows_gray, cols_gray = self.IMG_GRAY.shape
        
        rows_comb = max(rows_bgr, rows_gray)
        cols_comb = cols_bgr + cols_gray
        self.IMG_COMB = np.zeros(shape=(rows_comb, cols_comb, channels_bgr), dtype=np.uint8)
        
        self.IMG_COMB[:rows_bgr, :cols_bgr] = self.IMG_BGR
        self.IMG_COMB[:rows_gray, cols_bgr:] = self.IMG_GRAY[:, :, None]
        
        # 為了要不斷顯示圖片，所以使用一個迴圈
        while True:
            # 顯示彩圖
            cv2.imshow('BGR GRAY CONCAT', self.IMG_COMB)
        
            # 直到按下 ESC 鍵才會自動關閉視窗結束程式
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destroyAllWindows()
                break
    
if __name__ == '__main__':
    IMG_PATH ='lena.png'
    
    Cv2Read(IMG_PATH)