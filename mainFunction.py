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

import detect
import response
import basic


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
    basic.getGameScreen(logger)
    if detect.detectVictory(logger):
        response.responseOfDetectVictory(logger)
    if detect.detectFu(logger):
        response.responseOfDetectFu(logger)
    logger.info("victory not found")


def liaoTuPo() -> None:
    basic.getGameScreen(logger)
    if detect.detectRemainFightTimesIsZero(logger) \
            or detect.detectRemainFightTimesIsZeroWhenIsNearlyOver(logger):
        response.responseOfDetectRemainFightTimesIsZero(logger)
    if detect.detectLiaoTuPo(logger):
        logger.info("already in the liaoTupo")
        while detect.detectMoreThanFiveMedals(logger):
            response.responseOfDetectMoreThanFiveMedals(logger)
        response.responseOfDetectNotMoreThanFiveMedals(logger)
        time.sleep(random.randint(2, 3))
        while True:
            if detect.detectVictory(logger):
                response.responseOfDetectVictory(logger)
                break
            if detect.detectFu(logger):
                response.responseOfDetectFu(logger)
                break
            response.responseOfNotDetectOrFu(logger)
            if detect.detectLiaoTuPo(logger):
                break
    else:
        logger.info("not in the liaoTuPo or the liaoTuPo has accomplished")


def fightCh28():
    # enter into Ch28
    # drag down characters which are full levels

    pass


def commonFight() -> None:
    pass


def chooseMode(mode, time, logger) -> None:
    if mode == "onlyVictory":
        # only detect the victory picture and the points here are related to the picture itself
        chooseMode(mode, time, logger)
    if mode == "liaoTuPo":
        chooseMode(mode, time, logger)
    else:
        logger.error("there exists mistake in input")
        sys.exit(0)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    chooseMode("liaoTuPo", 500000)
    # chooseMode("onlyVictory", 50000)
    # getGameScreen()
    # getScreenMean(246, 487, 259, 504)
