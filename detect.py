#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/02/2020 21:40
# @Author  : Achilles
# @Site    : 
# @File    : detect.py
# @Software: PyCharm

from yys import basic


def simpleJudge(x1, y1, x2, y2, standardBMean, standardGMean, standardRMean, logger) -> bool:
    bMean, gMean, rMean = basic.getScreenMean(x1, y1, x2, y2, logger)
    return abs(standardBMean - bMean) < 1 and \
        abs(standardGMean - gMean) < 1 and \
        abs(standardRMean - rMean) < 1


def detectVictory(logger) -> bool:  # detect victory
    return simpleJudge(365, 120, 483, 220, 73.92, 89.23, 156.42, logger)


def detectFu(logger) -> bool:  # detect fu
    return simpleJudge(473, 452, 630, 539, 34.50, 43.77, 105.11, logger)


def detectLiaoTuPo(logger) -> bool:  # detect whether in LiaoTuPo
    return simpleJudge(36, 599, 119, 620, 73.60, 82.00, 91.92, logger)


def detectMoreThanFiveMedals(logger) -> bool:  # detect whether more than five medals
    return simpleJudge(454, 158, 640, 194, 136.98, 153.04, 167.54, logger)


def detectRemainFightTimesIsZero(logger) -> bool:  # detect whether remain fight times is zero
    return simpleJudge(246, 487, 259, 504, 136.98, 153.04, 167.54, logger)


def detectRemainFightTimesIsZeroWhenIsNearlyOver(logger) -> bool:
    return simpleJudge(246, 487, 259, 504, 63.64, 69.64, 74.64, logger)


def detectDefaultAskingForTeam(logger) -> bool:
    return simpleJudge(12, 196, 247, 258, 133.09, 158.92, 177.15,  logger)


def detectAskForTeam(logger) -> bool:
    pass
    # return simpleJudge()
