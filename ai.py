import game
from time import sleep
from os import system

class SimpleAI(game.game):
	def __init__(self, r, *args):
		'''
		Initializes the AI object using game.game's __init__
		function.

		r - ratio for heuristic function
		*args - all other arguments for the creation of the game
		'''
		self.r = r
		game.game.__init__(self, *args)
		self.testGame = game.game(*args)

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

	def loop(self, printBoard=False):
		'''
		Overwrites the loop function in game.game to fit the
		playstyle of the AI
		'''
		while not self.isOver():
			possible = self.canMove()
			# print possible
			bestMove = None
			bestH = 0
			for move in possible:
				self.testGame.board = self.board
				self.testGame.slide(move)
				if self.value(self.testGame.board) > bestH:
					bestH = self.value(self.testGame.board)
					bestMove = move
			self.slide(bestMove)
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
				scores.append(self.score)
			print 'Max Score:', max(scores)
			print 'Min Score:', min(scores)
			print 'Average Score:', sum(scores)/len(scores)
		except KeyboardInterrupt:
			print 'Max Score:', max(scores)
			print 'Min Score:', min(scores)
			print 'Average Score:', sum(scores)/len(scores)
