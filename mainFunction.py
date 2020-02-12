#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 08/02/2020 21:36
# @Author  : Achilles
# @Site    : 
# @File    : mainFunction.py.py
# @Software: PyCharm
# one thing need to be mentioned is that the game may block simulated mouse operations,
# so the script must obtain the administration authority to run smoothly

import random
import sys
import time
import logging
import win32gui

from tools import basic, detect, response
from tupo.liaoTuPo import LiaoTuPo
from tools.basic import Basic
from tools.positions import TuPoPositions
from tools.positions import Common


def Auto(m, T) -> None:
    i, j = 0, 0
    start = time.time()
    while True:
        i = i + 1
        spend = time.time() - start
        logger.info("loop " + str(i) + " times, the program runs for "
                    + " " + str(spend) + " seconds")
        if spend > T:
            sys.exit(0)
        time.sleep(random.randint(0, 1))
        if m == "onlyVictory":
            clickVictory()
        if m == "liaoTuPo":
            liaoTuPo()
        if m == "fightCh28":
            fightCh28()


def clickVictory() -> None:
    basic.Basic.getGameScreen(logger)
    if detect.detectVictory(logger):
        response.responseOfDetectVictory(logger, handle)
    if detect.detectFu(logger):
        response.responseOfDetectFu(logger, handle)
    logger.info("victory not found")


def liaoTuPo() -> None:
    basic.getGameScreen(logger)
    if detect.detectRemainFightTimesIsZero(logger) \
            or detect.detectRemainFightTimesIsZeroWhenIsNearlyOver(logger):
        response.responseOfDetectRemainFightTimesIsZero(logger, handle)
    if detect.detectLiaoTuPo(logger):
        logger.info("already in the liaoTupo")
        while detect.detectMoreThanFiveMedals(logger):
            response.responseOfDetectMoreThanFiveMedals(logger, handle)
        response.responseOfDetectNotMoreThanFiveMedals(logger, handle)
        time.sleep(random.randint(2, 3))
        while True:
            if detect.detectVictory(logger):
                response.responseOfDetectVictory(logger, handle)
                break
            if detect.detectFu(logger):
                response.responseOfDetectFu(logger, handle)
                break
            response.responseOfNotDetectOrFu(logger, handle)
            if detect.detectLiaoTuPo(logger):
                break
    else:
        logger.info("不在寮突破界面")


def fightCh28():
    # enter into Ch28
    # drag down characters which are full levels

    pass


def commonFight() -> None:
    pass


def chooseMode(mode, time) -> None:
    if mode == "onlyVictory":
        # 仅仅只检测胜利图标
        Auto(mode, time)
    if mode == "liaoTuPo":
        Auto(mode, time)
    else:
        logger.error("输入存在错误")
        sys.exit(0)


if __name__ == '__main__':
    hwnd = win32gui.FindWindow(0, "阴阳师-网易游戏")
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    liaoTuPo = LiaoTuPo(hwnd, logger)
    liaoTuPo.start()
    # 如果一个窗口长期不操作，可能休眠，导致获取handle失败
    # imgSrcName = "./img/attack.jpg"
    # basicControl = Basic(hwnd, logger)
    # basicControl.compareScreens(imgSrcName)
    # basicControl.interceptImg("remainZero.jpg", *TuPoPositions.remainZero)
