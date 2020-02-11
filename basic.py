#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/02/2020 22:08
# @Author  : Achilles
# @Site    : 
# @File    : basic.py
# @Software: PyCharm

import pyautogui
import cv2
import random


def getGameScreen(logger) -> None:
    img = pyautogui.screenshot(region=[114, 64, 1251 - 114, 704 - 64])
    img.save("yys.jpg")
    logger.info("succeed storing yys.jpg")


def getScreenMean(x1, y1, x2, y2, logger) -> (float, float, float):
    img = cv2.imread("yys.jpg")  # BGR
    img = img[y1:y2, x1:x2]
    cv2.imwrite("sample.jpg", img)
    logger.info("succeed storing sample.jpg")
    bMean = img[:, :, 0].mean()
    gMean = img[:, :, 1].mean()
    rMean = img[:, :, 2].mean()
    # BGR mean
    logger.info("succeed getting mean value of the BGR, B:" + str(bMean) + " G:"
                + str(gMean) + " R:" + str(rMean))
    return bMean, gMean, rMean


def mouseClick(x1, y1, x2, y2, logger) -> None:  # click the mouse
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    t = random.random()
    pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    logger.info("click:(" + str(x) + ", " + str(y) + "), spend " + str(t) + " seconds")


def mouseDrag(x1, y1, x2, y2, length) -> None:
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    t = random.random()
    pyautogui.moveTo(x, y, duration=t, tween=pyautogui.easeInOutQuad)
    pyautogui.drag(0, -length, duration=t + random.random())
