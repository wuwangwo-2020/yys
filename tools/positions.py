#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/02/2020 14:14
# @Author  : Achilles
# @Site    : 
# @File    : positions.py
# @Software: PyCharm


class CommonPositions:
    victory = (367, 74), (484, 157)  # 战斗胜利结束后中间偏上出现的胜利战鼓
    fu = (495, 457), (611, 520)  # 战斗胜利结束后中间偏下出现的福


class TuPoPositions:
    tuPoJiLu = (36, 596), (119, 622)  # 寮突破左下角突破记录字体，判断是否处于寮突破界面
    firstFight = (442, 105), (640, 194)  # 寮突破中第一个对手的位置
    attack = (527, 288), (634, 330)  # 点击寮突破中第一个对手的位置后出现的挑战按钮
    liaoArea = (123, 90), (331, 231)  # 左上角的寮突破界面，点击这里以防止误点
    remainZero = (245, 485), (284, 505)  # 寮突破剩余次数为0


class HuntuPositions:
    victoryClick = (12, 305), (121, 526)  # 魂土战斗胜利结束后应该点击的坐标
    huntuAttack = (1060, 560), (1110, 596)
