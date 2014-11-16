import game
from time import sleep
from os import system

class SimpleAI(game.Game):
	def __init__(self, r, *args):
		'''
		Initializes the AI object using game.Game's __init__
		function.

		r - ratio for heuristic function
		*args - all other arguments for the creation of the game
		'''
		self.r = r
		game.Game.__init__(self, *args)
		self.testGame = game.Game(*args)

	def value(self, board):
		'''
		Calculates the 'value' of the board based on the ratio
		the board given

		returns: heuristic value for the board
		'''
		r = 1
		hScore = 0
		for rowIndex in range(len(board)):
			row = board[rowIndex] if rowIndex%2 == 0 else board[rowIndex][::-1] 
			for val in row:
				hScore += r*val
				r *= self.r
		return hScore

	def getBestMove(self, board):
		'''
		Determines the optimal move based on the value function

		returns: direction of optimal move
		'''
		self.testGame.board = board
		bestMove = None
		bestH = 0
		for move in self.testGame.canMove():
			self.testGame.board = board
			self.testGame.score = 0
			self.testGame.slide(move, addTile=False)
			if (self.value(self.testGame.board) + self.testGame.score) > bestH:
				bestH = (self.value(self.testGame.board) + self.testGame.score)
				bestMove = move
		return bestMove

	def loop(self, printBoard=False):
		'''
		Overwrites the loop function in game.Game to fit the
		playstyle of the AI
		'''
		while not self.isOver():
			self.slide(self.getBestMove(self.board))
			# system('clear')
			# self.printBoard()
			# sleep(.5)
		if printBoard: self.printBoard() 

	def simPlay(self, numTrials):
		'''
		Plays a 2048 game from start to finish numTrials times
		and prints the max, min, and average score
		'''
		try:
			scores = []
			for i in range(numTrials):
				if i%100 == 0:
					print i
				self.reset()
				self.loop()
				if self.isWon():
					print 'Winner Winner'
					self.printBoard()
				scores.append(self.score)
			print 'Max Score:', max(scores)
			print 'Min Score:', min(scores)
			print 'Average Score:', sum(scores)/len(scores)
		except KeyboardInterrupt:
			print 'Max Score:', max(scores)
			print 'Min Score:', min(scores)
			print 'Average Score:', sum(scores)/len(scores)

class DigDeeperAI(SimpleAI):
	def __init__(self, *args):
		SimpleAI.__init__(self, *args)

	def loop(self, printBoard=False):
		while not self.isOver():
			bestMove = None
			bestH = 0
			for move in self.canMove():
				self.testGame.board = self.board
				self.testGame.slide(move, addTile=False)
				m = self.getBestMove(self.testGame.board)
				self.testGame.slide(m, addTile=False)
				# print move, m, self.value(self.testGame.board), bestH
				if self.value(self.testGame.board) > bestH:
					bestH = self.value(self.testGame.board)
					bestMove = move
			# print bestMove
			self.slide(bestMove)
			sleep(.5)
			system('clear')
			self.printBoard()
			# print self.value(self.board)
		if printBoard: self.printBoard()
