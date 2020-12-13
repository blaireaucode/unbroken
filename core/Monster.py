from signalslot import Signal
from box import Box


class Monster(object):
    monster_changed = Signal()

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.monster_type = None
        self.name = None
        self.armor = 0
        self.health = 0
        self.level = 1
        self.trickery = None
        self.ambush = None

        # self.abilities = []
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

    def __str__(self):
        s = f'{self.id} {self.monster_type} {self.name} ({self.level}) ar:{self.armor} heath:{self.health}'
        return s

    def set_game(self, g):
        self.game = g
        # for a in self.abilities:
        #    a.set_game(g)

    def trick(self):
        self.game.character.update_resource(self.trickery)
        self.game.sub_phase.trick_to_hunger()
        self.game.phase_changed.emit()
