from CommandIdentifier import *
from Command import *
from CommandList import *

class Game(object):

	def __init__(self):
		self.commandId = CommandIdentifier()
		self.rooms = []
		self.createWorld()
		self.actualRoom = rooms[0]

	def createWorld(self):
		pass

	def printLogo(self):
		pass

	def printTutorial(self):
		pass

	def printWelcome(self):
		pass

	def selectCommand(self, command):
		pass

	def play():
		pass