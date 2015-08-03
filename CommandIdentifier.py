from Command import *
from commandList import *

class CommandIdentifier(object):
	''' Identifica e trata o comando digitado pelo usuário '''

	def __init__(self):
		self.words = []
		self.lineInput = ''
		self.command = None
		self.commandList = commandList()

	def idCommand(self, lineInput):
		self.lineInput = input(str("O que você faz? "))
		self.words = lineInput.lower().lstrip().split(' ', 1)
		if(commandList.isValid(self.words[0])):
			if (len(self.words) == 2):
				command = Command(self.words[0], self.words[1])
				return command
			elif(len(self.words) == 1):
				command = Command(self.words[0], None)
				return command
		else:
			print('Este não é um comando válido! Tente novamente')
			return None
