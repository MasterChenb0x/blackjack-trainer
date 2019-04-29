#!/usr/bin/python

# Variable Setup
count = 0 # initial card count
elevens = 0 # counter, for aces counting as 11 in hand

# Simple print format, taking the currant hand, total value, and deck count, currently just a function to allow testing, will probably just be inline
def gui(cards, ph_total, count):
    print(f"Player Hand: {cards}")
    print(f"Current card value: {ph_total}")
    print(f"Current deck count: {count}")
    
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
            global elevens
            elevens += 1
    else:
        sum = int(card)
    return sum

# Returns a count of the card passed to the function. The return should be appended to a running count in the main game.
def hilo_counter(card):
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
