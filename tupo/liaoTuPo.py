#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/02/2020 16:20
# @Author  : Achilles
# @Site    : 
# @File    : liaoTuPo.py
# @Software: PyCharm

from tools.fight import Fight
from tools.positions import TuPoPositions
from tools.positions import CommonPositions

import time
import random
import win32gui


class LiaoTuPo(Fight):
    def __init__(self, hwnd, logger):
        Fight.__init__(self, hwnd, logger)

    def setForeground(self, val):
        if val == 0:
            win32gui.SetActiveWindow(self.hwnd)
            win32gui.SetForegroundWindow(self.hwnd)

    def start(self):
        imgSrcName = "./img/tuPoJiLu.jpg"
        while True:
            maxVal1, maxLoc1 = self.basicControl.compareScreens(imgSrcName)
            time.sleep(random.randint(1, 2))
            while maxVal1 > 0.9:
                self.logger.info("处于寮突破界面")
                self.forSakeOfWrongPosition(*TuPoPositions.liaoArea)
                maxVal2, maxLoc2 = self.basicControl.compareScreens("./img/remainZero.jpg")
                if maxVal2 > 0.9:
                    t = random.randint(300, 400)
                    self.logger.info("等待寮突破次数恢复" + str(t))
                    time.sleep(t)
                maxVal3, maxLoc3 = self.basicControl.compareScreens("./img/firstFightMedals.jpg")
                if maxVal3 > 0.9:
                    self.logger.info("未找到合适勋章对手")
                    break
                self.logger.info("开始战斗")
                self.basicControl.mouseClick(*TuPoPositions.firstFight)
                time.sleep(random.randint(0, 1))
                maxVal4, maxLoc4 = self.basicControl.compareScreens("./img/attack.jpg")
                if maxVal4 > 0.9:
                    self.forSakeOfWrongPosition(*TuPoPositions.attack)  # 再次点击挑战，防止漏点
                    self.logger.info("点击了挑战按钮")
                    while True:
                        maxVal5, maxLoc5 = self.basicControl.compareScreens("./img/fu.jpg")
                        if maxVal5 > 0.9:
                            self.logger.info("找到福")
                            for j in range(3):
                                self.basicControl.mouseClick(*CommonPositions.fu)
                                time.sleep(random.randint(1, 2))
                            break
                        else:
                            self.logger.info("等待战斗结束")
                            time.sleep(random.randint(5, 10))
                time.sleep(random.randint(10, 20))
            else:
                self.logger.info("不处于寮突破界面,需要手动切换到寮突破界面")
