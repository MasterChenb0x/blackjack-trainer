#!/usr/bin/env python3

import random

class Deck:
    def __init__(self, decks=1):
        self.decks = decks
        self.count = 0
        self.cards = {}
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        self.last_card = {}

        for r in self.ranks:
            self.cards[r] = {'suits': ['diamonds', 'clubs', 'hearts', 'spades'] * self.decks}
            self.cards[r]['remaining'] = len(self.cards[r]['suits'])
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
        card = random.choice(cards)
        suit = random.choice(card[1]['suits'])
        card[1]['suits'].remove(suit)
        card[1]['remaining'] -= 1
        if card[1]['suits'] == []:
            del self.cards[card[0]]
        self.count += card[1]['count_val']
        self.last_card = card
        return f'{card[0]} of {suit}'

    def count_status(self):
        return self.count

if __name__ == "__main__":
    print("This is just a deck of cards")
    D1 = Deck()
    print(D1.cards)
    print(D1.deal())
    print(D1.deal())
    print(D1.deal())
    print(D1.last_card)
    print(D1.cards)
