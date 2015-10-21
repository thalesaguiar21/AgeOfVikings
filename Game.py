from CommandIdentifier import *
from Command import *
from CommandList import *
from Room import *
import os

class Game(object):

	''' Classe principal do jogo '''

	def __init__(self):
		self.commandId = CommandIdentifier()
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
		arredoresDeSiegheim1 = Room('arredores de Siegheim', ' ao sair da sua cabana, você se encontra nas florestas que rodeiam as ruinas de'\
			+ ' Siegheim(nome da cidade principal dos dominios do rei ragnar)')
		arredoresDeSiegheim2 = Room('arredores de Siegheim', ' andando pelo caminho, você lembra dos passeios com seu pai por essas mesmas florestas.'\
			+ ' Olhando ao redor você observa alguns cogumelos e lembra dos ensinamentos de seu pai, explicando os efeitos de cada planta nas florestas.')
		arredoresDeSiegheim3 = Room('arredores de Siegheim', ' seguindo frente você se depara com uma bifurcação no caminho. Você acha estranho,'\
			+ ' pois o caminho havia se alterado repentinamente.')
		arredoresDeSiegheim4 = Room('arredores de Siegheim', ' você anda com desconfiança pela floresta desconhecida. Ao longe observa-se uma slhueta de uma pessoa.')
		eremita = Room('velho eremita misterioso', 'Aproximando-se, a silhueta toma a forma de um senhor de idade. Enquanto você passa ele joga pragas'\
			+ ' aos ventos. No momento em que ele o vê, os olhos do eremita se enchem de raiva. O senhor começa a esbravejar insunuações sobre o seu pai ter'\
			+ ' sido a ruína dos bárbaros. Logo após ele corre em direção a mata dansa e nebulosa.')
		arredoresDeSiegheim5 = Room('arredores de Siegheim', ' com o tempo você começa a reconhecer o caminho. Lembra que havia uma cicatriz naquela árvore.'\
			+ ' a partir desse momento você se dá conta de que se aproxima das ruínas do palácio.')


		#Adicionando as segundas descrições
		cabana.setDescription2(' seu quarto, nele você pode ver sua cama e algumas coisas comuns')
		cozinha.setDescription2(' sua cozinha. Você pode ver sua dispensa e mesa.')
		dispensa.setDescription2(' armário antigo')
		cama.setDescription2(' sua cama')
		arredoresDeSiegheim1.setDescription2(' arredores de sigheim, próxima a sua cabana.')
		arredoresDeSiegheim2.setDescription2(' arredores de Siegheim, essa área possui várias plantas medicinais.')
		arredoresDeSiegheim3.setDescription2(' arredores de Siegheim, você se encontra na bifurcação estranha.')
		arredoresDeSiegheim4.setDescription2(' arredores de Siegheim, local próximo ao seu encontro com o eremita.')
		arredoresDeSiegheim5.setDescription2(' arredores de Siegheim, você está mais próximo das ruínas.')
		eremita.setDescription2(' arredores de Siegheim, local exato onde você encontrou o eremita.')


		#Adicionando saídas as salas
		salaMisteriosa.setExits('correr', cabana)

		cabana.setExits('porta', cozinha)
		cabana.setExits('cama', cama)

		cozinha.setExits('porta', cabana)
		cozinha.setExits('dispensa', dispensa)
		cozinha.setExits('fora da cabana', arredoresDeSiegheim1)

		dispensa.setExits('cozinha', cozinha)

		cama.setExits('quarto', cabana)

		arredoresDeSiegheim1.setExits('cabana', cozinha)
		arredoresDeSiegheim1.setExits('continuar andando', arredoresDeSiegheim2)
		arredoresDeSiegheim2.setExits('voltar', arredoresDeSiegheim1)
		arredoresDeSiegheim2.setExits('seguir em frente', arredoresDeSiegheim3)
		arredoresDeSiegheim3.setExits('voltar', arredoresDeSiegheim2)
		arredoresDeSiegheim3.setExits('esquerda', arredoresDeSiegheim4)
		arredoresDeSiegheim3.setExits('direita', arredoresDeSiegheim5)
		arredoresDeSiegheim4.setExits('voltar', arredoresDeSiegheim3)
		arredoresDeSiegheim4.setExits('se aproximar da silhueta', eremita)
		arredoresDeSiegheim5.setExits('voltar', arredoresDeSiegheim3)

	

		
		#Criando itens
		bilhete = Item('bilhete', ' "Encontre-me nas ruinas do antigo rei,\nDe: Seu amigo\nPara: Sieg"')
		roupas = Item('roupas', 'Roupas de couro de animais das redondezas, protegem bastante contra o frio')
		machado = Item('machado', 'Um machado comum')
		escudo = Item('escudo', 'Escudo de madeira feito pelo seu pai.')
		frutas = Item('frutas', 'algumas frutas que sobraram antes do início do inverno.')
		simboloDeCaçada = Item('Troféu', 'A cabeça de um javali morto na sua primeira caçada com seu pai. Olhar ela lhe traz lembranças de sua infância...'\
			+ ' De quando você ainda estava aprendendo a segurar seu escudo.')
		cogumelosVerdes = Item('cogumelo verde', 'Cogumelo com capacidades curativas')
		

		#Adicionando itens as salas
		cabana.addItem(roupas)
		cabana.addItem(machado)
		cabana.addItem(escudo)

		cozinha.addItem(simboloDeCaçada)
		cozinha.addItem(bilhete)

		dispensa.addItem(frutas)

		arredoresDeSiegheim2.addItem(cogumelosVerdes)

		#Atribuindo a sala inicial
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
		print('0. Este jogo ainda está em desenvolvimento, é possível encontrar bugs ou funcionalidades pendentes.')
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

		elif(not command.hasSecondWord() and command.getFirstWord() not in self.commandId.getOneWords()):
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
			os.system('CLS')
			#os.system('clear')
			self.printWelcome()
			print('')
			self.printRoomInfo()
			self.actualRoom.setVisited()
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
		if(self.lastRoom != None):
			if(self.lastRoom in self.actualRoom.getExitsDict().values()):
				aux = self.actualRoom
				self.actualRoom = self.lastRoom
				self.lastRoom = aux
				self.printLogo
				self.printRoomInfo()
		else:
			print('Não há salas para voltar =\'(')
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
		self.printRoomInfo()
		print('')
		while(playing == True):
			command = self.commandId.idCommand()
			print('')
			playing = self.selectCommand(command)

keepPlaying = 1
while(keepPlaying == 1):
	os.system('CLS')
	#os.system('clear')
	eraDosVikings = Game()
	eraDosVikings.play()
	print('Pressione uma tecla para jogar novamente: ')
	input()
print('Nos encontraremos em Valhala, nobre guerreiro')
