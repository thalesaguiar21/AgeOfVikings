
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

		if(hp > 0):
			self.hp = hp
		else:
			self.hp = 50
		if(mp > 0)
			self.mp = mp
		else:
			self.mp = 25
		self.atk = 0.0
		self.defense = 0.0
		self.carryWeight = 0.0
		self.bag = {}

	def getName(self):
		return self.name

	def getHp(self):
		return self.hp

	def getBag(self):
		return self.bag

	def getMp(self):
		return self.mp

	def getDefense(self):
		return self.defense

	def getAtk(self):
		return self.atk

	def getWeapons(self):
		pass

	def getArmors(self):
		pass

	def getEtc(self):
		pass

	def setName(self, name):
		self.name = name

	def maxStat(self, stat1, stat2, maximum):
		if(stat1 + stat2 > maximum):
			stat2 = maximum - stat1
		elif(stat1 + stat2 < 0):
			stat2 = 0 - stat1
		return stat2

	def setHp(self, hp):
		self.hp += self.maxStat(self.hp, hp, MAX_HP)

	def setMp(self, mp):
		self.mp += self.maxStat(self.mp, mp, MAX_MP)
		
	def setDefense(self, defense):
		self.defense += self.maxStat(self.defense, defense, MAX_DEFENSE)
		
	def setAtk(self, atk):
		self.atk += self.maxStat(self.atk, atk, MAX_ATK)

	def addToBag(self, item):
		if(self.carryWeight + item.getWeight < CARRY_CAPACITY)
			self.bag[item.getName()] = item
			self.carryWeight += item.getWeight()
		else:
			return 'Você está carregando muitos itens!'

	def rmFromBag(self, name):
		try
			del self.bag[name]
		except KeyError:
			return 'Você não possui esse item!'

	def listBag(self):
		bagString = ''
		for keys in self.bag:
			bagString += ' ' + keys
		return bagString

