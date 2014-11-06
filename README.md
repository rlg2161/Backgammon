Backgammon

This repository is a backgammon game I wrote from scratch in Python for practice.

As of now, the game is only playable from the terminal. Plays like a normal game of backgammon 
with error checking of illegal moves. 

Currently, the AI has 2 settings - a random player and a player guided by logic (written by me 
but inspired by http://www.bkgm.com/articles/Berliner/BKG-AProgramThatPlaysBackgammon/). To 
change the type of computer player, can modify the second argument in any of the play turn 
functions in play() in backgammon.py. I have also implemented a simulation mode to test 
strategies against each other. At this point, I only have the two above strategies but intend
to implement more.

Success vs. Random:
My algorithm - 999/1000 wins vs. random computer


Features:
Every before every move (and then after the end of the game to capture the last state), 
the current board, turn and roll values are copied to a state value and added to a linked
list. At the end of the game, the LL is written to lastGameFile.txt so there is a printout
of all moves in the game. Later, I intend to update the game with an undo feature - this
state register will allow the game to be reset to the state of the game one move earlier 
(until the beginning of the game).


Current Issues:
Need to improve move evaluating algorithm
Possible bug in computer not taking final dice move if it will cause it to move off the board
and the previous move was the first to move all pieces into the final quadrant - seems fixed
but want to be aware in case it pops up again

Completed Issues:
Need to fix move generator that calculates all possible moves for the computer
Need to fix move generator/compGenMoves() to avoid infinite loop on doubles - not an infinite
  loop but a recursion overflow. Fixed by pruning repititve states so that there is not an 
  explosion of recursive calls when evaluating a double.
Have to make sure that the "best" move always uses 2 dice if possible in accordance with rules  
  - possibly reasserting itself in above error
