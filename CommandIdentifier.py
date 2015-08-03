from Command import *
from CommandList import *

class CommandIdentifier(object):
	''' Identifica e trata o comando digitado pelo usuário '''

	def __init__(self):
		self.words = []
		self.lineInput = ''
		self.command = None
		self.commandList = CommandList()

	def idCommand(self):
		self.lineInput = input(str("O que você faz? "))
		self.words = self.lineInput.lower().lstrip().split(' ', 1)
		if(self.commandList.isValid(self.words[0])):
			if (len(self.words) == 2):
				self.command = Command(self.words[0], self.words[1])
				return self.command
			elif(len(self.words) == 1):
				self.command = Command(self.words[0], None)
				return self.command
		else:
			return None

	def getCommands(self):
		return self.commandList.getCommands()

	def getCommandsString(self):
		commandString = ''
		for command in self.commandList:
			commandString += ' ' + command
		return 'Comandos: ' + commandString
