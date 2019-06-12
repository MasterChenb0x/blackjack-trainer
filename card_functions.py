#!/usr/local/bin/python3

# We are an import and import company
import sys
import random

# Variable Setup
fulldeck = []  # empty deck list
deck_size = 0  # empty deck count
player_hand = []  # empty player hand list
ph_total = 0  # initial player hand value
dealer_hand = []  # empty dealer hand list
dh_total = 0  # initial dealer hand value

# Creates a combination of 52 card decks, and then randomizes the order


def Deck(decks):
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = cards * 4 * decks
    random.shuffle(cards)
    return cards

# Basic tests to check functions and flow


def deck_count():
    decks = ""
    while decks not in ["1", "2", "6"]:
        decks = input("Would you like 1, 2, or 6 decks in the game:")
        if decks not in ["1", "2", "6"]:
            print("Incorrect choice, please try again.")
    return int(decks)

# Returns, and removes, the "top" card from the deck


def deal(fulldeck):
    card = fulldeck[0]
    fulldeck.remove(card)
    return fulldeck, card

# Resets the player hand variables


def newplayerhand():
    player_hand = []
    ph_total = 0
    return player_hand, ph_total

# Resets the dealer hand variables


def newdealerhand():
    dealer_hand = []
    dh_total = 0
    return dealer_hand, dh_total

# Runs the reset functions, and reinitializes the deck


def new_game(deck_size):
    new_deck = Deck(deck_size)
    player_hand = []
    ph_total = 0
    dealer_hand = []
    dh_total = 0
    return new_deck, player_hand, ph_total, dealer_hand, dh_total


if __name__ == "__main__":
    print("This file contains basic card game functions.")
    sys.exit()
