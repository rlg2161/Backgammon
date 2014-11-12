
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
  print ""
  print "0: two people to play each other"
  print "1: human vs. computer"
  print "2: comp vs. comp (strategy testing and simulation)"
  print "3: simulation"
  computer = raw_input("Please make your selection:   ")
  
  good_input = False

  while (good_input != True):
    try:
      if (int(computer) == 1 or int(computer) == 0 or int(computer) == 2 or int(computer) == 3):
        good_input = True
        continue
      else:
        computer = raw_input("Please enter 0 to play against a person or 1 for computer or 2 for 2 computers against eachother:  ")
    except:
      computer = raw_input("Please enter 0 to play against a person or 1 for computer or 2 for 2 computers against eachother:  ")
  
  if (int(computer) < 3):
    again = play(int(computer))

    while(again):
      again = play(int(computer))

  else: 
    num_sims = raw_input("How many games would you like to simulate? ")
    print "What strategies would you like the computer to use? They are, currently: "
    print "1: Random computer player"
    print "2: My own, custom algorithm"
    print "... More to come ..."
    first_strat = raw_input("Choice for comp 1: ")
    second_strat = raw_input("Choice for comp 2: ")

    simulateSession(first_strat, second_strat, num_sims)

def play(num):
  ''' Play a game'''
  
  lastGameFile = open('lastgame.txt', 'wa')

  die = dice.oneDie(6)

  state = createInitialState(die)
  
  winner = -1

  if (num == 0): #Play 2 humans
    #print str(state)
    playTurn(state, 0, 1)
  
    while(winner == -1):
      roll = die.rollDie()
      state.updateRoll(roll)
      state.turn.switchTurn()
      
      playTurn(state, 0, 1)

      winner = state.testGameOver()
      
  if (num == 1): #Play human v. comp
    if (state.turn.turn == 0):
      playTurn(state, 0, 1)
    else:
      playTurn(state, 2, 1)

    while (winner == -1):
      roll = die.rollDie()
      state.updateRoll(roll)
      state.turn.switchTurn()
      if (state.turn.turn == 0):
        playTurn(state, 0, 1)
      else:
        playTurn(state, 2, 1)

      winner = state.testGameOver()

  if (num == 2): #Play comp v. comp
    if (state.turn.turn == 0):
      playTurn(state, 2, 1) #White == Strat
    else:
      playTurn(state, 1, 1) #Black == Random

    while (winner == -1):
      raw_input("wait")
      roll = die.rollDie()
      state.updateRoll(roll)
      state.turn.switchTurn()
      if (state.turn.turn == 0):
        playTurn(state, 2, 1)
      else:
        playTurn(state, 1, 1)

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

def simulateSession(first_strat, second_strat, number_games):
  die = dice.oneDie(6)
  
  white_score = 0
  black_score = 0

  for x in range(0, int(number_games)):
    winner = simulateGame(int(first_strat), int(second_strat), die)
    
    if (winner == 0):
      white_score += 1
    elif(winner == 1):
      black_score += 1

    print "Game " + str(x + 1) + " completed - ",
    if (winner == 0):
      print "White won"
    else:
      print "Black won"
 
  if (white_score > black_score):
    print "White wins"
  else:
    print "Black wins"
 
  print "White's score for this round was: " + str(white_score) + \
  " while playing " + str(first_strat)
  print "Black's score for this round was: " + str(black_score) + \
  " while playing " + str(second_strat)


def simulateGame(first_strat, second_strat, die):
  '''Simulate a game'''

  state = createInitialState(die)
  
  winner = -1

  if (state.turn.turn == 0):
    playTurn(state, first_strat, 0) #White == Strat
  else:
    playTurn(state, second_strat, 0) #Black == Random

  while (winner == -1):
    roll = die.rollDie()
    state.updateRoll(roll)
    state.turn.switchTurn()
    if (state.turn.turn == 0):
      playTurn(state, first_strat, 0)
    else:
      playTurn(state, second_strat, 0)

    winner = state.testGameOver()

  return winner



