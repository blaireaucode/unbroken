from signalslot import Signal
from box import Box


class Character(object):
    character_changed = Signal()

    alias = {'se': 'small_efforts',
             'me': 'medium_efforts',
             'le': 'large_efforts',
             'time': 'time',
             'c': 'cunning',
             'f': 'food',
             'w': 'wood',
             'm': 'metal',
             't': 'treasure',
             'k': 'skill'
             }

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.name = None
        self.class_type = None
        self.level = 1
        self.abilities = []
        self.image = None
        self.game = None
        self.orienteer_cards = 2
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
        # resources
        self.resources = Box()
        self.resources.small_efforts = 13
        self.resources.medium_efforts = 0
        self.resources.large_efforts = 0
        self.resources.cunning = 0
        self.resources.time = 7
        self.resources.food = 0
        self.resources.wood = 0
        self.resources.metal = 0
        self.resources.treasure = 0

    def init_abilities(self, all_actions):
        ab = []
        for a in self.abilities:
            aa = next((item for item in all_actions if item.id == a), None)
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

    def get_resource_update(self, s):
        words = s.split()
        rtype = []
        rn = []
        if len(words) > 1:
            for w in words:
                t, n = self.get_resource_update(w)
                rtype = rtype + t
                rn = rn + n
            return rtype, rn
        f = None
        if s[0] == '-':
            f = -1
        if s[0] == '+':
            f = 1
        if s[0] == '0':  # do nothing
            return rtype, rn
        n = int(s[1:2])
        r = s[2:]
        r = self.alias[r]
        v = f * n
        rtype.append(r)
        rn.append(v)
        return rtype, rn

    def is_enough_resource(self, spend):
        rtype, rn = self.get_resource_update(spend)
        for t, n in zip(rtype, rn):
            # (n is negative because spend)
            if not self.resources[t] >= -n:
                return False
        return True

    def update_resource(self, s):
        rt, rn = self.get_resource_update(s)
        for t, n in zip(rt, rn):
            self.resources[t] += n
        self.character_changed.emit()
