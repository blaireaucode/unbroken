from .Action import *
from .Character import *
import json


class Database(object):
    all_actions = []
    characters = []

    def __init__(self):
        pass

    def read_all_data(self):
        self.all_actions = read_actions_database()
        self.characters = read_character_database(self.all_actions)


def read_actions_database():
    f = open('qrc/actions.json')
    data = json.load(f)
    actions = []
    for d in data:
        c = Action(d)
        actions.append(c)
    return actions


def read_character_database(actions):
    f = open('qrc/characters.json')
    data = json.load(f)
    i = 0
    characters = []
    for d in data:
        c = Character(d)
        c.id = i
        c.init_actions(actions)
        characters.append(c)
        # FIXME actions
        i = i + 1
    return characters
