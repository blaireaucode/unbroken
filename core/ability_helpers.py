#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_general_action_applicable(g):
    if not g.phase.is_travel and not g.phase.is_fight:
        return False
    return True


# focus #4
def action_focus_is_applicable(g):
    return g.character.small_efforts >= 4


# focus #4
def action_focus_do_it(g):
    g.character.add_small_efforts(-4)
    g.character.add_medium_efforts(1)


# inspiration #5
def action_inspiration_is_applicable(g):
    return g.character.medium_efforts >= 2


# inspiration #5
def action_inspiration_do_it(g):
    g.character.add_medium_efforts(-2)
    g.character.add_large_efforts(1)


# plan # 6
def action_plan_is_applicable(g):
    return g.character.small_efforts >= 4


# plan #6
def action_plan_do_it(g):
    g.character.add_small_efforts(-4)
    g.character.add_cunning(1)


# decision # 10
def action_decision_is_applicable(g):
    return g.phase.is_travel and g.sub_phase.is_preparation_step


# decision #10
def action_decision_do_it(g):
    g.sub_phase.to_decision()
    g.phase_changed.emit()
