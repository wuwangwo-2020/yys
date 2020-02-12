#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/02/2020 21:45
# @Author  : Achilles
# @Site    : 
# @File    : response.py
# @Software: PyCharm

import time
import random

from tools import basic


def responseOfDetectVictory(logger, handle) -> None:
    logger.info("find victory")
    for j in range(3):
        time.sleep(random.randint(0, 1) + random.random())
        basic.mouseClick(237, 439, 446, 532, logger, handle)


def responseOfDetectFu(logger, handle) -> None:
    logger.info("find fu")
    for j in range(3):
        time.sleep(random.randint(0, 1) + random.random())
        basic.mouseClick(237, 439, 446, 532, logger, handle)


def responseOfNotDetectOrFu(logger, handle) -> None:
    basic.mouseClick(280, 149, 433, 311, logger, handle)
    logger.info("victory not found and fu not found")
    time.sleep(random.randint(1, 2) + random.random())
    basic.getGameScreen(logger)


def responseOfDetectMoreThanFiveMedals(logger, handle) -> None:
    basic.mouseClick(280, 149, 433, 311, logger, handle)
    logger.info("not find folks with no more than 5 medals")
    basic.mouseDrag(566, 228, 739, 253, 115, handle)
    logger.info("succeed dragging down")
    basic.getGameScreen(logger)


def responseOfDetectNotMoreThanFiveMedals(logger, handle) -> bool:
    logger.info("find folks with no more than 5 medals")
    basic.mouseClick(566, 228, 739, 253, logger, handle)
    time.sleep(random.randint(2, 4))
    logger.info("begin fight")
    basic.mouseClick(644, 354, 741, 396, logger, handle)
    basic.getGameScreen(logger)


def responseOfDetectRemainFightTimesIsZero(logger) -> None:
    logger.info("waiting the fighting times to recover")
    time.sleep(random.randint(300, 400))
    logger.info("waiting is over")


def responseOfDetectAskForTeam(logger) -> bool:
    pass
    # return simpleJudge()


def responseOfDetectAskForTeam(logger) -> None:
    # TODO
    # mouseClick()
    pass
