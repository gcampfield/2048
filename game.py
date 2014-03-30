import random

class game(object) :
	def __init__(self, w=4, h=4, prob=.9) :
		self.board = [[0]*w]*h
		self.score = 0
		self.prob = prob

	def getScore(self) :
		return self.score

	def printBoard(self) :
		pass

	def getEmptyTiles(self) :
		emptyTiles = []
		for rowNum in range(len(self.board)) :
			for colNum in range(len(self.board[row])) :
				if not self.board[rowNum][colNum] :
					emptyTiles.append((rowNum, colNum))

	def addTile(self, loc=None) :
		row, col = loc if loc else random.choice(self.getEmptyTiles)
		self.board[row][col] = 2 if random.random() < self.prob else 4

	