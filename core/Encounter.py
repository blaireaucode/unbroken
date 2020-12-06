class Encounter(object):

    def __init__(self, *initial_data, **kwargs):
        self.id = None
        self.name = None
        self.text = None
        self.spend = None
        self.gain = None
        self.time = 0
        # initialize according a initial_data dictionary
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, _(dictionary[key]))
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        s = f'{self.id} {self.name} {self.spend}|{self.gain} ; {self.text}'
        return s

    def set_game(self, game):
        self.game = game

    def resolve(self):
        s = f'{self.spend} {self.gain} -{self.time}time'
        print(s)
        self.game.character.update_resource(s)

    def rest(self):
        e = self.game.encounter[0]
        s = f'+{e.time}se -{self.time}time'
        print(s)
        self.game.character.update_resource(s)
