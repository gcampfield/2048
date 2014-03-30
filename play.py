from game import *

def playGameHuman(w=4, h=4, prob=.9, goal=2048) :
	currentGame = game(w, h, prob)
	while not currentGame.isWon() :
		move = raw_input('Move: ')
		try :
			currentGame.slide(move)
			currentGame.printBoard()
		except :
			print 'Invalid Move...'