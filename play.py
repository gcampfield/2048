import game

def playGameHuman(size=4, prob=.9, goal=2048, numStartTiles=2) :
	playerGame = game.game(size, prob, goal, numStartTiles)
	playerGame.printBoard()
	while not playerGame.isWon() :
		move = raw_input('Move: ').lower()
		if move == 'exit' :
			exit()
		try :
			playerGame.slide(move)
			playerGame.printBoard()
			print '\n'
		except :
			print 'Invalid Move...'
	print 'You win!'
	print 'Your score:', playerGame.getScore()

playGameHuman()