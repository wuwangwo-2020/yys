#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/02/2020 16:27
# @Author  : Achilles
# @Site    : 
# @File    : fight.py
# @Software: PyCharm

import configparser
import time
import random

from tools.basic import Basic


class Fight:
    def __init__(self, hwnd, logger):
        self.hwnd = hwnd
        self.logger = logger
        self.basicControl = Basic(hwnd, logger)

    def forSakeOfWrongPosition(self, pos1, pos2):
        time.sleep(random.randint(0, 1))
        self.basicControl.mouseClick(pos1, pos2)
        time.sleep(random.randint(0, 1))
        self.basicControl.mouseClick(pos1, pos2)
        time.sleep(random.randint(0, 1))
        self.basicControl.mouseClick(pos1, pos2)

    def start(self):
        pass
