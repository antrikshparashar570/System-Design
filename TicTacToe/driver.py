from user import User
from TicTacToe import TicTacToeService

def driver():
	users = []
	n = int(input())

	for i in range(n):
		users.append(User(str(input())))

	rows = int(input())
	columns = int(input())

	TictacToe = TicTacToeService(rows, columns, users)

	TictacToe.startGame()


driver()