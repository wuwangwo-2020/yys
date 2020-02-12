#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/02/2020 16:27
# @Author  : Achilles
# @Site    : 
# @File    : fight.py
# @Software: PyCharm

import configparser


class Fight:
    def __init__(self, hwnd, logger):
        conf = configparser.ConfigParser()
        conf.read("settings.ini", encoding="utf-8")
        self.hwnd = hwnd
        self.logger = logger
        self.mode = conf.getint("SETTINGS", "mode")
        self.logger.info("成功读取配置！")

    def start(self):
        pass
