from Item import *

class Weapon(Item):
    def __init__(self, name, description, collectable = True, effect = None, weight = 0.0, dmg = 0.0):
        Item.__init__(self, name, description, collectable, effect, weight)
        self.dmg = dmg

    def getDmg(self):
        return self.dmg

    def setDmg(self, dmg):
        self.dmg = dmg

    
