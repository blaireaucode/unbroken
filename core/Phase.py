#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from statemachine import StateMachine, State


class Phase(StateMachine):
    # states
    before = State('before', initial=True)
    travel = State('travel')
    combat = State('combat')
    terminated = State('terminated')
    # transitions
    start = before.to(travel)
    to_combat = travel.to(combat)
    end_combat = combat.to(travel)
    end_game = combat.to(terminated)

    def on_start(self):
        print('start', self.model)


class SubPhase(StateMachine):
    # states
    preparation_step = State('preparation_step', initial=True)
    decision_step = State('decision_step')
    exploration_step = State('exploration_step')
    ambush_step = State('ambush_step')
    trickery_step = State('trickery_step')
    battle_step = State('battle_step')
    # transitions
    to_decision = preparation_step.to(decision_step)
    to_exploration = decision_step.to(exploration_step)
    to_battle = decision_step.to(battle_step)
    to_ambush = exploration_step.to(ambush_step)
    to_preparation = exploration_step.to(preparation_step)
    to_trickery = decision_step.to(trickery_step)
