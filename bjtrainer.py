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

#Hit or Stand function
def HitStand():
	hitstand = raw_input("Hit or Stand?")
        while hitstand == "Hit":
        	card3 = deal()
                count = count + counter(card3)
               	card3 = faceSum(card3)
                total = total + int(card3)
                hitstand = "Stand"

# Tell the users what this is and how to use
def usage():
	print "Welcome to the BlackJack Trainer (Super Alpha)"
	print "Hopefully this doesn't break while you are playing."


def deal():
	card = fulldeck[random.randint(0,len(fulldeck)-1)]
        fulldeck.remove(card)
	return card

# More initialization
def initialization():
	global PlayerHand
	PlayerHand = [0,0,0,0,0]
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

# Start of main game
initialization()
play = 1
while play == 1:
	try:
		PlayerHand[0] = deal()
		PlayerHand[1] = deal()
		count += counter(PlayerHand[0])
        	count += counter(PlayerHand[1])
		print "Your hand: {0},{1}".format(PlayerHand[0], PlayerHand[1])
		print "The count is: {0}".format(count)
		PlayerHand[0] = faceSum(PlayerHand[0])
		PlayerHand[1] = faceSum(PlayerHand[1])
		total = int(PlayerHand[0]) + int(PlayerHand[1])
		print "The total is: {0}".format(total)
		if total < 21:
			hitstand = raw_input("Hit or Stand?")
                        while hitstand == "Hit":
                                PlayerHand[2] = deal()
				print PlayerHand[2]
                                count += counter(PlayerHand[2])
				print "The count is: {0}".format(count)
                                PlayerHand[2] = faceSum(PlayerHand[2])
                                total += int(PlayerHand[2])
                                hitstand = "Stand"

	except ValueError:
		# The ValueError Exception is a shuffle of the deck essentially.
		initialization()
		PlayerHand[0] = deal()
		PlayerHand[1] = deal()
		count += counter(PlayerHand[0])
        	count += counter(PlayerHand[1])
		print "Your hand: {0},{1}".format(PlayerHand[0], PlayerHand[1])
		print "The count is: {0}".format(count)
		PlayerHand[0] = faceSum(PlayerHand[0])
		PlayerHand[1] = faceSum(PlayerHand[1])
		total = int(PlayerHand[0]) + int(PlayerHand[1])
		print "The total is: {0}".format(total)
                if total < 21:
                        hitstand = raw_input("Hit or Stand?")
                        while hitstand == "Hit":
                                PlayerHand[2] = deal()
				print PlayerHand[2]
                                count = count + counter(PlayerHand[2])
				print "The count is: {0}".format(count)
                                PlayerHand[2] = faceSum(PlayerHand[2])
                                total += int(PlayerHand[2])
                                hitstand = "Stand"

	print "The total is: {0}".format(total)
	print "The count is: {0}".format(count)
	print fulldeck
	response = raw_input("Deal?(y/n)")
	if response == "n":
		play = 0

