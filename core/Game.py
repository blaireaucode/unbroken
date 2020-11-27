#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Database import *


class Game:

    def __init__(self):
        self.db = Database()
        self.character = None
        self.db.read_all_data()
