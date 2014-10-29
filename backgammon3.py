
import dice
import space
import board
import state
import turn

stateList = []

def main():
  
  

  again = play(0)

  while(again):
    again = play(0)

def play(num):
  ''' Play a game'''
  
  lastGameFile = open('lastgame.txt', 'wa')

  die = dice.oneDie(6)

  state = createInitialState(die)
  
  winner = -1

  if (num == 0): #Play 2 humans
    #print str(state)
    playTurn(state, True)
  
    while(winner == -1):
      roll = die.rollDie()
      state.updateRoll(roll)
      state.turn.switchTurn()
      
      playTurn(state, True)

      winner = state.testGameOver()
      

    state.printState()
    stateList.append(state)

  if (winner == 0):
    print "Player One ('o') was the winner."
  else:
    print "Player Two ('x') was the winner."

  again_in = raw_input("Would you like to play again?\nEnter y/Y/yes/Yes for another game:  ")
  if(again_in == "y" or again_in == "Y" or again_in == "yes" or again_in == "Yes"):
    again = True
  else:
    again = False

  
  return again

def playTurn(state, bool_flag):
  
  val_moves = state.existValidMoves()

  if (val_moves == False):
    stateList.append(state)
    print "No valid moves exist - next player's turn"
    state.printState()


  while (val_moves == True):
    stateList.append(state)
    state.printState()

    valid_move = False

    if (bool_flag == True):
      while (valid_move == False):
        # Generate player moves and check if they are valid
        space_to_valid = playHumanTurn(state)
        valid_move = space_to_valid[0]
        if (valid_move != True):
          # If invalid, print relevant error
          state.printError(space_to_valid[3])
        else:
          #assign valid move values to actual move varialbes
          space_from = space_to_valid[1]
          space_to = space_to_valid[2]
          move_dist = space_to_valid[3]

          # Execute move
          move_piece = state.board.spaceList[space_from].s.pop()

          #Check if the current space is now empty - if so and not a jail space, update color
          if (isinstance(state.board.spaceList[space_from], space.jailSpace) == False):
            if (len(state.board.spaceList[space_from]) == 0):
              state.board.spaceList[space_from].updateColor(-1)

          # Capture opponent piece and put it in jail
          if (state.board.spaceList[space_to].getColor() != state.turn.turn):
            if (len(state.board.spaceList[space_to]) == 1):
              cap_piece = state.board.spaceList[space_to].s.pop()
              if (state.turn.turn == 0): # WHITE
                state.board.spaceList[27].s.append(cap_piece)
              else: #BLACK
                state.board.spaceList[26].s.append(cap_piece)

          state.board.spaceList[space_to].s.append(move_piece)
          state.board.spaceList[space_to].updateColor(state.turn.turn)

          state.roll.remove(move_dist)

      val_moves = state.existValidMoves()
      #state.printState()      
  
    else: #Comp turn
      print "not implemented yet"

def playHumanTurn(state):
   '''Receive move from human and check its validity'''
   space_from = getSpaceFrom(state)
   space_to = getSpaceTo()
   space_to_valid = state.checkSpaceTo(space_from, space_to)

   return space_to_valid

def getSpaceFrom(state):
  '''Get space from user'''
  if (len(state.board.spaceList[26 + state.turn.turn]) > 0):
    print "You must move your piece from Jail"
    space_from = (26 + state.turn.turn)

  else:
    move_from = False
    while (move_from == False):
      space_from = raw_input("Please input the space you would like to move from: ")
      try:
        space_from = int(space_from)
      except:
        print "That was not a valid input."

      if (space_from < 27 and space_from >= 0):
        space_color = state.board.spaceList[space_from].getColor()
        if (space_color == state.turn.turn):
          move_from = True

  return space_from

def getSpaceTo():
  '''Get space to move to from user'''
  again = True
  while (again):
    space_to = raw_input("Please input the space you would like to move to: ")
    try:
      space_to = int(space_to)
      again = False
    except:
      print "That was not a valid input."
  
  return space_to



def createInitialState(die):
  
  b = board.board()
  b.initBoard()
  
  gf = die.goesFirst()

  t = gf[0]
  r = gf[1]

  #print t

  st = state.state(b, t, r)

  return st

if __name__ == "__main__":
  main()