#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/02/2020 16:20
# @Author  : Achilles
# @Site    : 
# @File    : liaoTuPo.py
# @Software: PyCharm

from tools.fight import Fight
from tools.basic import Basic
from tools.positions import TuPoPositions
from tools.positions import Common

import time
import random


class LiaoTuPo(Fight):
    def __init__(self, hwnd, logger):
        Fight.__init__(self, hwnd, logger)
        self.basicControl = Basic(hwnd, logger)

    def start(self):
        self.logger.info("进入寮突破模式")
        imgSrcName = "./img/tuPoJiLu.jpg"
        maxVal1, maxLoc1 = self.basicControl.compareScreens(imgSrcName)
        time.sleep(random.randint(1, 2))
        while maxVal1 > 0.9:
            self.logger.info("处于寮突破界面")
            time.sleep(random.randint(1, 2))
            self.basicControl.mouseClick(*TuPoPositions.liaoArea)
            maxVal2, maxLoc2 = self.basicControl.compareScreens("./img/remainZero.jpg")
            if maxVal2 > 0.9:
                t = random.randint(300, 400)
                self.logger.info("等待寮突破次数恢复" + str(t))
                time.sleep(t)
            self.basicControl.mouseClick(*TuPoPositions.firstFight)
            time.sleep(random.randint(0, 1))
            self.basicControl.mouseClick(*TuPoPositions.attack)
            time.sleep(random.randint(1, 2))
            self.basicControl.mouseClick(*TuPoPositions.attack)  # 再次点击，防止漏点
            while True:
                maxVal4, maxLoc4 = self.basicControl.compareScreens("./img/fu.jpg")
                if maxVal4 > 0.9:
                    self.logger.info("找到福")
                    for j in range(3):
                        self.basicControl.mouseClick(*Common.Fu)
                        time.sleep(random.randint(1, 2))
                    break
                else:
                    self.logger.info("等待战斗结束")
                    time.sleep(random.randint(5, 10))
            maxVal1, maxLoc1 = self.basicControl.compareScreens(imgSrcName)
        else:
            self.logger.info("不处于寮突破界面,需要手动切换到寮突破界面")
