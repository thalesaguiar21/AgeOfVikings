from CommandIdentifier import *
from Command import *
from CommandList import *
from Room import *

class Game(object):

	def __init__(self):
		self.commandId = CommandIdentifier()
		self.rooms = []
		self.actualRoom = ''
		self.lastRoom = []
		self.bag = []
		self.createWorld()

	def createWorld(self):
		#Criando as salas...
		salaMisteriosa = Room('sala misteriosa', 'Você abre os olhos devagar, sua visão ainda embaçada consegue identificar que você encontra-se em um salão tão brilhante quanto ouro. Ao seu lado você percebe uma silhueta de um homem vestido em uma armadura e segurando o que parece ser uma lança... Ele dirigi-se à você...')
		cabana = Room('cabana', 'Você acorda assustado e suando. Olha ao redor e encontra suas roupas penduradas na parede, sua cama e seu machado e escudo pendurados na parde de madeira, logo ao lado uma porta... Você então se dá conta de que está em sua cabana e que tudo não passou de um sonho.')
		cozinha = Room('cozinha', 'Entrando na cozinha, você já está familiarizado com sua velha dispensa, sua pequena mesa com o que restou da caça de ontem. Além disso, a parte mais importante, seu trófeu da primeira caçada ao lado de seu pai.')

		#Adicionando saídas as salas
		salaMisteriosa.setExits('correr', cabana)
		cabana.setExits('porta', cozinha)
		cozinha.setExits('porta', cabana)
		
		#Criando itens
		roupas = Item('roupas', 'Roupas de couro de animais das redondezas, protegem bastante contra o frio')
		cama = Item('cama', 'Cama de feno e pedaços de pele de animais. Muito usadas nesses tempos...')
		machado = Item('machado', 'Um machado comum')
		escudo = Item('escudo', 'Escudo de madeira feito pelo seu pai.')
		dispensa = Item('dispensa', 'um armário antigo com algumas frutas.', False)
		frutas = Item('frutas', 'algumas frutas que sobraram antes do início do inverno.')

		#Adicionando itens aos itens '-'
		dispensa.addItems(frutas)

		#Adicionando itens as salas
		cabana.addItem(roupas.getName(), roupas)
		cabana.addItem(cama.getName(), cama)
		cabana.addItem(machado.getName(), machado)
		cabana.addItem(escudo.getName(), escudo)

		cozinha.addItem(dispensa.getName(), dispensa)

		self.actualRoom = salaMisteriosa

	def printLogo(self):
				print("  _      __     _    _")
				print(" | |    / / _  | |  / / _   _   _   _____     _____")
				print(" | |   / / | | | | / / | | | \ | | |  _  |   /  ___|")
				print(" | |  / /  | | | |/ /  | | |  \| | | |_| |  /  /__")
				print(" | | / /   | | |   /   | | |     | |___  |  \___  \ ")
				print(" | |/ /    | | |   \   | | |     |     | |      \  \ ")
				print(" |   /     | | | |\ \  | | | |\  |  ___| |  ____/  /")
				print(" |__/      |_| |_| \_\ |_| |_| \_| |_____| |______/ ") 
				print("") 

	def printTutorial(self):
		print('1. Este é um jogo baseado em texto, digite os comandos disponíveis para jogar.')
		print('2. Alguns comandos precisam de um complemento e outros não.')
		print('3. Digite apenas um comando por vez.')

	def printWelcome(self):
		self.printLogo()
		self.printTutorial()
		
	def printRoomInfo(self):
		print(self.actualRoom.getFullDescription())
		print()
		if(self.actualRoom.hasExit()):
			print(self.actualRoom.getExitString())
		if(self.actualRoom.hasItems()):
			print(self.actualRoom.listItems())



	def selectCommand(self, command):
		if(command == None):
			print('Este não é um comando válido!')
			return True
		else:
			if(command.getFirstWord() == 'ir'):
				return self.executarIr(command)
			elif(command.getFirstWord() == 'pegar'):
				return self.executarPegar(command)
			elif(command.getFirstWord() == 'olhar'):
				return self.executarOlhar(command)
			elif(command.getFirstWord() == 'voltar'):
				return self.executarVoltar(command)
			elif(command.getFirstWord() == 'ajuda'):
				return self.executarAjuda(command)
			elif(command.getFirstWord() == 'atacar'):
				return self.executarAtacar(command)
			elif(command.getFirstWord() == 'defender'):
				return self.executarDefender(command)
			elif(command.getFirstWord() == 'sair'):
				return self.executarSair()

	def executarIr(self, command):
		if(command.hasSecondWord() and (command.getSecondWord() in self.actualRoom.getExits())):
			self.lastRoom.append(self.actualRoom)
			self.actualRoom = self.actualRoom.goExit(command.getSecondWord())
		else:
			secondWord = 'NAOTONALISTADESAIDAS'
			while(secondWord not in self.actualRoom.getExits()):
				secondWord = input(str('Ir para onde? '))
			command.setSecondWord(secondWord)
			self.actualRoom = self.actualRoom.goExit(command.getSecondWord())
		self.printRoomInfo()
		return True

	def executarPegar(self, command):
		if(command.hasSecondWord() and (command.getSecondWord() in self.actualRoom.getItems())):
			self.bag.append(self.actualRoom.getItem(command.getSecondWord()))
			self.actualRoom.rmItem(command.getSecondWord())
		print('Você pegou: %s' %command.getSecondWord())
		print('')
		return True

	def executarOlhar(self, command):
		if(not self.actualRoom.hasItems()):
			print('Não há itens nessa sala')
			return True
		if(command.hasSecondWord() and (command.getSecondWord() in self.actualRoom.getItems())):
			print(self.actualRoom.getItem(command.getSecondWord()).getDescription())
		else:
			secondWord = 'NAOTONALISTADEITEMS'
			while(secondWord not in self.actualRoom.getItems()):
				secondWord = input(str('Olhar o que? '))
			command.setSecondWord(secondWord)
			print(self.actualRoom.getItem(command.getSecondWord()).getDescription())
		print('')
		return True

	def executarVoltar(self, command):
		self.actualRoom = self.lastRoom.pop()
		self.printRoomInfo()
		return True

	def executarAjuda(self, command):
		self.printRoomInfo()
		return True

	def executarSair(self):
		print('Apenas os guerreiros mortos em batalha irão para os salões dourados! ')
		print('Pressione uma tecla para sair...')
		input()
		return False

	def executarAtacar(self, command):
		pass

	def executarDefender(self, command):
		pass

	def play(self):
		playing = True
		self.printWelcome()
		self.printRoomInfo()
		while(playing == True):
			print('')
			command = self.commandId.idCommand()
			print('')
			playing = self.selectCommand(command)

eraDosVikings = Game()
eraDosVikings.play()
