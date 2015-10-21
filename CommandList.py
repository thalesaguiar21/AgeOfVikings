class CommandList(object):

	''' Classe que possui todos os comandos possíveis do jogo '''

	def __init__(self):
		self.commandListSinonimous = {'ir' : ['ir', 'vou', 'irei'], \
									  'olhar' : ['olhar', 'ver', 'inspecionar', 'verificar', 'observar'], \
									  'ajuda' : ['ajuda', 'socorro'], \
									  'sair' : ['sair', 'desistir', 'abandonar', 'terminar'], \
									  'voltar' : ['voltar', 'retornar'], \
									  'pegar' : ['pegar', 'apanhar', 'coletar'], \
									  'atacar' : ['atacar', 'bater'], \
									  'defender' : ['defender', 'bloquear']}
		#self.commandList = ['ir', 'voltar', 'olhar', 'pegar', 'ajuda', 'atacar', 'defender', 'sair']

	def getCommandList(self):
		return self.commandListSinonimous.keys()

	def getOneWordCommands(self):
		oneWordCommands = []
		oneWordCommands.extend(self.commandListSinonimous.get('sair')[:])
		oneWordCommands.extend(self.commandListSinonimous.get('ajuda')[:])
		oneWordCommands.extend(self.commandListSinonimous.get('voltar')[:])
		return self.oneWordCommands

	def isValid(self, command):
		return (command in self.commandList)

	def isValid2(self, command):
		for key in self.commandListSinonimous.keys():
			if(command in self.commandListSinonimous[key]):
				return key
		return None

	def getCommand(self, command):
		return self.commandListSinonimous[command]
'''
Teste = CommandList()
print(Teste.isValid2("vou"))
print(Teste.isValid2("pirueta"))
'''