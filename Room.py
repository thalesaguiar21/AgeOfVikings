from Item import *

class Room(object):

	''' Classe que define uma sala dentro do jogo '''

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.exits = {}
		self.items = {}

	def addItem(self, name, item):
		if(type(name) == type('') and type(item) == type(Item)):
			self.items[name] = item
		else:
			raise AttributeError

	def listItems(self):
		itemList = ''
		for item in self.items:
			itemList += ' ' + str(item)
		return itemList

	def hasItems(self):
		if(len(self.items.keys()) == 0):
			return False
		return True


	def getDescription(self):
		return self.description

	def getName(self):
		return self.name

	def getFullDescription(self):
		return 'Você está nos(as)/no(a) ' + self.name + ', ' + self.description

	def setExits(self, exit, room):
		self.exits[exit] = room

