from .Ability import *
from .Character import *
import json

class Database:
    abilities = []
    characters = []

    def __init__(self):
        pass

    def read_all_data(self):
        self.abilities = read_abilities_database()
        self.characters = read_character_database(self.abilities)


def read_abilities_database():
    f = open('qrc/abilities.json')
    data = json.load(f)
    abilities = []
    for d in data:
        c = Ability(d)
        abilities.append(c)
    return abilities


def read_character_database(abilities):
    f = open('qrc/characters.json')
    data = json.load(f)
    i = 0
    characters = []
    for d in data:
        c = Character(d)
        c.id = i
        c.init_abilities(abilities)
        characters.append(c)
        # FIXME abilities
        i = i + 1
    return characters
