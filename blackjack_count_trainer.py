#!/usr/bin/env python3

from Deck import Deck
import time
import random

D1 = Deck()

while D1:
    print(D1.deal())
    time.sleep(2)
