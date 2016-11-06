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
#Convert face cards to their integer value
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

# More initialization
usage()
fulldeck = []
fulldeck = Deck() * deckselect()
print fulldeck
count = 0
total = 0

play = 1
while play == 1:
	try:
		card1 = deal()
		card2 = deal()
		count = count + counter(card1)
        	count = count + counter(card2)
		print "Your hand: {0},{1}".format(card1, card2)
		card1 = faceSum(card1)
		card2 = faceSum(card2)
		total = int(card1) + int(card2)
	except ValueError:
		fulldeck = []
		fulldeck = Deck() * deckselect()
		print fulldeck
		count = 0
		card1 = deal()
		card2 = deal()
		count = count + counter(card1)
        	count = count + counter(card2)
		print "Your hand: {0},{1}".format(card1, card2)
		card1 = faceSum(card1)
		card2 = faceSum(card2)
		total = int(card1) + int(card2)
	print "The total is: {0}".format(total)
	print "The count is: {0}".format(count)
	print fulldeck
	response = raw_input("Deal?(y/n)")
	if response == "n":
		play = 0

