class Board:
    def __init__(self, size):
        self.boardSize = size
        self.snakes = []
        self.ladders = []
        self.playerPieces = {}

    def getBoardSize(self):
        return self.boardSize

    def getSnakes(self):
        return self.snakes

    def setSnakes(self, Snakes):
        self.snakes = Snakes

    def getLadders(self):
        return self.ladders

    def setLadders(self, Ladders):
        self.ladders = Ladders

    def getPlayerPieces(self):
        return self.playerPieces

    def setPlayerPieces(self, playerPieces):
        self.playerPieces = playerPieces