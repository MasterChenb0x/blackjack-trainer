#!/usr/bin/python

# Import the universe, or at least what is needed
import sys
import random
from card_functions import *
from blk_jak_functions import *

# Function to restart game if bust, out of deck, or just something happens
def game_over(player_total, fulldeck):
        if player_total > 21:
            print("You busted, would you like to play again?")
        elif len(fulldeck) == 0:
            print("The deck ran out of cards, would you like to play again")
        else:
            print("I am not sure what happened, would you like to play again though?")
        q = input("(Y)es or (N)o?:")
        if q.upper() == "Y":
            fulldeck, player_hand, ph_total, dealer_hand, dh_total = new_game(deck_size)
            eleven = 0
            count = 0
            return fulldeck, player_hand, ph_total, dealer_hand, dh_total, eleven, count
        else:
            print("Thank you for playing")
            sys.exit()

# Basic Flow, to test all functions

print("Welcome to the BlackJack Card Counting Testing Suite")
deck_size = deck_count()
fulldeck = Deck(deck_size)
print("")
print("")

while True:
    # Deals out a card, and updates player_hand, ph_total, and count correctly
    fulldeck, card = deal(fulldeck)
    player_hand.append(card)
    ph_total, elevens = faceSum(card, ph_total, elevens)
    count = hilo_counter(card, count)
    if len(player_hand) < 2:
        continue # using this to get starting hand
    print("")
    # Checks if player hand is over 21, checks to see if any aces are 11
    if ph_total > 21:
        ph_total, elevens = ace_bust_check(ph_total, elevens)
        if ph_total > 21:
            gui(player_hand, ph_total, count)
            fulldeck, player_hand, ph_total, dealer_hand, dh_total, eleven, count = game_over(ph_total, elevens)
            if ph_total == 0:
                continue
    gui(player_hand, ph_total, count)
    # Asks if you want to hit or stand
    player_hand, ph_total, elevens = player_action(player_hand, ph_total, elevens)
