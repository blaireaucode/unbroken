def is_general_action_applicable(g):
    if not g.phase.is_travel and not g.phase.is_combat:
        return False
    return True


# focus #4
def action_focus_is_applicable(g):
    return g.character.resources.small_efforts >= 4


# focus #4
def action_focus_do_it(g):
    g.character.update_resource('-4se')
    g.character.update_resource('+1me')


# inspiration #5
def action_inspiration_is_applicable(g):
    return g.character.resources.medium_efforts >= 2


# inspiration #5
def action_inspiration_do_it(g):
    g.character.update_resource('-2me')
    g.character.update_resource('+1le')


# plan # 6
def action_plan_is_applicable(g):
    return g.character.resources.small_efforts >= 4


# plan #6
def action_plan_do_it(g):
    g.character.update_resource('-4se')
    g.character.update_resource('+1c')


# Orienteer # 8
def action_orienteer_is_applicable(g):
    return g.phase.is_travel \
           and g.sub_phase.is_preparation_step \
           and g.character.resources.small_efforts >= 1


# Orienteer #8
def action_orienteer_do_it(g):
    g.character.update_resource('-1se')
    g.character.orienteer_cards += 2
    g.character.character_changed.emit()


# decision # 10
def action_decision_is_applicable(g):
    return g.phase.is_travel and g.sub_phase.is_preparation_step


# decision #10
def action_decision_do_it(g):
    g.sub_phase.to_decision()
    g.phase_changed.emit()
