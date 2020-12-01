#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Database import *
from .Phase import *
import jsonpickle

jsonpickle.set_encoder_options('json', indent=2)


class Game(object):
    db = None

    def __init__(self):
        self.character = None
        self.phase = Phase(self)
        self.encounter = None
        self.actions = []
        self.all_actions = []
        if not Game.db:
            print('reading database')
            Game.db = Database()
            Game.db.read_all_data()
        self.all_actions = Game.db.all_actions.copy()
        for a in self.all_actions:
            a.set_game(self)

    def save(self, filename):
        print('save to', filename)
        data = jsonpickle.encode(self)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, filename):
        print('load from ', filename)
        with open(filename, 'r') as f:
            data = json.load(f)
            g = jsonpickle.decode(data)
            return g

    def set_character(self, c):
        self.character = c
        self.character.set_game(self)
