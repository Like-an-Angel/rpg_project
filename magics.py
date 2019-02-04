import random

class Magic():
    def __init__(self, name, mp_cost, dmg, type, aoe = False):
        self.spell = name
        self.cost = mp_cost
        self.dmg = dmg
        self.type = type
        self.aoe = aoe

    def generate_magic_dmg(self):
        dmg = random.randint(self.dmg - 15, self.dmg + 15)
        return dmg
