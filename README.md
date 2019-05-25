blackjack-trainer
==============

by MasterChen @chenb0x
----------------------

#### DISCLAIMER: It is NOT ILLEGAL to count cards on a table in Las Vegas, HOWEVER, it IS illegal to use an apparatus outside of your own mind (devices, etc) while at a table. Please use discretion and understand that this is a mental exercise.


###### This is a BlackJack trainer. It trains the user on how to count cards using the High/Low or Revere(Plus/Minus) method of counting

###### This is not designed for use at a Vegas table, but rather to prepare your mind before going to a table.

### 04/04/2017
Added a check for going over 21 (busting)
Attempted to turn most of the game section into a function, but got tripped up over local vs global variable (I should know this). Will attempt again when I know exactly what I wnat/need to make local. 
Increased PlayerHand array to 7 card total.

### 04/03/2017
Changed how a player indicates Hit/Stand, and Deal/NoDeal.
Fully implemented the PlayerHand array/list during the game.

Need to work on ending game when player "busts".

### 11/15/2016
Added a way to increment the PLayerHand array. Not much use now, but will help when the player wants to hit more than once. With taht said, the next step is to change the "if total < 21" clause to a loop...without breaking anything...
Should also handle a "Bust" scenario in the near future.

### 11/07/2016
Created an initialization function to maybe save a few lines of code? Declared variables in function as globals which seemed to resolve the initialization breakage before. 

### 11/06/2016
Started working on the Hit or Stand functionality, but there is a lot of work to be done. The program, so far, can add one more card when a "Hit" is requested.
This brings us to adding parameters when a "Bust" happens.
Changed card variables into an array for better organization and manipulation.

### 11/05/2016
Moved the ace checker so the user can know the had before decidibg on 1 or 11.

### 11/04/2016
Revisited code and tried to condense. Still working on it. 
Fixed most major breaks, but will need to clean that up a bit too with Exception handlers.
Separated setup functions for better organization. Setup is now in bjsetup.py
Added ace card handling and printed a total sum.

###### To Do

### 04/04/2017
1. Attempt to functionalize the main secion of the game since it gets called more than once.
2. Now that the PlayerHand mechanics are figured out, need to start Dealer functionality so the player gets a sense of winning against an opponent.
3. Betting functionality
4. More verbose output for count training (this includes true and running counts).