def playTurn(state, num_flag, print_mode):
  '''Plays one turn'''
  stateList.append(copy.deepcopy(state))
  if (num_flag == 0 or num_flag == 1):
    val_moves = state.existValidMoves()

    if (val_moves == False):
      #stateList.append(copy.deepcopy(state))
      if (print_mode):
        print "No valid moves"
        state.printState()


    while (val_moves == True):
      #stateList.append(copy.deepcopy(state))
      if (print_mode):
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
          if (print_mode):
            state.printError(space_to_valid[3])

        
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

      #print state.roll
      state.roll.remove(move_dist)
      #print state.roll
      state.updatePipCount()

      val_moves = state.existValidMoves()
      #print val_moves

    if (print_mode):
      state.printState()

    #stateList.append(copy.deepcopy(state))
    
  else:
    if (print_mode):
      state.printState()

    new_state = playStrategicCompTurn(state)
    
    if (print_mode):
      new_state.printState()

    #stateList.append(new_state)
    state.updateFromState(new_state)

def genAllPossMoves(posStates):
  '''Recursively generate all possible moves given a game-state'''
  if (len(posStates) > 1000):
    print "Runaway recursion :( - game exited"
    exit(1)
  state = posStates[0]

  if (len(state.roll) == 0 or state.existValidMoves() == False):
    return 

  else:
    if (state.pieceInJail() == True):
      #print "piece in jail"
      
      for x in range(0, len(state.roll)):
        cpy_state = copy.deepcopy(state)
        if (state.turn.turn == 0): #White
          space_to_valid = cpy_state.checkSpaceTo(26, 25- cpy_state.roll[x])
        else: # Black
          space_to_valid = cpy_state.checkSpaceTo(27, cpy_state.roll[x])
        if (space_to_valid[0] == True):
          space_from = space_to_valid[1]
          space_to = space_to_valid[2]
          move_dist = space_to_valid[3]

          # Execute move
          move_piece = cpy_state.board.spaceList[space_from].s.pop()

          #Check if the current space is now empty - if so and not a jail space, update color
          if (isinstance(cpy_state.board.spaceList[space_from], space.jailSpace) == False):
            if (len(cpy_state.board.spaceList[space_from]) == 0):
              cpy_state.board.spaceList[space_from].updateColor(-1)

          # Capture opponent piece and put it in jail
          if (cpy_state.board.spaceList[space_to].getColor() != cpy_state.turn.turn):
            if (len(cpy_state.board.spaceList[space_to]) == 1):
              cap_piece = cpy_state.board.spaceList[space_to].s.pop()
              if (cpy_state.turn.turn == 0): # WHITE
                cpy_state.board.spaceList[27].s.append(cap_piece)
              else: #BLACK
                cpy_state.board.spaceList[26].s.append(cap_piece)

          cpy_state.board.spaceList[space_to].s.append(move_piece)
          cpy_state.board.spaceList[space_to].updateColor(state.turn.turn)
          cpy_state.roll.remove(cpy_state.roll[x])
          cpy_state.updatePipCount()

          if (compareStateToList(cpy_state, posStates) != True):
            posStates.append(cpy_state)
          #cpy_state.printState()

      posStates.remove(state)
      genAllPossMoves(posStates)

    else:
      #print "nobody in jail"
      for x in range(0, 25):
        #print x
        
        cur_space = state.board.spaceList[x]
        
        if (cur_space.getColor() != state.turn.turn):
          continue

        else: 
          for y in range(0, len(state.roll)):
            cpy_state = copy.deepcopy(state)
            if (state.turn.turn == 0): #White
              space_to_valid = cpy_state.checkSpaceTo(x, x - state.roll[y])
            else: #Black
              space_to_valid = cpy_state.checkSpaceTo(x, x + state.roll[y])
            #print space_to_valid
            if (space_to_valid[0] == True):
              #print "Exist valid move?"
              space_from = space_to_valid[1]
              space_to = space_to_valid[2]
              move_dist = space_to_valid[3]

              # Execute move
              move_piece = cpy_state.board.spaceList[space_from].s.pop()

              #Check if the current space is now empty - if so and not a jail space, update color
              if (isinstance(cpy_state.board.spaceList[space_from], space.jailSpace) == False):
                if (len(cpy_state.board.spaceList[space_from]) == 0):
                  cpy_state.board.spaceList[space_from].updateColor(-1)

              # Capture opponent piece and put it in jail
              if (cpy_state.board.spaceList[space_to].getColor() != cpy_state.turn.turn):
                if (len(cpy_state.board.spaceList[space_to]) == 1):
                  cap_piece = cpy_state.board.spaceList[space_to].s.pop()
                  if (cpy_state.turn.turn == 0): # WHITE
                    cpy_state.board.spaceList[27].s.append(cap_piece)
                  else: #BLACK
                    cpy_state.board.spaceList[26].s.append(cap_piece)

              cpy_state.board.spaceList[space_to].s.append(move_piece)
              cpy_state.board.spaceList[space_to].updateColor(state.turn.turn)
              cpy_state.roll.remove(cpy_state.roll[y])
              cpy_state.updatePipCount()

              if (compareStateToList(cpy_state, posStates) != True):
                posStates.append(cpy_state)
              #cpy_state.printState()
          
      posStates.remove(state)
      genAllPossMoves(posStates)

