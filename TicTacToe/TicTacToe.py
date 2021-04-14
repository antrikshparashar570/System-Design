from user import User
from board import Board

class TicTacToeService:
	def __init__(self, rows, columns, users):
		self.userMoves = {}
		for user in users:
			self.userMoves[user.getId()] = []
		self.users = users
		self.Board = Board(rows, columns)
		self.moves = []


	def checkCase(self, x, y):
		if x >= 0 and x < self.Board.getRows() and y >= 0 and y < self.Board.getColumns():
			return 1
		return 0

	def isGameCompleted(self):
		if self.Board.getVal(0, 0) == self.Board.getVal(1, 1) and self.Board.getVal(1, 1) == self.Board.getVal(2, 2) or self.Board.getVal(0, 0) == self.Board.getVal(1, 0) and self.Board.getVal(1, 0) == self.Board.getVal(2, 0) or self.Board.getVal(0, 2) == self.Board.getVal(1, 1) and self.Board.getVal(1, 1) == self.Board.getVal(2, 0):
			return 1
		elif self.Board.getVal(0, 0) == self.Board.getVal(0, 1) and self.Board.getVal(0, 1) == self.Board.getVal(0, 2) or self.Board.getVal(0, 2) == self.Board.getVal(1, 2) and self.Board.getVal(1, 2) == self.Board.getVal(2, 2) or self.Board.getVal(2, 0) == self.Board.getVal(2, 1) and self.Board.getVal(2, 1) == self.Board.getVal(2, 2):
			return 1
		elif self.Board.getVal(1, 0) == self.Board.getVal(1, 1) and self.Board.getVal(1, 1) == self.Board.getVal(1, 2) or self.Board.getVal(0, 1) == self.Board.getVal(1, 1) and self.Board.getVal(1, 1) == self.Board.getVal(2, 1):
			return 1

		return 0

	def movePlayer(self, user, flag, x, y):
		if flag == 0:
			self.Board.setVal(x, y, 0)
		else:
			self.Board.setVal(x, y, 1)

		self.userMoves[user.getId()].append((x, y))

	def startGame(self):
		flag = 0
		while not self.isGameCompleted():
			if len(self.moves) >= 3*3:
				print("Nobody wins")
				return

			movex = int(input())
			movey = int(input())

			if self.checkCase(movex, movey):
				if (movex, movey) in self.moves:
					print("error")
				else:
					self.moves.append((movex, movey))

					if flag == 0:
						self.movePlayer(self.users[0], flag, movex, movey)
						flag = 1
					else:
						self.movePlayer(self.users[1], flag, movex, movey)
						flag = 0

					print(self.moves)
					self.Board.printMatrix()
			else:
				print("move not valid")

		if flag == 0:
			print(self.users[1].getName() + " wins")
		else:
			print(self.users[0].getName() + " wins")
