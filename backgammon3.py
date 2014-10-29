
import dice
import space
import board
import state
import turn
import copy
import math
import random

stateList = []

def main():
  
  print "Would you like to play against another person or the computer?"
  computer = raw_input("Enter 0 for human or 1 for computer or 2 for 2 computers against eachother:  ")
  
  good_input = False

  while (good_input != True):
    try:
      if (int(computer) == 1 or int(computer) == 0 or int(computer) == 2):
        good_input = True
        continue
      else:
        computer = raw_input("Please enter 0 to play against a person or 1 for computer or 2 for 2 computers against eachother:  ")
    except:
      computer = raw_input("Please enter 0 to play against a person or 1 for computer or 2 for 2 computers against eachother:  ")
  
  again = play(int(computer))

  while(again):
    again = play(int(computer))

def play(num):
  ''' Play a game'''
  
  lastGameFile = open('lastgame.txt', 'wa')

  die = dice.oneDie(6)

  state = createInitialState(die)
  
  winner = -1

  if (num == 0): #Play 2 humans
    #print str(state)
    playTurn(state, 0)
  
    while(winner == -1):
      roll = die.rollDie()
      state.updateRoll(roll)
      state.turn.switchTurn()
      
      playTurn(state, 0)

      winner = state.testGameOver()
      
  if (num == 1): #Play human v. comp
    playTurn(state, state.turn.turn)

    while (winner == -1):
      roll = die.rollDie()
      state.updateRoll(roll)
      state.turn.switchTurn()

      playTurn(state, state.turn.turn)

      winner = state.testGameOver()

  if (num == 2): #Play comp v. comp
    playTurn(state, 1)

    while (winner == -1):
      roll = die.rollDie()
      state.updateRoll(roll)
      state.turn.switchTurn()

      playTurn(state, 1)

      winner = state.testGameOver() 
  

  state.printState()
  stateList.append(copy.deepcopy(state))
  
  stateList.reverse()
  while(len(stateList) > 0):
    lastGameFile.write(str(stateList.pop()))
  lastGameFile.close()

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

def playTurn(state, num_flag):
  
  val_moves = state.existValidMoves()

  if (val_moves == False):
    stateList.append(copy.deepcopy(state))
    print "No valid moves exist - next player's turn"
    state.printState()


  while (val_moves == True):
    stateList.append(copy.deepcopy(state))
    state.printState()

    valid_move = False

    
    while (valid_move == False):
      # Generate player moves and check if they are valid
      if (num_flag == 0): #Human Player
        space_to_valid = playHumanTurn(state)
      elif (num_flag == 1): #Random computer player 
        space_to_valid = playRandCompTurn(state)
      valid_move = space_to_valid[0]
      
      if (valid_move != True and state.turn.turn == 0):
        # If invalid, print relevant error
        state.printError(space_to_valid[3])

      
    #assign valid move values to actual move varialbes
    print space_to_valid
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

    #print state.roll
    state.roll.remove(move_dist)
    #print state.roll
    state.updatePipCount()

    val_moves = state.existValidMoves()
    #print val_moves
          
  
def playRandCompTurn(state):
  '''Calculate and return a valid, random Computer move'''
  space_from = getCompSpaceFrom(state)
  space_to = getCompSpaceTo(state, space_from)
  space_to_valid = state.checkSpaceTo(space_from, space_to)

  return space_to_valid

def getCompSpaceFrom(state):
  '''Get space_from for computer player'''
  if (len(state.board.spaceList[26 + state.turn.turn]) > 0):
    #print "Computer must move piece from Jail. "
    space_from = 26 + state.turn.turn
    return space_from

  else:
    roll_copy = copy.deepcopy(state.roll)
    roll_copy.sort()
    test = roll_copy.pop()
    if (state.allInFinalQuadrant()):
      #All pieces in final quadrant
      if (state.lastOccupiedSpace() <= test):
        # If largest roll is greater than or equal to distance from home of farthest piece
        if (state.turn.turn == 0):
          space_from = state.lastOccupiedSpace()
        else:
          space_from = 25 - state.lastOccupiedSpace()
      else:
        #If largest roll is smaller than furthest away piece
        move_from = False
        while(move_from == False):
          test_space = int(math.floor(random.random()*24) + 1)
          if (state.board.spaceList[test_space].getColor() == state.turn.turn):
            move_from = True
            space_from = test_space
    else:
      # No pieces in jail and not all in final quadrant
      move_from = False
      while(move_from == False):
        test_space = int(math.floor(random.random()*24) + 1)
        if (state.board.spaceList[test_space].getColor() == state.turn.turn):
          move_from = True
          space_from = test_space
 
    return space_from

def getCompSpaceTo(state, space_from):
  ''' Return's the comps select space plus the largest remaining dice roll'''
  rollcpy = copy.deepcopy(state.roll)
  
  if (random.random() > .5):
    # Check the higher or lower value 50% of time - allows both high and low rolls to be
    # checked by comp
    rollcpy.reverse()
  
  test = rollcpy.pop()

  if (state.turn.turn == 1):
    if (space_from == 26 + state.turn.turn):
      # If comp is in jail
            
      space_to = test
    

    elif (state.allInFinalQuadrant() == False):
      # Comp not in jail && not all in final quadrant
      #test = rollcpy.pop()
      space_to = space_from + test
    
    else:
      # If all pieces in final quadrant 
      #test = rollcpy.pop()
      space_to = space_from + test
      if (space_to > 25):
        space_to = 25
      
  
  elif (state.turn.turn == 0):
    if (space_from == 26 + state.turn.turn):
      # If comp is in jail
      if (random.random() > .5):
        rollcpy.reverse()
      #test = rollcpy.pop()
      space_to = 25-test

    elif (state.allInFinalQuadrant() == False):
      # Comp not in jail && not all in final quadrant
      #test = rollcpy.pop()
      space_to = space_from - test

    else:
      # If all pieces in final quadrant 
      #test = rollcpy.pop()
      space_to = space_from - test
      if (space_to < 0):
        space_to = 0

  return space_to

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