from .Database import *
from .Phase import *
import jsonpickle
from signalslot import Signal
import random

jsonpickle.set_encoder_options('json', indent=2)


class Game(object):
    db = None
    phase_changed = Signal()

    def __init__(self):
        self.character = None
        self.phase = Phase()
        self.sub_phase = SubPhase()
        self.encounter = []
        self.monster = None
        self.actions = []
        self.all_actions = []
        self.all_encounters = []
        if not Game.db:
            print('reading database')
            Game.db = Database()
            Game.db.read_all_data()
        # init all actions (make a copy to keep the game consistent)
        self.all_actions = Game.db.all_actions.copy()
        for a in self.all_actions:
            a.set_game(self)
        # init all encounters (make a copy to keep the game consistent)
        self.all_encounters = Game.db.all_encounters.copy()
        for a in self.all_encounters:
            a.set_game(self)
        # shuffle
        random.shuffle(self.all_encounters)

    def save(self, filename):
        print('save to', filename)
        data = jsonpickle.encode(self)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, filename):
        print('load from ', filename)
        with open(filename, 'r') as f:
            data = json.load(f)
            g = jsonpickle.decode(data)
            return g

    def set_character(self, c):
        self.character = c
        self.character.set_game(self)

    def combat(self):
        self.phase.to_combat()
        self.sub_phase.to_trickery()
        self.phase_changed.emit()

    def explore(self):
        self.sub_phase.to_exploration()
        self.encounter = []
        # choose 2 cards or more if orienteer was used
        n = self.character.orienteer_cards
        for i in range(n):
            e = self.all_encounters.pop(0)
            self.encounter.append(e)
        self.phase_changed.emit()

    def choose_encounter_card(self, index):
        # put all other cards at the end of the desk
        i = 0
        for e in self.encounter:
            if i != index:
                self.all_encounters.append(e)
            i += 1
        # keep only one encounter card
        e = self.encounter[index]
        self.encounter = []
        self.encounter.append(e)
        # announce
        self.phase_changed.emit()

    def after_encounter(self):
        # init nb of cards to reveal
        self.character.orienteer_cards = 2
        # remove encounter, put end of the deck
        e = self.encounter.pop(0)
        self.all_encounters.append(e)
        # check time
        if self.character.resources.time <= 0:
            self.sub_phase.to_ambush()
            self.phase.to_combat()
        else:
            self.sub_phase.to_preparation()
        self.phase_changed.emit()
