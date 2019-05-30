
class Item(object):
    
    ''' Classe que define um item no jogo '''

    def __init__(self, name, description, collectable = True, effect = None, weight = 0.0):
        self.collectable = collectable
        self.name = name
        self.description = description
        self.weight = weight
        self.effect = effect

    def is_collectable(self):
        return self.collectable

    def get_name(self):
        return self.name

    def getdescription(self):
        return self.description

    def getWeight(self):
        return self.weight

    def getFullDescription(self):
        return self.name + ', ' + self.description

