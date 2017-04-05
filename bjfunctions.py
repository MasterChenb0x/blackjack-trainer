#!/usr/bin/pythonj

import sys
import random
# Functions that do the background functions of a blackjack game.

# Returns a count of the card passed to the function. The return should be appended to a running count in the main game.
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
