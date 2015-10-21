from CommandIdentifier import *
from Command import *
from CommandList import *
from Room import *
import os

class Game(object):

	''' Classe principal do jogo '''

	def __init__(self):
		self.commandId = CommandIdentifier()
		#self.rooms = 
		self.actualRoom = None
		self.lastRoom = None
		self.bag = []
		self.createWorld()

	def createWorld(self):
		#Criando as salas...
		salaMisteriosa = Room('sala misteriosa', 'Você abre os olhos devagar, sua visão ainda embaçada consegue identificar que'\
			+ ' você encontra-se em um salão tão brilhante quanto ouro. Ao seu lado você percebe uma silhueta de um homem vestido em uma'\
			+ ' armadura e segurando o que parece ser uma lança... Ele dirigi-se à você...')
		cabana = Room('cabana', 'Você acorda assustado e suando. Olha ao redor e encontra suas roupas penduradas na parede, sua cama'\
			+ ' e seu machado e escudo pendurados na parde de madeira, logo ao lado uma porta... Você então se dá conta de que'\
			+ ' está em sua cabana e que tudo não passou de um sonho.')
		cozinha = Room('cozinha', 'Entrando na cozinha, você já está familiarizado com sua velha dispensa, sua pequena mesa  e sobre ela o'\
			+ ' que restou da caça de ontem e uma pequena runa. Além disso, a parte mais importante, seu trófeu da primeira caçada ao lado'\
			+ ' de seu pai.')
		dispensa = Room('dispensa', 'um armário antigo com algumas frutas')
		cama = Room('cama', 'cama de feno e pedaços de pele de animais. Muito usada nesses tempos...')
		arredoresDeSiegheim1 = Room('arredores de Siegheim', 'Ao sair da sua cabana, você se encontra nas florestas que rodeiam as ruinas de'\
			+ ' Siegheim(nome da cidade principal dos dominios do rei ragnar)')
		#arredoresDeSiegheim2 = Room('arredores de Siegheim', 'andando pelo caminho, você lembra dos passeios com seu pai por essas mesmas florestas')


		#Adicionando as segundas descrições
		cabana.setDescription2('Seu quarto, nele você pode ver sua cama e algumas coisas comuns')

		#Adicionando saídas as salas
		salaMisteriosa.setExits('correr', cabana)

		cabana.setExits('porta', cozinha)

		cozinha.setExits('porta', cabana)
		cozinha.setExits('dispensa', dispensa)
		cozinha.setExits('fora da cabana', arredoresDeSiegheim1)

		dispensa.setExits('cozinha', cozinha)

		cama.setExits('cabana', cabana)

		arredoresDeSiegheim1.setExits('cabana', cozinha)
		#arredoresDeSiegheim1.setExits('frente', arredoresDeSiegheim2)

		
		#Criando itens
		bilhete = Item('bilhete', ' "Encontre-me nas ruinas do antigo rei,\nDe: Seu amigo\nPara: Sieg"')
		roupas = Item('roupas', 'Roupas de couro de animais das redondezas, protegem bastante contra o frio')
		cama = Item('cama', 'Cama de feno e pedaços de pele de animais. Muito usadas nesses tempos...')
		machado = Item('machado', 'Um machado comum')
		escudo = Item('escudo', 'Escudo de madeira feito pelo seu pai.')
		frutas = Item('frutas', 'algumas frutas que sobraram antes do início do inverno.')
		simboloDeCaçada = Item('Troféu', 'A cabeça de um javali morto na sua primeira caçada com seu pai. Olhar ela lhe traz lembranças de sua infância... De quando você ainda estava aprendendo a segurar seu escudo.')

		#Adicionando itens aos itens '-'
		

		#Adicionando itens as salas
		cabana.addItem(roupas)
		cabana.addItem(cama)
		cabana.addItem(machado)
		cabana.addItem(escudo)

		cozinha.addItem(simboloDeCaçada)
		cozinha.addItem(bilhete)

		dispensa.addItem(frutas)

		self.actualRoom = salaMisteriosa

	def printLogo(self):
		print("  _      __")
		print(" | |    / / _   _   __  _   _   _    _____     _____")
		print(" | |   / / | | | | / / | | | \ | |  |  _  |   /  ___|")
		print(" | |  / /  | | | |/ /  | | |  \| |  | |_| |  /  /__")
		print(" | | / /   | | |   /   | | |     |  |___  |  \___  \ ")
		print(" | |/ /    | | |   \   | | |     |      | |      \  \ ")
		print(" |   /     | | | |\ \  | | | |\  |  ____| |  ____/  /")
		print(" |__/      |_| |_| \_\ |_| |_| \_| |______| |______/ ") 
		print("") 

	def printTutorial(self):
		print('1. Este é um jogo baseado em texto, digite os comandos disponíveis para jogar.')
		print('2. Alguns comandos precisam de um complemento e outros não.')
		print('3. Digite apenas um comando por vez.')
		print('4. Caso esteja perdido digite \'ajuda\'')

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

		elif(not command.hasSecondWord() and command.getFirstWord() not in commandId.getOneWords()):
			secondWord = None
			while(secondWord == None):
				secondWord = input(command.getFirstWord().capitalize() + '... ?')
			command.setSecondWord(secondWord)
			return self.selectCommand(command)

		elif(command.getFirstWord() == 'ir'):
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
		if(command.getSecondWord() in self.actualRoom.getExits()):
			
			self.lastRoom = command.getSecondWord()
			self.actualRoom = self.actualRoom.goExit(command.getSecondWord())
			#self.printRoomInfo()
			#self.actualRoom.setVisited()
			os.system('CLS')
			#os.system('clear')
		else:
			print('Esta saída não existe!')
		return True

	def executarPegar(self, command):
		if(not self.actualRoom.hasItems()):
			print('Não há itens nessa sala!')
		elif(command.getSecondWord() in self.actualRoom.getItems()):
			self.bag.append(self.actualRoom.getItem(command.getSecondWord()))
			self.actualRoom.rmItem(command.getSecondWord())
			print('Você pegou: %s' %command.getSecondWord())
		else:
			print('Não exite esse item na sala!')
		return True

	def executarOlhar(self, command):
		if(not self.actualRoom.hasItems()):
			print('Não há itens nessa sala')
		elif(command.getSecondWord() in self.actualRoom.getItems()):
			print(self.actualRoom.getItem(command.getSecondWord()).getDescription())
		else:
			print('Não exite esse item na sala!')
		return True

	def executarVoltar(self, command):
		aux = self.actualRoom
		self.actualRoom = self.lastRoom
		self.lastRoom = aux
		#self.printRoomInfo()
		return True

	def executarAjuda(self, command):
		self.printRoomInfo()
		print(self.commandId.getCommandsString())
		return True

	def executarSair(self):
		print('Apenas os guerreiros mortos em batalha irão para os salões dourados! ')
		print('Pressione uma tecla para sair...')
		input()
		return False

	def executarAtacar(self, command):
		return True

	def executarDefender(self, command):
		return True

	def play(self):
		playing = True
		self.printWelcome()
		print('')
		while(playing == True):
			self.printRoomInfo()
			print('')
			command = self.commandId.idCommand()
			print('')
			playing = self.selectCommand(command)


eraDosVikings = Game()
eraDosVikings.play()
