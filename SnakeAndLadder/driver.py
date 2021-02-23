from services.snakeAndLadderService import SnakeAndLadderService
from model.player import Player
from model.snake import Snake
from model.ladder import Ladder
from model.board import Board


def main():

    noOfSnakes = int(input())
    snakes = []
    for i in range(noOfSnakes):
        snakes.append(Snake(int(input()), int(input())))

    noOfLadders = int(input())
    ladders = []
    for i in range(noOfLadders):
        ladders.append(Ladder(int(input()), int(input())))

    noOfPlayers = int(input())
    players = []
    for i in range(noOfPlayers):
        players.append(Player(str(input())))

    size = int(input())
    snakeAndLadder1 = SnakeAndLadderService(size)
    snakeAndLadder1.setPlayers(players)
    snakeAndLadder1.setSnakes(snakes)
    snakeAndLadder1.setLadders(ladders)

    snakeAndLadder1.startGame()

if __name__ == '__main__':
    main()