#!/usr/bin/env python3

import random

class Deck:

    def __init__(self):
        self.count = 0
        self.cards = {
                diamonds: [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
                clubs: [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
                hearts: [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
                spades: [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
                }

