from services.diceRollService import DiceService
from model.board import Board
from model.player import Player

class SnakeAndLadderService:
    def __init__(self, boardSize):
        self.board = Board(boardSize)
        self.noOfPlayers = 0
        self.players = []

    def setPlayers(self, players):
        self.noOfPlayers = len(players)
        playerPieces = {}
        for player in players:
            self.players.append(player)
            playerPieces[player.getId()] = 0

        self.board.setPlayerPieces(playerPieces)

    def setSnakes(self, snakes):
        self.board.setSnakes(snakes)

    def setLadders(self, ladders):
        self.board.setLadders(ladders)

    def rollDice(self):
        return DiceService.roll(self)

    def isGameCompleted(self):
        currentPLayersSize = len(self.players)
        return currentPLayersSize < self.noOfPlayers

    def checkThroughSnakesAndLadders(self, newPosition):
        previousPosition = None

        while (previousPosition != newPosition):
            previousPosition = newPosition

            for snake in self.board.getSnakes():
                if snake.getStart() == newPosition:
                    newPosition = snake.getEnd()

            for ladder in self.board.getLadders():
                if ladder.getStart() == newPosition:
                    newPosition = ladder.getEnd()

        return newPosition

    def movePlayer(self, player, positions):
        oldPosition = self.board.getPlayerPieces()[player.getId()]
        newPosition = oldPosition + positions

        boardSize = self.board.getBoardSize()

        if newPosition > boardSize:
            newPosition = oldPosition
        else:
            newPosition = self.checkThroughSnakesAndLadders(newPosition)

        self.board.getPlayerPieces()[player.getId()] = newPosition

    def hasPlayerWon(self, player):
        playerPosition = self.board.getPlayerPieces()[player.getId()]
        print(playerPosition)
        return playerPosition == self.board.getBoardSize()

    def startGame(self):
        summ = {}
        while not (self.isGameCompleted()):
            currentPlayer = self.players.pop(0)
            print(currentPlayer.getName() + " chance")
            if currentPlayer.getName() not in summ:
                summ[currentPlayer.getName()] = 0
            diceValue = self.rollDice()
            summ[currentPlayer.getName()] += diceValue
            print(diceValue)
            print(summ)
            self.movePlayer(currentPlayer, diceValue)
            if self.hasPlayerWon(currentPlayer):
                print(currentPlayer.getName() + " wins the game")
                del self.board.getPlayerPieces()[currentPlayer.getId()]
                break
            else:
                self.players.append(currentPlayer)


