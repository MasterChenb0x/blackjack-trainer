#!/usr/bin/env python3

# We are an import and import company
import sys
import random

#### Reference variables
card_pool = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits_pool = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
card_pool = {'Ace' : 'A', 'Two' : '2', 'Three' : '3', 'Four' : '4', 'Five' : '5', 
    'Six' : '6', 'Seven' : '7', 'Eight' : '8', 'Nine' : '9', 'Ten' : '10', 'Jack' : 'J',
    'Queen' : 'Q', 'King' : 'K'}
symbol = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}

# Reference text
text_decks = 'Please enter how many decks to use'
text_cards = 'Please enter how many cards to select'

class Card:
    def __init__(self, name, suit, value) -> None:
        "Generates with a name, suit, and value"
        self.name = name
        self.suit = suit
        self.value = value
    
    def show(self):
        """Prints the name and suit of the card."""
        print(f"{self.name} of {self.suit}")

    def checkSuit(self, suit):
        """Checks the suit of the card."""
        if self.suit == suit:
            return True
        else:
            return False
    
    def checkValue(self, value):
        """Checks the value of the card."""
        if self.value == value:
            return True
        else:
            return False


class Deck:
    def __init__(self, deck_count=1) -> None:
        """Auto runs the build function on creation."""
        self.buildDeck(deck_count)

    def buildDeck(self, deck_count):
        """Creates a minimum of one 52 card deck, and then shuffles."""
        self.cards = []
        for card in card_pool:
            for suit in suits_pool:
                self.cards.append(Card(card, suit, card_pool[card]))
        self.cards = self.cards * deck_count
        self.shuffleDeck()
    
    def shuffleDeck(self):
        """Shuffles the order of the deck."""
        random.shuffle(self.cards)
    
    def showCards(self):
        """Shows the order of the deck."""
        for card in self.cards:
            card.show()
    
    def drawCard(self):
        """Removes and returns the first card in deck"""
        return self.cards.pop()

class Hand:
    def __init__(self, name) -> None:
        """Sets the name of this hand, and an empty hand."""
        self.name =  name
        self.hand = []
    
    def drawCard(self, deck):
        """Draws a card from a deck."""
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        """Shows the current hand."""
        for card in self.hand:
            card.show()
    
    def clearHand(self):
        """Clears the current hand."""
        self.hand = []

    def selectCard(self):
        """
        Used to select a card from the current hand. 
        Currently works, but will just select the first of a card if only a value is given
        On future TODO to resolve that matter.
        """
        while True:
            print("Select a card")
            print("")
            self.showHand()
            selection = input("")
            selection = selection.split(" ")
            for card in self.hand:
                if card.checkValue(selection[0]):
                    try:
                        if card.checkSuit(selection[2]):
                            return card
                    except:
                        return card
            print("Please enter either the entire card or just the value")

def confirm_integer(text):
    """Verifies that a variable is actually an integer"""
    while True:
        number = input(f"{text} > ")
        try:
            number = int(number)
            return number
        except:
            print('Please enter a valid number')

if __name__ == "__main__":
    print('This file contains basic card game functions.')
    sys.exit()
