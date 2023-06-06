#!/usr/bin/env python3

# We are an import and import company
import sys
import card_functions

# Variable Setup
text_count = "What is the count?"

class BlackJackHAND(card_functions.Hand):
    def __init__(self, name):
        """Creates a hand from card functions, with the added variable of total and eleven."""
        self.total = 0
        self.eleven = 0
        self.count = 0
        super().__init__(name)
    
    def drawCard(self, deck):
        """Draws a card from a deck and then updates the hand total."""
        card = deck.drawCard()
        self.hand.append(card)
        self.valueCounter(card.value)
        self.hiloCounter(card.value)
        return self
    
    def bustCheck(self):
        """Checks if hand total is over 21, meaning the hand is bust and out of the round"""
        if self.total > 21:
            return True
        else:
            return False

    def listState(self):
        """Lists the name and total of the hand."""
        print(f"Play Name: {self.name}")
        self.showHand()
        if self.bustCheck():
                print(f"Current card value: {self.total} BUSTED")
        else:
            print(f"Current card value: {self.total}")
    
    def valueCounter(self, card):
        """Checks the value of the card, and updates the hand's total."""
        if card in ['J', 'Q', 'K']:
            self.total += 10
        elif card == 'A':
            if self.total + 11 > 21:
                self.total += 1
            else:
                self.total += 11
                self.eleven += 1
        else:
            self.total += int(card)
        if self.total > 21 and self.eleven > 0:
            self.total -= 10
            self.eleven -= 1
        return self
    
    def hiloCounter(self, card):
        """Takes the value of the card, and updates the hand's count."""
        try:
            thisCard = int(card)
            if thisCard <= 6:
                self.count += 1
            elif thisCard <= 9:
                self.count += 0
        except:
            if card in ['10', 'J', 'Q', 'K', 'A']:
                self.count += -1
        return self

# Message if run directly
if __name__ == "__main__":
    print("This file contains basic blackjack functions")
    sys.exit()
