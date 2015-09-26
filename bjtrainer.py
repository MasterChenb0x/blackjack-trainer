#!/usr/bin/python

import sys
import random

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

def usage():
	print "Welcome to the BlackJack Trainer (Super Alpha)\n\n"

d1 = Deck()
count = 0

DELETEME = 1

usage()

exit = False
while not exit:
	try:
		card = d1[random.randint(0,len(d1)-1)]
	except ValueError:
		d1 = Deck()
		card = d1[random.randint(0,len(d1)-1)]
	print "Your card: {0}".format(card)
	
	count = count + counter(card)
	print "The coount is: {0}".format(count)

	d1.remove(card)
	print d1
	response = raw_input("Deal?(y/n)")
	if response == "n":
		exit = True


