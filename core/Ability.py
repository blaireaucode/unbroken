#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Ability:

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.name = None
        self.text = None
        self.action_type = None
        self.game = None
        # initialize according a initial_data dictionary
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, _(dictionary[key]))
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        s = f'{self.id} {self.name} {self.action_type}'
        return s

    def do_it(self):
        print(f'do the action', self.name)

    def set_game(self, g):
        self.game = g
