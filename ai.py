import game

class SimpleAI(game.game):
	def __init__(self, r=.5, size=4, prob=.9, goal=2048, numStartTiles=2):
		self.r
		game.game.__init__(self, size, prob, goal, numStartTiles)

	# def value(board):
	# 	r = self.r
	# 	for row in board:
	# 		for val in row:
