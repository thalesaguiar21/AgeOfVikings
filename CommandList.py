class CommandList(object):

	''' Classe que possui todos os comandos possíveis do jogo '''

	def __init__(self):
		self.commandList = ['ir', 'voltar', 'olhar', 'pegar', 'ajuda', 'atacar', 'defender', 'sair']

	def getCommandList(self):
		return self.commandList

	def isValid(self, command):
		return (command in self.commandList)
