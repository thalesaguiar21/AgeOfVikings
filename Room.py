from Item import *

class Room(object):

	''' Classe que define uma sala dentro do jogo '''

	def __init__(self, name, description1):
		self.name = name
		self.description1 = description1
		self.description2 = ''
		self.visited = False
		self.exits = {}
		self.items = {}

	def setDescription2(self, description2):
		self.description2 = description2

	def setVisited(self):
		self.visited = True

	def addItem(self, item):
		self.items[item.getName()] = item

	def rmItem(self, name):
		del self.items[name]

	def listItems(self):
		itemList = ''
		for item in self.items:
			itemList += ' | ' + str(item)
		return 'Itens: ' + itemList + ' |'

	def hasItems(self):
		if(len(self.items.keys()) == 0):
			return False
		return True

	def getItem(self, name):
		return self.items[name]

	def getItems(self):
		return self.items.keys()

	def getDescription(self):
		if(not self.visited):
			return self.description1
		return self.description2

	def getName(self):
		return self.name

	def getFullDescription(self):
		return 'Você está nos(as)/no(a) ' + self.name + ', ' + self.getDescription()

	def setExits(self, exit, room):
		self.exits[exit] = room

	def hasExit(self):
		if(len(self.exits.keys()) > 0):
			return True
		return False

	def getExits(self):
		return self.exits.keys()

	def getExitsDict(self):
		return self.exits

	def getExitString(self):
		exitString = ''
		for exit in self.exits:
			exitString += ' | ' + exit
		return 'Saídas: ' + exitString + ' |'

	def goExit(self, exit):
		return self.exits[exit]

