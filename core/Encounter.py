#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .ability_helpers import *


class Encounter(object):

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.name = None
        self.text = None
        self.spend = None
        self.gain = None
        self.time = 0
        # initialize according a initial_data dictionary
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, _(dictionary[key]))
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        s = f'{self.id} {self.name} {self.spend}|{self.gain} ; {self.text}'
        return s

    def set_game(self, game):
        self.game = game

    def resolve(self):
        c = self.game.character
        c.update_resource(self.spend)
        c.update_resource(self.gain)