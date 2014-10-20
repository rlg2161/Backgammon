# Wrapper program for backgammon GUI, playing methods and AI (to be added later)

import backgammon2 as bg 
import backgammonGUI as bgGUI 
import dice

def main():

  die = dice.oneDie(6)
  gf = bg.goesFirst(die)
  board = bg.board()
  board.initBoard()

  gui = bgGUI.backgammonGUI(board, gf[1], gf[0])
  

  again = play(board, die, gui)
  while(again):
    board.initBoard()
    again = play(board, die, gui)

def play(board, die, gui):
  
  gui.redraw(board)

  #if(len(board.board[2].s) == 1):
    #print "Game over!"

  #again_in = raw_input("Would you like to play again?\nEnter y/Y/yes/Yes for another game:  ")
  
  #if(again_in == "y" or again_in == "Y" or again_in == "yes" or again_in == "Yes"):
    #again = True
  #else:
    #again = False

  return 0 #again
  






if __name__ == "__main__":
  main()