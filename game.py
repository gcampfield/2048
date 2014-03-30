import random

class game(object) :
	def __init__(self, w=4, h=4, prob=.9, goal=2048) :
		self.board = [[0 for a in range(w)] for b in range(h)]
		self.score = 0
		self.prob = prob
		self.goal = goal

	def isWon(self) :
		for row in self.board :
			if self.goal in row :
				return True
		return False

	def getScore(self) :
		return self.score

	def printBoard(self) :
		for row in self.board :
			for val in row:
				print '{:<6}'.format(val),
			print

	def getEmptyTiles(self) :
		emptyTiles = []
		for rowNum in range(len(self.board)) :
			for colNum in range(len(self.board[rowNum])) :
				if not self.board[rowNum][colNum] :
					emptyTiles.append((rowNum, colNum))
		return emptyTiles

	def addTile(self, loc=None) :
		try :
			row, col = random.choice(self.getEmptyTiles())
			self.board[row][col] = 2 if random.random() < self.prob else 4
			return True
		except :
			return False

	
	def moveRowHoriz(self, row):
		changed = False
		for tileIndex in range(len(row) - 1):
			thisIndex = tileIndex
			if not row[thisIndex]:
				changed = True
				row[thisIndex] = row[thisIndex + 1]
				row[thisIndex + 1] = 0
		return row, changed

	def move(self, direction):
		changed = False
		if direction == 'left':
			for i in range(len(self.board)):
				row = self.board[i]
				row, changed = self.moveRowHoriz(row)
				self.board[i] = row
		elif direction == 'right':
			for i in range(len(self.board)):
				row = self.board[i]
				row = row[::-1]
				row, changed = self.moveRowHoriz(row)
				row = row[::-1]
				self.board[i] = row
		elif direction == 'down':
		elif direction == 'up':
		return changed

	def merge(self, direction):
		if direction == 'left':
			for row in board:
				for tileIndex in range(len(row) - 1):
					if row[tileIndex] == row[tileIndex + 1]:
						row[tileIndex] *= 2
						row[tileIndex + 1] == 0

	def slide(self, direction):
		changed = move(direction)
		while changed:
			changed = move(direction)
		# merge
		# move