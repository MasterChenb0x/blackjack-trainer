#!/usr/bin/python

# Import the universe, or at least what is needed
import sys
import random
from bjsetup import *
from bjfunctions import *


def deal():
	card = fulldeck[random.randint(0,len(fulldeck)-1)]
        fulldeck.remove(card)
	return card

def newplayerhand():
	global PlayerHand
	PlayerHand = [0,0,0,0,0,0,0]
	global ph
	ph = 0

def newdealerhand():
	global DealerHand
	DealerHand = [0,0,0,0,0,0,0]
	global dh
	dh = 0


fulldeck = []
fulldeck = Deck() * deckselect()
print fulldeck
count = 0
total = 0
card = 0
ph = 0
print "The deck is now shuffled"

# Start of main game
usage()
play = "1"
while play == "1":
	newplayerhand()
	newdealerhand()
	try:
		PlayerHand[ph] = deal()
        	count += counter(PlayerHand[ph])
        	ph += 1
		# ! Below code to ValueError is functional if placed after "The deck is now shuffled", just in case it needs to be placed back there again.
        	PlayerHand[ph] = deal()
        	count += counter(PlayerHand[ph])
        	print "Your hand: {0},{1}".format(PlayerHand[0], PlayerHand[1])
        	print "The count is: {0}".format(count)
        	PlayerHand[0] = faceSum(PlayerHand[0])
        	PlayerHand[1] = faceSum(PlayerHand[1])
        	total = int(PlayerHand[0]) + int(PlayerHand[1])
        	print "The total is: {0}".format(total)
        	if total <= 21:
                	hitstand = raw_input("Hit(1) or Stand(2)?")
                	while hitstand == "1":
                        	ph += 1
                        	PlayerHand[ph] = deal()
                        	print PlayerHand[ph]
                        	count += counter(PlayerHand[ph])
                        	print "The count is: {0}".format(count)
                        	PlayerHand[ph] = faceSum(PlayerHand[ph])
                        	total += int(PlayerHand[ph])
                        	print "The total is: {0}".format(total)
				if total > 22:
					print "You BUSTED and you lose."
					hitstand = "2"
				else:
                        		hitstand = raw_input("Hit(1) or Stand(2)?")
				
	except ValueError:
		# The ValueError Exception is a shuffle of the deck essentially.
		fulldeck = []
		fulldeck = Deck() * deckselect()
		print fulldeck
		count = 0
		total = 0
		card = 0
		ph = 0
		print "The deck is now shuffled"
	print "The total is: {0}".format(total)
	print "The count is: {0}".format(count)
	print fulldeck
	play = raw_input("Deal? Yes(1)/No(2)")
	

