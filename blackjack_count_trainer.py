#!/usr/bin/env python3

from Deck import Deck
import time
import random

D1 = Deck()

while D1:
    #This loop should only run while there are cards on the deck, but it still throws an IndexError instead of exiting the loop.
    #The break statement works, but is it the best approsch?
    try:
        print(D1.deal())
        time.sleep(2)
    except IndexError:
        break
