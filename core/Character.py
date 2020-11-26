#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
#import gettext

#_ = gettext.gettext


class Character:

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.name = None
        self.surname = None
        self.level = 1
        self.abilities = []
        self.image = None
        # initialize according a initial_data dictionary
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, _(dictionary[key]))
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        s = f'{self.id} {self.name} {self.surname}'
        return s


def read_character_database():
    f = open('character.json')
    data = json.load(f)
    print(len(data))
    i = 0
    characters = []
    for d in data:
        c = Character(d)
        c.id = i
        characters.append(c)
        # FIXME abilities
        i = i + 1
    return characters
