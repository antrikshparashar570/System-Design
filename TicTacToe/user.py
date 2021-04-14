import random

class User:
	def __init__(self, name):
		self.name = name
		self.id = random.randint(1, 10)


	def getName(self):
		return self.name

	def setname(self, name):
		self.name = name

	def getId(self):
		return self.id