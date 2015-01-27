Backgammon

This repository is a backgammon game I wrote from scratch in Python for practice.

As of now, the game is playable in the terminal with all features accessible or in a GUI
which is permanently in mode 1 - Human is White Player and Computer is Black Player playing
strategy 2.

Currently, the AI has 3 settings - a random player, and a player guided by logic (written by me 
but inspired by http://www.bkgm.com/articles/Berliner/BKG-AProgramThatPlaysBackgammon/), and
a player that was trained using basic machine learning concepts to generate a linear equation
to govern computer strategy. At this time, all strategies are fuctional, but none is a 
particularly strong player. 

There is also a fourth strategy that remains in the code but is not accessible via the normal
program loop - it is an attempt to look forward an calculate the best move based on what will
be the worst move for the opponent. This move strategy calculation can be found in the function
moveWithStateTree(). Although the methods work (i.e. the recursive generation of all states to
a pre-determined level [in this case 2]), they are both really slow and do not generate a 
viable/functional strategy for the computer player. As such, I left the methods in the program 
in case they ever need to be used again but they currently are not used to generate a playing 
strategy.

To play the game, simply run backgammon.py. A menu will pop up in the terminal - all of the play
modes are self explanitory. Option 7 opens the GUI for play against the computer as described 
above. 

Option 3 allows for simulation of various computer strategies against one another
Option 4 runs a set of simulations as specified by the user to generate a set of statistics
that are then used in Option 5 (basic learning using the normal equation to calculate an 
optimal set of weights for the linear equation governing computer move strategy).
Option 6 plots the movement of the values of the linear equation plotted in Option 5. 


Success vs. Random:

My algorithm (strat 2) - 979/1000 wins vs. random computer



Features:

Before every move (and then after the end of the game to capture the last state), 
the current board, turn and roll values are copied to a state value and added to a linked
list. At the end of the game, the LL is written to lastGameFile.txt so there is a printout
of all moves in the game. Later, I intend to update the game with an undo feature - this
state register will allow the game to be reset to the state of the game one move earlier 
(until the beginning of the game).




Going forward:

I am looking to use a neural net to calculate a non-linear strategy for the computer player 
to allow it to improve its level of play. I am intending to set up the inital neural net 
in the exact manner as Tesauro's neural net that is the basis for TD-gammon. Once I can get
that to work, I will experiment with the NN to see if I can produce a better result if I can
calibrate the neural net in a different manner.




Completed Issues:

Need to fix move generator that calculates all possible moves for the computer


Need to fix move generator/compGenMoves() to avoid infinite loop on doubles - not an infinite
  loop but a recursion overflow. Fixed by pruning repititve states so that there is not an 
  explosion of recursive calls when evaluating a double.


Have to make sure that the "best" move always uses 2 dice if possible in accordance with rules  
  - possibly reasserting itself in above error


Possible bug in computer not taking final dice move if it will cause it to move off the board
and the previous move was the first to move all pieces into the final quadrant 
  - seems fixed but want to be aware in case it pops up again
