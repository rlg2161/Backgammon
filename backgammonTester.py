# Wrapper program for backgammon GUI, playing methods and AI (to be added later)

import backgammon as bg 
import backgammonGUI as bgGUI 
import dice

def main():

  die = dice.oneDie(6)
  

  gui = bgGUI.backgammonGUI()
  
  


def playHumanTurn(state):
  
  state.updateRoll(bgGUI.backgammonGUI.rollLabel)
  print state.roll

  #val_moves = state.existValidMoves()
  #if (val_moves == False):


  #space_to_valid = state.checkSpaceTo(int(space_from), int(space_to))
  #print space_to_valid


  #while (winner == -1):
    #roll = die.rollDie()
    #bg.state.updateRoll(roll)
    #bg.state.switchTurn()
    #gui.redraw(state)
    #if (state.turn == 0):
      #playTurn(state, 0, 1)
    #else:
      #playTurn(state, 2, 1)

    #winner = state.testGameOver()  

  #if (state.turn == 0):
    
  #while True:
    #print bgGUI.moves
    #if (state.turn == 0):
      #if (len(bgGUI.moves) == 2):
        #space_to_valid = state.checkSpaceTo(int(bgGUI.moves[0]), int(bgGUI.moves[1]))
        #print space_to_valid
        #bgGUI.moves = []

      #else:
        #continue  



  
  

  #again = play(board, die, gui)
  #while(again):
    #board.initBoard()
    #again = play(board, die, gui)






  #print space_from






if __name__ == "__main__":
  main()