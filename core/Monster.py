from signalslot import Signal
from box import Box


class Monster(object):
    monster_changed = Signal()

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.name = None
        self.armor = 0
        self.health = 0
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

    def __str__(self):
        s = f'{self.id} {self.name} ({self.level}) ar:{self.armor} heath:{self.health}'
        return s

    def set_game(self, g):
        self.game = g
        for a in self.abilities:
            a.set_game(g)
