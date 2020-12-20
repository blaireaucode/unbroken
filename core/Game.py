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
        self.encounters = []
        self.monster = None
        self.battle_round = 0
        self.actions = []
        self.all_actions = []
        self.all_encounters = []
        self.all_monsters = []
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
        # shuffle encounters
        random.shuffle(self.all_encounters)
        # init all monsters (make a copy to keep the game consistent)
        self.all_monsters = Game.db.all_monsters.copy()
        for a in self.all_monsters:
            a.set_game(self)
        # shuffle monsters
        random.shuffle(self.all_monsters)

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

    def start_combat(self, t):
        self.phase.to_combat()
        if t == 'trickery':
            self.sub_phase.to_trickery()
        if t == 'ambush':
            self.sub_phase.to_ambush()
        # find the monster FIXME use D6 and level
        m = self.all_monsters.pop(0)
        self.monster = m
        # reset time
        level = self.character.level
        if level == 1:
            self.character.resources.time = 12
        if level == 2:
            self.character.resources.time = 16
        if level == 3:
            self.character.resources.time = 19
        if level == 4:
            self.character.resources.time = None
        self.character.level += 1
        if self.character.level > 4:
            self.character.level = 4
        self.character.character_changed.emit()
        self.phase_changed.emit()

    def start_explore(self):
        self.sub_phase.to_exploration()
        self.encounters = []
        self.monster = None
        # choose 2 cards or more if orienteer was used
        n = self.character.orienteer_cards
        for i in range(n):
            e = self.all_encounters.pop(0)
            self.encounters.append(e)
        self.phase_changed.emit()

    def choose_encounter_card(self, index):
        # put all other cards at the end of the desk
        i = 0
        for e in self.encounters:
            if i != index:
                self.all_encounters.append(e)
            i += 1
        # keep only one encounter card
        e = self.encounters[index]
        self.encounters = []
        self.encounters.append(e)
        # announce
        self.phase_changed.emit()

    def after_encounter(self):
        # init nb of cards to reveal
        self.character.orienteer_cards = 2
        # remove encounter, put end of the deck
        e = self.encounters.pop(0)
        self.all_encounters.append(e)
        # check time
        if self.character.resources.time <= 0:
            self.start_combat('ambush')
        else:
            self.sub_phase.to_preparation()
            self.phase_changed.emit()

    def start_fight(self):
        print(self.sub_phase)
        self.sub_phase.to_battle()
        self.battle_round = 1
        self.phase_changed.emit()
