from Item import *

class Room(object):

	''' Classe que define uma sala dentro do jogo '''

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.exits = {}
		self.items = {}

	def addItem(self, name, item):
		self.items[name] = item

	def rmItem(self, name):
		del self.items[name]

	def listItems(self):
		itemList = ''
		for item in self.items:
			itemList += ' ' + str(item)
		return 'Itens: ' + itemList

	def hasItems(self):
		if(len(self.items.keys()) == 0):
			return False
		return True

	def getItem(self, name):
		return self.items[name]

	def getItems(self):
		return self.items.keys()

	def getDescription(self):
		return self.description

	def getName(self):
		return self.name

	def getFullDescription(self):
		return 'Você está nos(as)/no(a) ' + self.name + ', ' + self.description

	def setExits(self, exit, room):
		self.exits[exit] = room

	def hasExit(self):
		if(len(self.exits.keys()) > 0):
			return True
		return False

	def getExits(self):
		return self.exits.keys()

	def getExitString(self):
		exitString = ''
		for exit in self.exits:
			exitString += exit + ' '
		return 'Saídas: ' + exitString


	def goExit(self, exit):
		return self.exits[exit]

