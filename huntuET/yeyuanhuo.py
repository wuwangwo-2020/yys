#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15/02/2020 21:14
# @Author  : Achilles
# @Site    : 
# @File    : yeyuanhuo.py
# @Software: PyCharm

from tools.fight import Fight
from tools.positions import YeyuanhuoPositions
from tools.positions import CommonPositions

import time
import random


class YeYuanHuo(Fight):
    def __init__(self, hwnd, logger):
        Fight.__init__(self, hwnd, logger)

    def start(self):
        victoryImgPath = "./img/victory.jpg"
        fuImgPath = "./img/fu.jpg"
        while True:
            # 检测开始
            maxVal1, maxLoc1 = self.basicControl.compareScreens("./img/yeAttack.jpg")
            if maxVal1 > 0.9:
                self.logger.info("检测到挑战按钮")
                self.forSakeOfWrongPosition(*YeyuanhuoPositions.yeYuanHuoArea)
                time.sleep(random.randint(2, 3))
                self.logger.info("选择业原火")
                self.forSakeOfWrongPosition(*YeyuanhuoPositions.chiArea)
                self.logger.info("选择痴")
                self.forSakeOfWrongPosition(*YeyuanhuoPositions.yeAttack)
                self.logger.info("开始挑战")
                self.logger.info("等待")
                time.sleep(random.randint(50, 60))
            # 检测结束
            maxVal3, maxLoc3 = self.basicControl.compareScreens(victoryImgPath)
            maxVal4, maxLoc4 = self.basicControl.compareScreens(fuImgPath)
            if maxVal3 > 0.9 or maxVal4 > 0.9:  # 战斗结算
                self.logger.info("战斗结束")
                self.forSakeOfWrongPosition(*CommonPositions.victoryClick)
                self.forSakeOfWrongPosition(*CommonPositions.victoryClick)
