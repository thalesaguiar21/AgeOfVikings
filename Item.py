
class Item(object):
	
	''' Classe que define um item no jogo '''

	def __init__(self, name, description, collectable = True):
		self.collectable = collectable
		self.name = name
		self.description = description
		self.items = []

	def isCollectable(self):
		return self.collectable

	def addItems(self, item):
		self.items.append(item)

	def rmItems(self, itemName):
		rmIndex = self.items.index(itemName)
		self.items.remove(rmIndex)

	def getName(self):
		return self.name

	def getDescription(self):
		return self.description

	def getFullDescription(self):
		return self.name + ', ' + self.description