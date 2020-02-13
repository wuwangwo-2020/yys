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

    def start(self):
        # TODO 检测司机特有的挑战按钮
        huntuAttackImgPath = "./img/huntuAttack.jpg"
        victoryImgPath = "./img/victory.jpg"
        while True:
            maxVal1, maxLoc1 = self.basicControl.compareScreens(huntuAttackImgPath)
            maxVal2, maxLoc2 = self.basicControl.compareScreens(victoryImgPath)
            maxVal3, maxLoc3 = self.basicControl.compareScreens("./img/fu.jpg")
            if maxVal1 > 0.9:
                self.forSakeOfWrongPosition(*HuntuPositions.huntuAttack)
                self.logger.info("战斗开始")
            if maxVal2 > 0.9 or maxVal3 > 0.9:
                self.logger.info("战斗结束")
                self.forSakeOfWrongPosition(*HuntuPositions.victoryClick)
                self.forSakeOfWrongPosition(*HuntuPositions.victoryClick)
            else:
                t = random.randint(1, 2)
                self.logger.info("战斗未结束，等待" + str(t))
                time.sleep(t)
