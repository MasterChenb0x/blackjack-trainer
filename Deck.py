#!/usr/bin/env python3

import random

class Deck:
    def __init__(self):
        self.cards = {}
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

        for r in self.ranks:
            self.cards[r] = {'suits': ['diamonds', 'clubs', 'hearts', 'spades']
            }
            if r in ['2', '3', '4', '5', '6']:
                self.cards[r]['count_val'] = 1
                self.cards[r]['num_val'] = int(r)
            if r in ['7', '8', '9']:
                self.cards[r]['count_val'] = 0
                self.cards[r]['num_val'] = int(r)
            if r in ['10', 'jack', 'queen', 'king']:
                self.cards[r]['count_val'] = -1
                self.cards[r]['num_val'] = 10
            if r in ['ace']:
                self.cards[r]['count_val'] = -1
                self.cards[r]['num_val'] = [1, 11]

    def deal(self):
        cards = list(self.cards.items())
        return random.choice(cards)

new_deck = Deck()
print(new_deck.cards)
print(new_deck.deal())
