class Character(object):

	#Limites superiores de atributos
	MAX_HP = 200
	MAX_MP = 100
	MAX_ATK = 35.0
	MAX_DEFENSE = 30.0
	CARRY_CAPACITY = 30.0

	''' Classe que define um personagem do jogo '''

	def __init__(self, name, hp = 50, mp = 25):
		if(name != None):
			self.name = name
		else:
			self.name = ''

