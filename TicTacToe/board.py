import random

class Board:
	def __init__(self, rows, columns):
		self.matrix = [[random.randint(1, 100) for j in range(columns)] for i in range(rows)]
		print(self.matrix)

	def getVal(self, x, y):
		return self.matrix[x][y]

	def setVal(self, x, y, val):
		self.matrix[x][y] = val

	def printMatrix(self):
		print(self.matrix)

	def getRows(self):
		return len(self.matrix)

	def getColumns(self):
		return len(self.matrix[0])
