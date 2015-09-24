#!/usr/bin/python

import sys
import random

class Deck():
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

def counter(card):
	c = 0
	if card == '2' or card == '3' or card == '4' or card == '5' or card == '6':
		c = 1
	elif card == '7' or card == '8' or card ==  '9':
		c = 0
	elif card == '10':
		c = c-1
	elif card == 'J' or card == 'Q' or card == 'K' or card == 'A':
		c = c-1
	else:
		c = 0

	return c

def usage():
	print "Welcome to the BlackJack Trainer (Super Alpha)\n\n"

usage()
d1 = Deck()
count = 0
exit = False
while not exit:
	card = d1.cards[random.randint(0,len(d1.cards)-1)]
	print card
	
	count = count + counter(card)
	print count

	response = raw_input("Keep counting?(y/n)")
	if response == "n":
		exit = True
