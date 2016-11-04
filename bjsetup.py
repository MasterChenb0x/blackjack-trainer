#!/usr/bin/python

import sys
import random

# Initialize the deck of cards
def Deck():
        cards = ['2','3','4','5','6','7','9','10','J','Q','K','A']
        return cards * 4

def deckselect():
        dint = input("How Many decks will we use? (1,2, or 6)")
        d = int(dint)
        while d not in [1,2,6]:
                dint = input("How many decks will we use? (1, 2, or 6)")
                d = int(dint)
                if d == 1:
                        print "Single Deck.\n"
                        d = 1
                        return d
                elif d == 2:
                        d = 2
                        print "Double Deck.\n"
                        return d
                elif d == 6:
                        print "6 Deck Shoe.\n"
                        d = 6
                        return d
                elif d not in [1,2,6]:
                        print "You didn't choose a proper deck size."
        return d

if __name__ == "__main__":
	print "This file does nothing on its own..."
	sys.exit()
