import random

class Person():
    def __init__(self, name, hp=100, mp=100, atk = 70, magiclist = [], *args):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Physical Attack", "Magic", "Defend"]
        self.magic = magiclist

    def generate_attack_damage(self):
        dmg = random.randint(self.atk_low,self.atk_high) # btw randrange would have a step parameter
        return dmg

    def statout(self):
        print("{} state:".format(self.name))
        print("{}/{} hp and {}/{} mp".format(self.hp, self.maxhp, self.mp, self.maxmp))
        return True

    def choose_action(self):
        print("{} has choice of actions:".format(self.name))
        ind = 1
        for act in self.action:
            print("{}: {}".format(ind, act))
            ind += 1
        return True

    def choose_magic(self):
        print("{} has choice of spells:".format(self.name))
        ind = 1
        for mag in self.magic:
            print("{}: {} which needs {} mp".format(ind, mag.spell, mag.cost))
            ind += 1
        return True

    def take_damage(self, dmg):
        #if self.act != alist[1]:
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

	# @classmethod
	# def addmagic(cls, *args):
