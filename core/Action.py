#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .ability_helpers import *


class Action(object):

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.name = None
        self.text = None
        self.action_type = None
        self.game = None
        self.is_ability = True
        # initialize according a initial_data dictionary
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, _(dictionary[key]))
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        s = f'{self.id} {self.name} {self.action_type}'
        return s

    def is_applicable(self):
        if self.action_type == "General":
            if not is_general_action_applicable(self.game):
                return False
        if self.id not in all_abilities_is_applicable:
            return False
        return all_abilities_is_applicable[self.id](self.game)

    def do_it(self):
        if self.id not in all_abilities_do_it:
            print('error in Action', self.id, all_abilities_do_it)
            exit()
        all_abilities_do_it[self.id](self.game)

    def set_game(self, g):
        self.game = g


all_abilities_is_applicable = {}
all_abilities_do_it = {}

all_abilities_is_applicable[4] = action_focus_is_applicable
all_abilities_is_applicable[5] = action_inspiration_is_applicable
all_abilities_is_applicable[6] = action_plan_is_applicable

all_abilities_do_it[4] = action_focus_do_it
all_abilities_do_it[5] = action_inspiration_do_it
all_abilities_do_it[6] = action_plan_do_it
