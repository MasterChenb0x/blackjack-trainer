#!/usr/bin/env python3

# Import for both function modules, and basic system modules
import blackjack_functions
import card_functions
import time
import sys

# Import and Class to capture the card.show() output to be added to a count log
from io import StringIO 

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

# Basic subclass of BlackJackHand to handle drawing cards and printing a log
class trainerHAND(blackjack_functions.BlackJackHAND):
    def __init__(self, name):
        """Creates a hand from Black Jack functions."""
        super().__init__(name)
        self.log = []
    
    def drawCard(self, deck):
        """Draws a card from a deck and then updates the hand total."""
        card = deck.drawCard()
        self.hand.append(card)
        self.hiloCounter(card.value)
        
        # This part captures the output of the card.show() function, and then both adds it to a log with the current count, and outputs it to the user
        with Capturing() as output:
            card.show()
        self.log.append(output[0] + ' : ' + str(self.count))
        print(output[0])
        return self
    
    def showlog(self):
        for cards in self.log:
            print(cards)

# Takes the user's name, how many decks to use, and how many cards to deal, returns all three as variables
def setup():
    name = input("What is your name? > ")
    decks = card_functions.confirm_integer(card_functions.text_decks)
    cards = card_functions.confirm_integer(card_functions.text_cards)
    deck = card_functions.Deck(decks)
    player = trainerHAND(name)
    return deck, player, cards

# Takes the variables from the setup() function, 
def trainer_deal(deck, player, cards):
    for t in range(cards):
        try:
            player.drawCard(deck)
            time.sleep(3)
        except IndexError:
            break
    while True:
        try:
            check = card_functions.confirm_integer(blackjack_functions.text_count)
            if player.count == check:  
                print("Congrats!")
                break
            else:
                print(f"Try Harder, the count was {player.count}")
                player.showlog()
                    
                break
        except:
            pass

if __name__ == "__main__":
    deck, player, cards = setup()
    trainer_deal(deck, player, cards)
    sys.exit()