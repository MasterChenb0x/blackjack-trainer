#!/usr/bin/python

# Import the universe, or at least what is needed
import sys
import random

# Initialize the deck of cards
def Deck():
	cards = [
	'2','2','2','2',
	'3','3','3','3',
	'4','4','4','4',
	'5','5','5','5',
	'6','6','6','6',
	'7','7','7','7',
	'8','8','8','8',
	'9','9','9','9',
	'10','10','10','10',
	'J','J','J','J',
	'Q','Q','Q','Q',
	'K','K','K','K',
	'A','A','A','A'
	]
	return cards

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

# Tell the users what this is an dhow to use
def usage():
	print "Welcome to the BlackJack Trainer (Super Alpha)\n\n"

# More initialization
d1 = Deck()
count = 0
exit = False


while not exit:
	try:
		card1 = d1[random.randint(0,len(d1)-1)]
		card2 = d1[random.randint(0,len(d1)-1)]
		d1.remove(card1)
		d1.remove(card2)
	except ValueError:
		d1 = Deck()
		card1 = d1[random.randint(0,len(d1)-1)]
		d1.remove(card1)
		card2 = d1[random.randint(0,len(d1)-1)]
		d1.remove(card2)
	count = count + counter(card1)
	count = count + counter(card2)
	print "Your hand: {0},{1}".format(card1, card2)
	print "The coount is: {0}".format(count)
	print d1
	response = raw_input("Deal?(y/n)")
	if response == "n":
		exit = True


