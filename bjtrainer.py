#!/usr/bin/python

# Import the universe, or at least what is needed
import sys
import random
from bjsetup import *

# Return the count status of the card passed through the method
def counter(card):
	c = -1
	try:
		thisCard = int(card)
		if thisCard <= 6:
			c = 1
		elif thisCard <= 9:
			c = 0
	except:
		if card in [10,'J','Q','K','A']:
			c = -1
	return c

# Convert face cards to their integer value
def faceSum(card):
	sum = 0
	if card in ['J','Q','K']:
		sum = 10
	elif card == 'A':
        	aceCard = raw_input("Do you want your card to be 1 or 11?")
                if aceCard == '1':
                	sum = 1
                else:
                        sum = 11
	else:
		sum = int(card)
	return sum


# Tell the users what this is and how to use
def usage():
	print "Welcome to the BlackJack Trainer (Super Alpha)"
	print "Hopefully this doesn't break while you are playing."


def deal():
	card = fulldeck[random.randint(0,len(fulldeck)-1)]
        fulldeck.remove(card)
	return card

def newhand():
	global PlayerHand
	PlayerHand = [0,0,0,0,0,0,0]
	global i
	i = 0

# More initialization
def initialization():
	global PlayerHand
	PlayerHand = [0,0,0,0,0,0,0]
	global fulldeck
	fulldeck = []
	fulldeck = Deck() * deckselect()
	print fulldeck
	global count
	count = 0
	global total
	total = 0
	global card
	card = 0
	global i
	i = 0
	print "The deck is now shuffled"

# Start of main game
play = "1"
initialization()
while play == "1":
	newhand()
	try:
		PlayerHand[i] = deal()
        	count += counter(PlayerHand[i])
        	i += 1
        	PlayerHand[i] = deal()
        	count += counter(PlayerHand[i])
        	print "Your hand: {0},{1}".format(PlayerHand[0], PlayerHand[1])
        	print "The count is: {0}".format(count)
        	PlayerHand[0] = faceSum(PlayerHand[0])
        	PlayerHand[1] = faceSum(PlayerHand[1])
        	total = int(PlayerHand[0]) + int(PlayerHand[1])
        	print "The total is: {0}".format(total)
        	if total <= 21:
                	hitstand = raw_input("Hit(1) or Stand(2)?")
                	while hitstand == "1":
                        	i += 1
                        	PlayerHand[i] = deal()
                        	print PlayerHand[i]
                        	count += counter(PlayerHand[i])
                        	print "The count is: {0}".format(count)
                        	PlayerHand[i] = faceSum(PlayerHand[i])
                        	total += int(PlayerHand[i])
                        	print "The total is: {0}".format(total)
				if total > 21:
					print "You BUSTED and you lose."
					hitstand = "2"
				else:
                        		hitstand = raw_input("Hit(1) or Stand(2)?")
				
	except ValueError:
		# The ValueError Exception is a shuffle of the deck essentially.
		initialization()
		PlayerHand[i] = deal()
        	count += counter(PlayerHand[i])
        	i += 1
        	PlayerHand[i] = deal()
        	count += counter(PlayerHand[i])
        	print "Your hand: {0},{1}".format(PlayerHand[0], PlayerHand[1])
        	print "The count is: {0}".format(count)
        	PlayerHand[0] = faceSum(PlayerHand[0])
        	PlayerHand[1] = faceSum(PlayerHand[1])
        	total = int(PlayerHand[0]) + int(PlayerHand[1])
        	print "The total is: {0}".format(total)
        	if total <= 21:
                	hitstand = raw_input("Hit(1) or Stand(2)?")
                	while hitstand == "1":
                        	i += 1
                        	PlayerHand[i] = deal()
                        	print PlayerHand[i]
                        	count += counter(PlayerHand[i])
                        	print "The count is: {0}".format(count)
                        	PlayerHand[i] = faceSum(PlayerHand[i])
                        	total += int(PlayerHand[i])
                        	print "The total is: {0}".format(total)
				if total > 21:
                                        print "You BUSTED and you lose."
					hitstand = "2"
                                else:
                                        hitstand = raw_input("Hit(1) or Stand(2)?")
	print "The total is: {0}".format(total)
	print "The count is: {0}".format(count)
	print fulldeck
	play = raw_input("Deal? Yes(1)/No(2)")
	

