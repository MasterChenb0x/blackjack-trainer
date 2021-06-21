#!/usr/bin/env python3

from Deck import Deck
import time
import random

D1 = Deck(2)
curr_count = 0

for t in range(1,random.randint(1,(52*2))):
    try:
        print(D1.deal())
        time.sleep(3)
    except IndexError:
        break

curr_count = D1.count_status()
check = int(input("What is the count? "))
if curr_count == check:
    print("Congrats!")
else:
    print("Try Harder")
