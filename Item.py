
class Item(object):
	
	''' Classe que define um item no jogo '''

	def __init__(self, name, description, collectable = True):
		self.collectable = collectable
		self.name = name
		self.description = description

	def isCollectable(self):
		return self.collectable

	def getName(self):
		return self.name

	def getDescription(self):
		return self.description

	def getFullDescription(self):
		return self.name + ', ' + self.description