#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from PySide2.QtCore import Signal, QObject
from signalslot import Signal


class Character(object):
    character_changed = Signal()

    def __init__(self, *initial_data, **kwargs):
        # QObject.__init__(self)
        self.id = None
        self.name = None
        self.class_type = None
        self.level = 1
        self.abilities = []
        self.image = None
        self.game = None
        # initialize according a initial_data dictionary
        for dictionary in initial_data:
            for key in dictionary:
                s = dictionary[key]
                if isinstance(s, str):
                    setattr(self, key, _(dictionary[key]))
                else:
                    setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
        # resources
        self.small_efforts = 13
        self.medium_efforts = 0
        self.large_efforts = 0
        self.cunning = 0

    def init_actions(self, all_actions):
        ab = []
        for a in self.abilities:
            aa = next((item for item in all_actions if item.id == a), None)
            if aa:
                ab.append(aa)
        self.abilities = ab

    def __str__(self):
        s = f'{self.id} {self.name} {self.class_type}'
        return s

    def set_game(self, g):
        self.game = g
        for a in self.abilities:
            a.set_game(g)

    def update_resource(self, s):
        words = s.split()
        print(words)
        if len(words) > 1:
            for w in words:
                self.update_resource(w)
            return
        f = None
        if s[0] == '-':
            f = -1
        if s[0] == '0':
            f = 1
        if not f:
            print('error update resource', s)
            return
        n = int(s[1:2])
        r = s[2:]
        print(n, r)
        v = f * n
        if r == 'se':
            self.small_efforts += v
        if r == 'me':
            self.medium_efforts += v
        if r == 'se':
            self.large_efforts += v
        self.character_changed.emit()

    def add_small_efforts(self, v):
        self.small_efforts += v
        self.character_changed.emit()

    def add_medium_efforts(self, v):
        self.medium_efforts += v
        self.character_changed.emit()

    def add_large_efforts(self, v):
        self.large_efforts += v
        self.character_changed.emit()

    def add_cunning(self, v):
        self.cunning += v
        self.character_changed.emit()
