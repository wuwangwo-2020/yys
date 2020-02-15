#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13/02/2020 11:45
# @Author  : Achilles
# @Site    : 
# @File    : huntuET.py
# @Software: PyCharm

import time
import random

from tools.fight import Fight
from tools.positions import HuntuPositions


class HuntuET(Fight):
    def __init__(self, hwnd, logger):
        Fight.__init__(self, hwnd, logger)
        self.times = 0  # 标记次数

    def start(self):
        huntuAttackImgPath = "./img/huntuAttack.jpg"
        victoryImgPath = "./img/victory.jpg"
        fuImgPath = "./img/fu.jpg"
        teShuImgPath = "./img/teShuJiZhi.jpg"
        while True:
            maxVal1, maxLoc1 = self.basicControl.compareScreens(huntuAttackImgPath)
            if self.driver == 1 and maxVal1 > 0.9:  # 司机开始按键
                self.forSakeOfWrongPosition(*HuntuPositions.huntuAttack)
                self.logger.info("战斗开始")
            maxVal20, maxLoc20 = self.basicControl.compareScreens(teShuImgPath)
            if self.mark == 1 and self.times == 0 and maxVal20 > 0.9:  # 手动标记大舅妈,进入魂土战斗
                self.logger.info("开始标记")
                self.basicControl.mouseClick(*HuntuPositions.jin)
                self.times += 1
            maxVal3, maxLoc3 = self.basicControl.compareScreens(victoryImgPath)
            maxVal4, maxLoc4 = self.basicControl.compareScreens(fuImgPath)
            if maxVal3 > 0.9 or maxVal4 > 0.9:  # 战斗结算
                self.logger.info("战斗结束")
                self.forSakeOfWrongPosition(*HuntuPositions.victoryClick)
                self.forSakeOfWrongPosition(*HuntuPositions.victoryClick)
                self.times = 0
