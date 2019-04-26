#!/usr/bin/python

# Import the universe, or at least what is needed
import sys
import random
#from bjsetup import * # disabled for testing, relavent functions have been added below
#from bjfunctions import * # disabled for testing, relavent functions have been added below

# Variable Setup
fulldeck = [] # empty deck list
count = 0 # initial card count
player_hand = [] # empty player hand list
ph_total = 0 #  initial player hand value
elevens = 0 # counter, for aces counting as 11 in hand
dealer_hand = [] # empty dealer hand list
dh_total = 0 # initial dealer hand value


# Basic Function setup

# Creates a combination of 52 card decks, and then randomizes the order
def Deck(decks):
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    cards = cards * 4 * decks
    random.shuffle(cards)
    return cards

# Returns, and removes, the "top" card from the deck
def deal():
    card = fulldeck[0]
    fulldeck.remove(card)
    return card

# Resets the player hand variables
def newplayerhand():
    global player_hand
    player_hand = []
    global ph_total
    ph_total = 0

# Resets the dealer hand variables
def newdealerhand():
    global dealer_hand
    dealer_hand = []
    global dh_total
    dh_total = 0

# Runs the reset functions, and reinitializes the deck (will have to add a varible somewhere, that keeps track of how many decks used, currently set to 1)
def new_game():
    global fulldeck
    fulldeck = Deck(1)
    newplayerhand()
    newdealerhand()

# Simple print format, taking the currant hand, total value, and deck count, currently just a function to allow testing, will probably just be inline
def gui(cards, ph_total, count):
    print(f"Player Hand: {cards}")
    print(f"Current card value: {ph_total}")
    print(f"Current deck count: {count}")


# Returns a count of the card passed to the function. The return should be appended to a running count in the main game.
def counter(card):
    count = 0
    try:
        thisCard = int(card)
        if thisCard <= 6:
            count = 1
        elif thisCard <= 9:
            count = 0
    except:
        if card in [10,'J','Q','K','A']:
            count = -1
    return count

# Convert face cards to their integer value, uses the current total to prevent aces from busting you (will have to figure out how to -10 from total if a future card causes bust, only if the ace was considered an 11, maybe a counter, if eleven = 1: total -= 10, eleven -= 1)
def faceSum(card, total):
    sum = 0
    if card in ['J','Q','K']:
        sum = 10
    elif card == 'A':
        if total + 11 > 21:
            sum = 1
        else:
            sum = 11
    else:
        sum = int(card)
    return sum

# Basic tests to check functions and flow
print("Welcome to the BlackJack Card Counting Testing Suite")
while True:
    decks = input("Select the number of decks you would like to count against 1, 2, 6:")
    if decks in ["1","2","6"]:
        fulldeck = Deck(int(decks)) # Creates a game deck, of the selected number of 52 card decks
        break
    else:
        print("Incorrect choice, please try again.")

print("")
print("")

while True:
    # Deals out a card, and updates player_hand, ph_total, and count correctly
    card = deal()
    player_hand.append(card)
    sum = faceSum(card, ph_total)
    if card == 'A' and sum == 11:
        elevens += 1 # inceasing internal counter of aces treated as an 11, for bust prevention later
    ph_total += sum
    count += counter(card)
    if len(player_hand) < 2:
        continue # using this to get starting hand

    print("")
    #converts an ace from an 11 to a 1 if it would cause you to bust
    if ph_total > 21:
        if elevens > 0:
            ph_total += -10
            elevens += -1
        else:
            gui(player_hand, ph_total, count)
            print("You busted, thanks for playing")
            break
    gui(player_hand, ph_total, count)
    q = input("Hit (1) or Stand (2)")
    if q == "2":
        newplayerhand()
        elevens = 0
