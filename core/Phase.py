#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from statemachine import StateMachine, State


class Phase(StateMachine):

    # states
    before = State('before', initial=True)
    travel = State('travel')
    fight = State('fight')
    terminated = State('terminated')
    # transitions
    start = before.to(travel)
    start_fight = travel.to(fight)
    end_fight = fight.to(travel)
    end_game = fight.to(terminated)
    print('phase init')

    def on_start(self):
        print('start', self.model)