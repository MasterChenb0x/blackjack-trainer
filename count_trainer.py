#!/usr/bin/env python3

import blackjack_functions
import time
import random

class trainerHAND(blackjack_functions.BlackJackHAND):
    def __init__(self, name):
        """Creates a hand from Black Jack functions."""
        super().__init__(name)
    
    def drawCard(self, deck):
        """Draws a card from a deck and then updates the hand total."""
        card = deck.drawCard()
        self.hand.append(card)
        self.hiloCounter(card.value)
        card.show()
        return self

deck = blackjack_functions.card_functions.Deck(2)
player = trainerHAND(input("What is your name? > "))

random_cards = random.randint(1, len(deck.cards))
for t in range(random_cards):
    try:
        player.drawCard(deck)
        time.sleep(3)
    except IndexError:
        break

while True:
    try:
        check = int(input("What is the count? "))
        if player.count == check:  
            print("Congrats!")
            break
        else:
            print("Try Harder")
            break
    except:
        pass
