#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Character:

    def __init__(self, *initial_data, **kwargs):
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

    def init_abilities(self, all_abilities):
        ab = []
        for a in self.abilities:
            aa = next((item for item in all_abilities if item.id == a), None)
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
