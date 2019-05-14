#!/usr/local/bin/python3

# We are an import and import company
import sys

# Variable Setup
count = 0 # initial card count
elevens = 0 # counter, for aces counting as 11 in hand

# Prints the player's current hand, the total value, and the running count
def gui(cards, total, count):
    print(f"Player Hand: {cards}")
    print(f"Current card value: {total}")
    print(f"Current deck count: {count}")
    
# Convert face cards to their integer value, uses the current total to prevent aces from busting you
def faceSum(card, total, elevens):
    card_sum = 0
    if card in ['J','Q','K']:
        card_sum = 10
    elif card == 'A':
        if total + 11 > 21:
            card_sum = 1
        else:
            card_sum = 11
            elevens += 1
    else:
        card_sum = int(card)
    total += card_sum
    return total, elevens

# Checks and modifies the running count, using the Hi-Lo System 
def hilo_counter(card, count):
    try:
        thisCard = int(card)
        if thisCard <= 6:
            count += 1
        elif thisCard <= 9:
            count += 0
    except:
        if card in [10,'J','Q','K','A']:
            count += -1
    return count

# If ph_total is over 21, check to see if any aces in hand are 11s, and if so, switches it to a 1
def ace_bust_check(ph_total, elevens):
    if elevens > 0:
        ph_total += -10
        elevens += -1
    return ph_total, elevens

# Asks if you want to hit or stand
def player_action(player_hand, ph_total, elevens):
    while True:
        q = input("Hit (1) or Stand (2)")
        if q == "1":
            break
        if q == "2":
            player_hand = 0
            ph_total = 0
            elevens = 0
        elif q == "Q":
            print("Exit through the gift shop")
            sys.exit()
    return player_hand, ph_total, elevens

# Message if run directly
if __name__ == "__main__":
    print("This file contains basic blackjack functions")
    sys.exit()
