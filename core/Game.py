#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Database import *
import jsonpickle

jsonpickle.set_encoder_options('json', indent=2)


# jsonpickle.set_encoder_options('simplejson', compactly=True)


class Game:
    db = None

    def __init__(self):
        self.character = None
        if not Game.db:
            print('reading database')
            Game.db = Database()
            Game.db.read_all_data()

    def save(self, filename):
        print('save to', filename)
        data = jsonpickle.encode(self)
        print(data)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, filename):
        print('load from ', filename)
        with open(filename, 'r') as f:
            data = json.load(f)
            return jsonpickle.decode(data)
