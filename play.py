import game

def playGameHuman(size=4, prob=.9, goal=2048, numStartTiles=2):
	playerGame = game.game(size, prob, goal, numStartTiles)
	playerGame.printBoard()
	while playerGame.canMove():
		move = raw_input('Move: ').lower()
		if move == 'exit':
			break
		try:
			playerGame.slide(move)
			playerGame.printBoard()
			print '\n'
		except:
			print 'Invalid Move...'
	if playerGame.isWon():
		print 'You win!'
	else:
		print 'Game over.'
	print 'Your score:', playerGame.getScore()

if __name__ == '__main__':
	playGameHuman()