def compareStateToList(state, stateList):
  '''Compare state to list of states to determine if it is already in the list'''
  alreadyInList = False
  
  for item in stateList:
    if (state.compareStates(item) == True):
      alreadyInList = True
      break

  return alreadyInList

def elimInvalidMoves(stateList):
  roll_count = 4

  for state in stateList:

    temp = len(state.roll)
    if (temp <= roll_count):
      roll_count = temp
    else:
      stateList.remove(state)


def evalMoves(posStates):
  '''Evaluate all moves in a list and return move with the highest score'''
  cur_max = -1000000
  best_move = []

  elimInvalidMoves(posStates)

  for x in range(0, len(posStates)):

    temp = calcMoveValue(posStates[x])
    #print temp

    if (temp > cur_max):
      # If temp move better than current best, remove current best and store temp
      cur_max = temp
      best_move = []
      best_move.append(posStates[x])

    elif (temp == cur_max):
      # If temp is equal to current best, store both moves and decide which one later
      best_move.append(posStates[x])

  #print "Best Move Value: " + str(cur_max)
  
  if (len(best_move) == 1):
    best = best_move[0]
  else:
    test = random.random()*len(best_move)
    best = best_move[int(math.floor(test))]

  return best

def calcMoveValue(state):
  '''Calculate the value of a move for a strategy-based computer to determine best move'''
  uncovered_score = 0
  opp_jail_score = 0
  blocade_score = 0
  blocade_count = 0
  covered_score = 0

  temp = state.lastOccupiedSpace()
  last_white_space = temp[0]
  last_black_space = temp[1]
  

  # Only count once
  if (state.turn.turn == 0):
      # Points for opp pieces in jail
      opp_jail_score = 8*(len(state.board.spaceList[27]))
      # Points for scoring pieces
      points_scored = 4*len(state.board.spaceList[25])
  else:
    opp_jail_score = 8*(len(state.board.spaceList[26]))
    points_scored = 4*len(state.board.spaceList[0])


  for x in range(0, 25):
    cur_space = state.board.spaceList[x]
    
    if (cur_space.getColor() != state.turn.turn):
      blocade_count = 0
      continue

    else:
      # Points for uncovered pieces
      if (len(cur_space) == 1):
        blot_points = 0
        blocade_count = 0
        if (state.turn.turn == 0): #White
          if (x > last_black_space): 
            blot_points = 5 * ((25-x)*.125)
        elif (state.turn.turn == 1): #Black
          if (x < last_white_space):
            blot_points = 5*((x)*.125)
        
        uncovered_score = uncovered_score + blot_points

      # Points for blocades
      if (len(cur_space) >= 2):
        covered_score += 1
        blocade_count += 1
        if (blocade_count > 1):
          blocade_score += blocade_count*2

  #print "points scored: " + str(points_scored) + " opponent jail score: " + str(opp_jail_score) \
  #+ " blocade score: " + str(blocade_score) + \
  #" covered score: " + str(covered_score) + " Uncovered score: -" + str(uncovered_score)
  #state.printState()
  move_value = points_scored + opp_jail_score + blocade_score + covered_score - uncovered_score
  return move_value
  
def playStrategicCompTurn(state):
  '''Plays a computer turn if a non-random strategy is being played'''
  posStates = [state]
  genAllPossMoves(posStates)
  best = evalMoves(posStates)
  return best
  
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
      if (state.furthestFromHome() <= test):
        # If largest roll is greater than or equal to distance from home of farthest piece
        if (state.turn.turn == 0):
          space_from = state.furthestFromHome()
        else:
          space_from = 25 - state.furthestFromHome()
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
  '''Returns the comps selected space plus the largest remaining dice roll'''
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
      space_to = space_from + test
    
    else:
      # If all pieces in final quadrant 
      space_to = space_from + test
      if (space_to > 25):
        space_to = 25
      
  
  elif (state.turn.turn == 0):
    if (space_from == 26 + state.turn.turn):
      # If comp is in jail
      space_to = 25-test

    elif (state.allInFinalQuadrant() == False):
      # Comp not in jail && not all in final quadrant
      space_to = space_from - test

    else:
      # If all pieces in final quadrant 
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
  '''Create initial game state given a die object'''
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