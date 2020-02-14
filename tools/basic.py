#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/02/2020 22:08
# @Author  : Achilles
# @Site    : 
# @File    : basic.py
# @Software: PyCharm

import cv2
import random
import win32gui
import win32con
import win32api
import win32ui
import time
import numpy as np
import pyautogui

from tools.positions import TuPoPositions


class Basic:
    def __init__(self, hwnd, logger):
        self.hwnd = hwnd
        self.logger = logger
        self.debug_enable = False
        l1, t1, r1, b1 = win32gui.GetWindowRect(self.hwnd)
        l2, t2, r2, b2 = win32gui.GetClientRect(self.hwnd)
        self._client_h = b2 - t2
        self._client_w = r2 - l2
        self._border_l = ((r1 - l1) - (r2 - l2)) // 2
        self._border_t = ((b1 - t1) - (b2 - t2)) - self._border_l

    def getGameScreen(self, gray=0, fileName=None) -> np.ndarray:
        try:
            hwindc = win32gui.GetWindowDC(self.hwnd)
            srcdc = win32ui.CreateDCFromHandle(hwindc)
            memdc = srcdc.CreateCompatibleDC()
            bmp = win32ui.CreateBitmap()
            bmp.CreateCompatibleBitmap(srcdc, self._client_w, self._client_h)
            memdc.SelectObject(bmp)
            memdc.BitBlt((0, 0), (self._client_w, self._client_h), srcdc,
                         (self._border_l, self._border_t), win32con.SRCCOPY)
            if fileName is not None:
                bmp.SaveBitmapFile(memdc, fileName)
                srcdc.DeleteDC()
                memdc.DeleteDC()
                win32gui.ReleaseDC(self.hwnd, hwindc)
                win32gui.DeleteObject(bmp.GetHandle())
                return
            else:
                signedIntsArray = bmp.GetBitmapBits(True)
                img = np.fromstring(signedIntsArray, dtype='uint8')
                img.shape = (self._client_h, self._client_w, 4)
                srcdc.DeleteDC()
                memdc.DeleteDC()
                win32gui.ReleaseDC(self.hwnd, hwindc)
                win32gui.DeleteObject(bmp.GetHandle())
                if gray == 0:
                    return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                else:
                    return cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        except:
            pass

    def readImg(self, imgSrcName) -> np.ndarray:
        self.logger.info("成功读取图片" + imgSrcName)
        return cv2.imread(imgSrcName)

    def compareScreens(self, imgSrcName) -> (float, float):
        img = self.getGameScreen(gray=0)  # 全屏图片
        cv2.imwrite("./img/sample.jpg", img)  # 为了减小IO压力，在这里存储图片，win32位图过大
        self.logger.info("成功保存sample.jpg")
        imgSrc = self.readImg(imgSrcName)
        res = cv2.matchTemplate(imgSrc, img, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
        self.logger.info(str(maxVal) + "," + str(maxLoc))
        return maxVal, maxLoc

    def interceptImg(self, dest, pos1, pos2):
        imgName = "./img/sample.jpg"
        img = self.readImg(imgName)
        imgCompare = img[pos1[1]:pos2[1], pos1[0]:pos2[0]]
        cv2.imwrite("./img/" + dest, imgCompare)
        self.logger.info("成功截取图片并保存:" + dest)

    def getScreenMean(self, x1, y1, x2, y2) -> (float, float, float):
        img = cv2.imread("yys.jpg")  # BGR
        img = img[y1:y2, x1:x2]
        cv2.imwrite("sample.jpg", img)
        self.logger.info("succeed storing sample.jpg")
        bMean = img[:, :, 0].mean()
        gMean = img[:, :, 1].mean()
        rMean = img[:, :, 2].mean()
        # BGR mean
        self.logger.info("succeed getting mean value of the BGR, B:"
                         + str(bMean) + " G:" + str(gMean) + " R:" + str(rMean))
        return bMean, gMean, rMean

    def mouseClick(self, pos1, pos2) -> None:  # click the mouse
        x = random.randint(pos1[0], pos2[0])
        y = random.randint(pos1[1], pos2[1])
        t = random.random()
        # 这里的都是相对坐标
        # pyautogui.moveTo(x, y, duration=t)
        # pyautogui.click(x, y)
        win32gui.SendMessage(
            self.hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x, y))
        win32gui.SendMessage(
            self.hwnd, win32con.WM_LBUTTONDOWN, 0, win32api.MAKELONG(x, y))
        time.sleep(random.randint(20, 80) / 1000)
        win32gui.SendMessage(
            self.hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(x, y))
        self.logger.info("点击了:(" + str(x) + ", " + str(y) + "), spend " + str(t) + " seconds")

    def mouseDrag(self, pos1, pos2, length) -> None:
        pass
        # x = random.randint(x1, x2)
        # y = random.randint(y1, y2)
        # t = random.random()
        # pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)
        # pyautogui.drag(0, -length, duration=t + random.random())
