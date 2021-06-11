#!/usr/bin/env python3

from Deck import Deck
import time
import random

D1 = Deck()

while D1:
    try:
        print(D1.deal())
    except IndexError:
        print(D1.deal())
    time.sleep(2)
