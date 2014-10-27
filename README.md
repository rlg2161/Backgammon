Backgammon

This repository is a backgammon game I wrote from scratch in Python for practice.

As of now, the game is only playable from the terminal. Plays like a normal game of backgammon 
with error checking of illegal moves. 

Currently, the AI is extremely rudimentary - it will play a strategy of picking a random, 
valid move for every roll. I intend to add logic to make a rules-based AI, and if possible 
will later implement some sort of forward-looking AI for better computer play. 

Features:
Every before every move (and then after the end of the game to capture the last state), 
the current board, turn and roll values are copied to a state value and added to a linked
list. At the end of the game, the LL is written to lastGameFile.txt so there is a printout
of all moves in the game. Later, I intend to update the game with an undo feature - this
state register will allow the game to be reset to the state of the game one move earlier 
(until the beginning of the game).


Current Issues:

Need to fix move generator that calculates all possible moves for the computer
Need to fix move generator/compGenMoves() to avoid infinite loop on doubles
Have to make sure that the "best" move always uses 2 dice if possible in accordance with rules
Need to fix move evaluating algorithm