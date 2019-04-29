#!/usr/bin/python

# We are an import and import company
import sys
import random

# Variable Setup
fulldeck = [] # empty deck list
deck_size = 1
player_hand = [] # empty player hand list
ph_total = 0 #  initial player hand value
dealer_hand = [] # empty dealer hand list
dh_total = 0 # initial dealer hand value

# Creates a combination of 52 card decks, and then randomizes the order
def Deck(decks):
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    cards = cards * 4 * decks
    random.shuffle(cards)
    return cards

# Basic tests to check functions and flow
def deck_count():
    while True:
        decks = input("Would you like 1, 2, or 6 decks in the game:")
        if decks in ["1","2","6"]:
            global deck_size
            deck_size = int(decks)
            break
        else:
            print("Incorrect choice, please try again.")
    return int(deck_size)

# Returns, and removes, the "top" card from the deck
def deal(deck):
    # this is where it causes issues, fulldeck is still = [] here
    #card = fulldeck[0]
    #fulldeck.remove(card)
    card = deck[0]
    return card

# Resets the player hand variables [CURRENTLY NOT WORKING]
def newplayerhand():
    global player_hand
    player_hand = []
    global ph_total
    ph_total = 0

# Resets the dealer hand variables [CURRENTLY NOT WORKING]
def newdealerhand():
    global dealer_hand
    dealer_hand = []
    global dh_total
    dh_total = 0

# Runs the reset functions, and reinitializes the deck [CURRENTLY NOT WORKING]
def new_game():
    global fulldeck
    fulldeck = Deck(deck_size)
    newplayerhand()
    newdealerhand()

if __name__ == "__main__":
    print("This file contains basic card game functions.")
    sys.exit()
