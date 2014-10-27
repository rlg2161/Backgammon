# A basic backgammon game that interfaces with console

import dice
import math
import copy
import random


WHITE = 0
BLACK = 1
stateList = [] # keeps track of every move and remaining dice at that time
               # creates a LL of game states for undo's

hflag = True
cflag = False
roll_dict = {1 : float(11)/36, 2: float(12)/36, 3: float(13)/36, 4: float(14)/36,\
            5: float(15)/36, 6: float(16)/36, 7: float(6)/36, 8: float(5)/36, \
            9: float(4)/36, 10 : float(3)/36, 11: float(2)/36, 12 : float(1)/36}
            #Dictionary with roll probabilites

class piece():
  '''Represents a board piece'''

  def __init__(self, color):
    if (color):
      self.color = BLACK
    else:
      self.color = WHITE

  def __str__(self):
    if (self.color):
      return 'x'
    else:
      return 'o'

class space():
  '''Object represents a space on the board'''

  def __init__(self):
    self.s = []
    self.color = -1

  def updateColor(self, color):
    self.color = color

  def getColor(self):
    return self.color

  def peek(self):
    temp = self.s.pop()
    piece = temp
    self.s.append(temp) 
    return piece

  def fillSpace(self, color, number):
    for x in range (0, number):
      p = piece(color)
      self.s.append(p)
    self.updateColor(color)

class jailSpace(space):
  '''Represents a jail space'''

  def __init__(self,col):
    self.s = []
    self.color = col

  def getMoveFrom(self):
    c = self.color
    if (c == WHITE):
      return 25
    elif (c == BLACK):
      return 0

class board():
  '''Represents the board'''

  def __init__(self):
    self.board = []
    for x in range(0,26):
      s = space()
      self.board.append(s)
    js = jailSpace(WHITE)
    self.board.append(js)
    js = jailSpace(BLACK)
    self.board.append(js)

  def updateFromState(self, state):
    self.board = copy.deepcopy(state.board.board)
    #self.board.printBoard()



  def initBoard(self):
    
    # NORMAL SETUP IN BELOW BLOCK

    self.board[1].fillSpace(1, 2)
    self.board[6].fillSpace(0, 5)
    self.board[8].fillSpace(0, 3)
    self.board[12].fillSpace(1, 5)
    self.board[13].fillSpace(0, 5)
    self.board[17].fillSpace(1, 3)
    self.board[19].fillSpace(1, 5)
    self.board[24].fillSpace(0, 2)

    #Board configuration for testing endgame
    #self.board[0].fillSpace(0,2)
    #self.board[1].fillSpace(0,2)
    #self.board[2].fillSpace(0,2)
    #self.board[3].fillSpace(0,2)
    #self.board[4].fillSpace(0,3)
    #self.board[5].fillSpace(0,3)
    #self.board[6].fillSpace(0,3)
    #self.board[7].fillSpace(0,2)
    #self.board[8].fillSpace(0,2)
    #self.board[9].fillSpace(0,2)
    #self.board[10].fillSpace(0,3)
    #self.board[11].fillSpace(0,3)
    #self.board[12].fillSpace(0,3)
    #self.board[19].fillSpace(1,3)
    #self.board[20].fillSpace(1,3)
    #self.board[21].fillSpace(1,3)
    #self.board[22].fillSpace(1,2)
    #self.board[23].fillSpace(1,2)
    #self.board[24].fillSpace(1,2)
    #self.board[25].fillSpace(1, 15)
    #self.board[26].fillSpace(0, 3)
    #self.board[27].fillSpace(1,3)


  def getScore(self):
    w_score = len(self.board[0].s)
    b_score = len(self.board[25].s)
    return (w_score, b_score)

  def printBoard(self):
    for x in range(0, len(self.board)):
      cur_space = self.board[x]
      if (x == 0):
        print "White Points Scored: ",
        for y in range(0, len(cur_space.s)):
          print cur_space.s[y],
        print ""
      elif (x > 0 and x < 25):
        print str(x) + ": ",
        for y in range(0, len(cur_space.s)):
          print cur_space.s[y],
        #print "    " + str(cur_space.color),
        print ""
      elif (x == 25):
        print "Black Points Scored: ",
        for y in range(0, len(cur_space.s)):
          print cur_space.s[y],
        print ""
        print ""
      elif (x == 26):
        print "White Jail: ",
        for y in range(0, len(cur_space.s)):
          print cur_space.s[y],
        #print "    " + str(cur_space.color),
        print ""
      else:
        print "Black Jail: ",
        for y in range(0, len(cur_space.s)):
          print cur_space.s[y],
        #print "    " + str(cur_space.color),
        print ""
    print "" 

  def __str__(self):
    return_string = " "
    
    for x in range(0, len(self.board)):
      cur_space = self.board[x]
      if (x == 0):
        #print type(return_string)
        return_string = return_string + "White Points Scored: "
        #print type(return_string)
        #print return_string
        for y in range(0, len(cur_space.s)):
          return_string = return_string + str(cur_space.s[y])
        return_string = return_string + "\n"
      elif (x > 0 and x < 25):
        return_string = return_string + str(x) + ": "
        for y in range(0, len(cur_space.s)):
          #print ""
          return_string = return_string + str(cur_space.s[y])
        #print "    " + str(cur_space.color),
        return_string = return_string + "\n"
      elif (x == 25):
        return_string = return_string + "Black Points Scored: "
        for y in range(0, len(cur_space.s)):
          #print ""
          return_string = return_string + str(cur_space.s[y])
        return_string = return_string + "\n "
        return_string = return_string + "\n "
      elif (x == 26):
        return_string = return_string + "White Jail: "
        for y in range(0, len(cur_space.s)):
          #print ""
          return_string = return_string + str(cur_space.s[y])
        #print "    " + str(cur_space.color),
        return_string = return_string + "\n "
      else:
        return_string = return_string + "Black Jail: "
        for y in range(0, len(cur_space.s)):
          #print ""
          return_string = return_string + str(cur_space.s[y])
        #print "    " + str(cur_space.color),
        return_string = return_string + "\n "
    return_string = return_string + "\n "

    return return_string

class state(): 

  def __init__(self, board, turn, roll):
    self.board = copy.deepcopy(board)
    self.turn = copy.copy(turn)
    self.roll = list(roll)
    self.pip_count = getPipCount(self.board)

  def printState(self):
    if (self.turn == 0):
      print "White's Turn"
    else:
      print "Black's Turn"

    print self.roll
    print " " 
    print "White pip count: " + str(self.pip_count[0]),
    print "Black pip count: " + str(self.pip_count[1])
    self.board.printBoard()

  def __str__(self):
    return_string = ''
    
    if (self.turn == 0):
      return_string = return_string + "White's Turn"
    else:
      return_string = return_string + "Black's Turn"

    return_string = return_string + str(self.roll) + "\n"
    return_string = return_string + "White pip count: " + str(self.pip_count[0])
    return_string = return_string + "Black pip count: " + str(self.pip_count[1])
    return_string = return_string + "\n" 
    return_string = return_string + str(self.board)

    return return_string

#class stateMove():
  
  #def __init__(self, state):
    #self.state = state
    #self.move_list = []

  #def addMove(self, move_tuple):
    #self.move_list.append(move_tuple)



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

def play(comp):
  '''Play a game'''
  lastGameFile = open('lastgame.txt', 'wa')

  b = board()
  b.initBoard()
  die = dice.oneDie(6)

  gf = goesFirst(die)
  turn = gf[0]
  roll = gf[1]

  winner = -1

  if (comp == 0): # Play 2 humans
  
    printTurn(turn)
    turn = playTurn(b, roll, turn, hflag)
    
    while(winner == -1):
      printTurn(turn)
      roll = rollDie(die)
      turn = playTurn(b, roll, turn, hflag, )
      winner = testGameOver(b)

    lastState = state(b, turn, roll)
    lastState.printState()
    stateList.append(lastState)
    
    
  elif (comp == 1): #Play against a computer
    # Human player is always white
    printTurn(turn)

    if (turn == 0):
      turn = playTurn(b, roll, turn, hflag)

    else:
      turn = playTurn(b, roll, turn, cflag)

    while(winner == -1):
      printTurn(turn)
      roll = rollDie(die)
      
      if (turn == 0):
        turn = playTurn(b, roll, turn, hflag)
      else:
        turn = playTurn(b, roll, turn, cflag)

      winner = testGameOver(b)

    lastState = state(b, turn, roll)
    lastState.printState()
    stateList.append(lastState)

  else: # play 2 computers
    printTurn(turn)
    turn = playTurn(b, roll, turn, cflag)

    while(winner == -1):
      printTurn(turn)
      roll = rollDie(die)
      turn = playTurn(b, roll, turn, cflag)
      winner = testGameOver(b)

    lastState = state(b, turn, roll)
    lastState.printState()
    stateList.append(lastState)
  

  stateList.reverse()
  while (len(stateList) > 0):
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

def pieceInJail(b, turn): 

  if (len(b.board[26+turn].s) > 0):
    return True
  else:
    return False
  
def compGenMoves(st):

  state_list = [st]
    
  genPosMoves(state_list[0], state_list)
  #roll = state_list[0].roll

  #while (len(roll) > 0):
  #NEED TO FIX FOR DOUBLES
  for x in range(0, len(state_list)):
    genPosMoves(state_list[x], state_list)
    print len(state_list)

    #roll = state_list[0].roll

  return state_list

def genPosMoves(st, state_list):
  # NEED TO FIX MOVE GENERATION
  '''Generates a list of possible move for computer to consider'''
  
  b = st.board
  turn = st.turn
  roll = st.roll
  #pip_count = state.pip_count

  val_moves = existValidMoves(b, roll, turn)

  if (val_moves == False):
    #print "no valid moves"
    return 

  else: #There exists at least one valid move
    #print "Getting here?"
    if(pieceInJail(b, turn)):
      #print "Pieces in jail"
      #Must move piece from jail if possible
      space_from = 26 + turn 
      for x in range(0, len(roll)):
        pos_valid = checkSpaceTo(b, turn, space_from, space_from + roll[x], roll)
        if (pos_valid[0]):
          space_to = pos_valid[1]
          move_dist = pos_valid[2]
          space_from = pos_valid[3]

          # Execute move
          b_copy = copy.deepcopy(b)
          move_piece = b_copy.board[space_from].s.pop()
    
          #Check if the current space is now empty - if so and not a jail space, update color
          if (isinstance(b_copy.board[space_from], jailSpace) == False):
            if (len(b_copy.board[space_from].s) == 0):
              b_copy.board[space_from].updateColor(-1)

          # Capture opponent piece and put it in jail
          if (b_copy.board[space_to].color != turn):
            if (len(b_copy.board[space_to].s) == 1):
              cap_piece = b_copy.board[space_to].s.pop()
              if (turn == WHITE):
                b_copy.board[27].s.append(cap_piece)
              elif (turn == BLACK):
                b_copy.board[26].s.append(cap_piece)

          b_copy.board[space_to].s.append(move_piece)
          # If space_to was empty, update color to turn
          b_copy.board[space_to].updateColor(turn)
          
          move_tuple = (space_from, space_to, move_dist)
          # Remove used roll from roll list
          roll.remove(move_dist)

          next_state = state(b_copy, turn, roll)
          state_list.append(next_state)


    else:
      print "No pieces in jail"
      # If no pieces in jail
      for x in range(1,25):
      
        # If current space is not same color as the player, continue
        cur_space = b.board[x]
        if (cur_space.color != turn):
          continue

        else:
          space_from = x
          for y in range(0, len(roll)):
            pos_valid = checkSpaceTo(b, turn, space_from, space_from + roll[y], roll)
            if (pos_valid[0]):
              space_to = pos_valid[1]
              move_dist = pos_valid[2]
              space_from = pos_valid[3]

              # Execute move
              b_copy = copy.deepcopy(b)
              r_copy = copy.copy(roll)
              move_piece = b_copy.board[space_from].s.pop()
    
              #Check if the current space is now empty - if so and not a jail space, update color
              if (isinstance(b_copy.board[space_from], jailSpace) == False):
                if (len(b_copy.board[space_from].s) == 0):
                  b_copy.board[space_from].updateColor(-1)

              # Capture opponent piece and put it in jail
              if (b_copy.board[space_to].color != turn):
                if (len(b_copy.board[space_to].s) == 1):
                  cap_piece = b_copy.board[space_to].s.pop()
                  if (turn == WHITE):
                    b_copy.board[27].s.append(cap_piece)
                  elif (turn == BLACK):
                    b_copy.board[26].s.append(cap_piece)

              b_copy.board[space_to].s.append(move_piece)
              # If space_to was empty, update color to turn
              b_copy.board[space_to].updateColor(turn)

              # Remove used roll from roll list
              r_copy.remove(move_dist)

              next_state = state(b_copy, turn, r_copy)
              state_list.append(next_state)
              #print "here " + str(len(state_list))

  
    state_list.remove(st)
    #print len(state_list)

def calcMoveValue(st):
  # NEED TO CHANGE ALGORITHM
  move_value = 0

  b = st.board
  turn = st.turn
  roll = st.roll
  pip_count = st.pip_count

  uncovered_score = 0
  blocade_score = 0

  # subtract points for uncovered pieces
  for x in range(0, 25):
    cur_space = b.board[x]
    if (cur_space.color != turn):
      continue

    else: 
      if (len(cur_space.s) == 1):
        if (turn == 0):
          blot_points = 10 * ((25-x)*.25) # 10 times distance from home/4 (just made it up)
        else:
          blot_points = 10 * ((x)*.25)
        uncovered_score = uncovered_score + blot_points

  # add points for blocades
  for x in range(0, 25):
    blocade_count = 0
    cur_space = b.board[x]

    if (len(cur_space.s) < 2 or cur_space.color != turn):
      # if reached end of the blocade
      blocade_score = blocade_score + (blocade_count*20)
      blocade_count = 0
  
    else:
      blocade_count += 1
  
  adj_pip_score = int(pip_count[turn])*.1
  move_value = blocade_score - uncovered_score - adj_pip_score

  return move_value


def playStratCompTurn(b, roll, turn):
  '''Calculate and return a valid move based on programmed strategy'''
  move_list = compGenMoves(state(b,turn,roll))
  #print len(move_list)
  
  cur_max = -1000000
  best_move = []

  for x in range(0, len(move_list)):
    
    temp = calcMoveValue(move_list[x])

    if (temp > cur_max):
      # If temp move better than current best, remove current best and store temp
      cur_max = temp
      best_move = []
      best_move.append(move_list[x])

    elif (temp == cur_max):
      # If temp is equal to current best, store both moves and decide which one later
      best_move.append(move_list[x])


    print str(x) + ":   "
    #move_list[x].printState()
  print "BEST MOVE VALUE: " + str(cur_max)
  #print best_move[0].printState()

  return best_move


def playRandCompTurn(b, roll, turn):
  '''Calculate and return a valid, random Computer move'''
 
  space_from = getCompSpaceFrom(b, turn, roll)
  space_to = getCompSpaceTo(b, roll, turn, space_from)
  space_to_valid = checkSpaceTo(b, turn, space_from, space_to, roll)
  
  return space_to_valid

def playHumanTurn(b, roll, turn):
  '''Receive move from human play and check its validity'''
  space_from = getSpaceFrom(b, turn)
  space_to = getSpaceTo()
  space_to_valid = checkSpaceTo(b, turn, space_from, space_to, roll)
  
  return space_to_valid

def playTurn(b, roll, turn, bool_flag):
  ''' Play one turn  - return the turn value of the other player'''
  
  val_moves = existValidMoves(b, roll, turn)

  if (val_moves == False):
    turnState = state(b, turn, roll)
    stateList.append(turnState)
    print "No valid moves exist - next player's turn."
    turnState.printState()
    
  while (val_moves):

    turnState = state(b, turn, roll)
    stateList.append(turnState)
    
    turnState.printState()
    
    valid_move = False

    if(bool_flag == True):
      while (valid_move == False):
        # Generate player moves and check if they are valid
        space_to_valid = playHumanTurn(b, roll, turn)
        valid_move = space_to_valid[0]
        if (valid_move != True):
          printError(space_to_valid[2])
        else:
          #assign valid move values to actual move varialbes
          space_to = space_to_valid[1]
          move_dist = space_to_valid[2]
          space_from = space_to_valid[3]

          # Execute move
          move_piece = b.board[space_from].s.pop()
    
          #Check if the current space is now empty - if so and not a jail space, update color
          if (isinstance(b.board[space_from], jailSpace) == False):
            if (len(b.board[space_from].s) == 0):
              b.board[space_from].updateColor(-1)

          # Capture opponent piece and put it in jail
          if (b.board[space_to].color != turn):
            if (len(b.board[space_to].s) == 1):
              cap_piece = b.board[space_to].s.pop()
              if (turn == WHITE):
                b.board[27].s.append(cap_piece)
              elif (turn == BLACK):
                b.board[26].s.append(cap_piece)

          b.board[space_to].s.append(move_piece)
          # If space_to was empty, update color to turn
          b.board[space_to].updateColor(turn)

          # Remove used roll from roll list 
          roll.remove(move_dist)
          #if (len(roll) > 0):
          #print roll

          # Check if there are any valid moves with remaining rolls
          val_moves = existValidMoves(b, roll, turn)
    else:
      list_moves = playStratCompTurn(b, roll, turn)
      i = int(math.floor(random.random()*len(list_moves)))
      list_moves[i].printState()
      b.updateFromState(list_moves[i])
      #b.printBoard()
      

      val_moves = False

  next_turn = switchTurn(turn)
  return next_turn


def getSpaceFrom(b, turn):
  '''Get space to move from from user'''
  if(len(b.board[26+turn].s) > 0):
    print "You must move your piece from Jail."
    space_from = (26+turn)
  else:
    move_from = False
    while (move_from == False):
      space_from = raw_input("Please input the space you would like to move from: ")
      try:
        space_from = int(space_from)
      except:
        print "That was not a valid input."

      if (space_from < 27 and space_from >= 0):
        space_color = b.board[space_from].color
        if(space_color == turn):
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

def getCompSpaceFrom(b, turn, roll):
  '''Get space from the computer'''
  if(len(b.board[26 + turn].s) >0):
    print "Computer must move piece from Jail."
    space_from = (26 + turn)
  else:
    test = roll.pop()
    if (allInFinalQuadrant(b, turn)):
      # All pieces in final quadrant
      if (lastOccupiedSpace(b,turn) < test):
        # If largest roll is greater than distance from home of farthest away space
        if (turn == 0):
          space_from = lastOccupiedSpace(b,turn)
        else:
          space_from = 25 - lastOccupiedSpace(b,turn)
      else:
        # If largest roll is smaller than furthest away piece
        move_from = False
        while (move_from == False):
          test_space = int(math.floor(random.random()*(24)) + 1)
          if (b.board[test_space].color == turn):
            move_from = True
            space_from = test_space
    else:
      # No piece in jail and not all in final quadrant
      move_from = False
      while (move_from == False):
        test_space = int(math.floor(random.random()*(24)) + 1)
        if (b.board[test_space].color == turn):
          move_from = True
          space_from = test_space

    roll.append(test)
  
  #print space_from
  return space_from

def getCompSpaceTo(b, roll, turn, space_from):
  ''' Return's the comps select space plus the largest remaining dice roll'''
  rollcpy = copy.copy(roll)

  if (random.random() > .5):
    # Check the higher or lower value 50% of time - allows both high and low rolls to be
    # checked by comp
    rollcpy.reverse()
  
  if (turn == 1):
    if (space_from == 26 + turn):
      # If comp is in jail
      
      test = rollcpy.pop()
      space_to = test
    

    elif (allInFinalQuadrant(b, turn) == False):
      # Comp not in jail && not all in final quadrant
      test = rollcpy.pop()
      space_to = space_from + test
      #roll.append(test)
    
    else:
      # If all pieces in final quadrant
      # To account for when 
      test = rollcpy.pop()
      space_to = space_from + test
      if (space_to > 25):
        space_to = 25
      #roll.append(test)
  
  elif (turn == 0):
    if (space_from == 26 + turn):
      # If comp is in jail
      if (random.random() > .5):
        rollcpy.reverse()
      test = rollcpy.pop()
      space_to = 25-test

    elif (allInFinalQuadrant(b, turn) == False):
      # Comp not in jail && not all in final quadrant
      test = rollcpy.pop()
      space_to = space_from - test

    else:
      # If all pieces in final quadrant
      # To account for when 
      test = rollcpy.pop()
      space_to = space_from - test
      if (space_to < 0):
        space_to = 0

  #print space_to
  return space_to


def checkFwdMove(space_from, space_to, turn):
  '''Check if inputted move is a forward move'''
  if (turn == WHITE):
    if (space_to < space_from):
      return True
    else:
      return False
  else:
    if (space_to > space_from):
      return True
    else:
      return False

def checkSpaceTo(b, turn, space_from, space_to, roll):
  '''Check if the space to move to is a valid location. If location is invalid, \
     return a specific negative move distance that will correlate to a specific error'''
  
  orig_space_from = space_from

  valid_move = True

  if((space_to > 25 or space_to < 0) and allInFinalQuadrant(b, turn) == False):
    valid_move = False
    return (valid_move, space_to, -1)
    # move_dist = -1 --> tried to move off the board

  # If a piece is in jail, it will start counting the moves from space 0 or 25 respectively
  if (isinstance(b.board[space_from], jailSpace)):
    space_from = b.board[space_from].getMoveFrom()
    
  # Check its forwards
  if (checkFwdMove(space_from, space_to, turn) == False):
    valid_move = False
    return (valid_move, space_to, -2)
    # move_dist = -2 --> tried to move backwards

  # Check you are not removing pieces prematurely
  if(space_to <= 0 or space_to >= 25):
    if(allInFinalQuadrant(b, turn)):
      # move_dist = -3 --> tried to score points when not allowed#If all pieces are in final quadrant
      check_last_space = lastOccupiedSpace(b, turn)
      temp = roll.pop()
      test = temp
      roll.append(temp)

      if ((math.fabs(space_from - space_to) == check_last_space) and \
        (test >= check_last_space)):
        return (valid_move, space_to, test, orig_space_from)
      
    else:
      valid_move = False
      return (valid_move, space_to, -3)

  # Check space_to is not a stack of the other color
  if((b.board[space_to].color != turn)):
    if(len(b.board[space_to].s) > 1):
      valid_move = False
      return (valid_move, space_to, -4)
      # move_dist = -4 --> tried to move to an occupied square of the other color


  # Check that the move distance is a remaining roll
  move_dist = math.fabs(space_from - space_to)
  if (roll.count(int(move_dist)) == 0):
    valid_move = False
    return (valid_move, space_to, -5)
    #move_dist = -5 --> tried to move a distance that wasn't rolled

  return(valid_move, space_to, move_dist, orig_space_from)    

def existValidMoves(b, roll, turn):
  '''Check to see if valid moves exist - if they do not, flip the turn'''
  
  val_moves = False

  if (len(roll) == 0):
    # no remaining rolls --> no valid moves
    return val_moves

  elif (pieceInJail(b, turn)):
    # If piece is in jail, check for valid moves from jail only
    space_from = 26+turn
    if (turn == BLACK):
      for x in range(0, len(roll)):
        pos_valid = checkSpaceTo(b, turn, space_from, roll[x], roll)
        if (pos_valid[0]):
          val_moves = True
          break
    else:
      for x in range(0, len(roll)):
        pos_valid = checkSpaceTo(b, turn, space_from, 25-roll[x], roll)
        if (pos_valid[0]):
          val_moves = True
          break

  else:
    # If no piece in jail, check all other pieces for valid moves
    for x in range(1,25):

      if (val_moves):
        break
      
      cur_space = b.board[x]

      if (cur_space.color != turn):
        continue

      else:
        space_from = x
        for y in range(0, len(roll)):
          if (turn == BLACK):
            if (space_from + roll[y] > 25):
              pos_valid = checkSpaceTo(b, turn, space_from, 25, roll)
            else:
              pos_valid = checkSpaceTo(b, turn, space_from, space_from + roll[y], roll)
          elif (turn == WHITE):
            if (space_from - roll[y] < 0):
              pos_valid = checkSpaceTo(b, turn, space_from, 0, roll)
            else:
              pos_valid = checkSpaceTo(b, turn, space_from, space_from - roll[y], roll)
          
          if (pos_valid[0]):
            val_moves = True
            
            break
  
  return val_moves


def printError(num):
  '''Print specific error messages depending on why user move was invalid'''

  print "Illegal move - ",

  if (num == -1):
    print "tried to move off the board."

  if (num == -2):
    print "tried to move backwards."

  if (num == -3):
    print "tried to remove pieces from board when not allowed."

  if (num == -4):
    print "tried to move to an occupied space of another color."

  if (num == -5):
    print "tried to move a distance that wasn't rolled."

def lastOccupiedSpace(b, turn):
  max_space = 0

  if (turn == WHITE):
    for x in range(1,25):
      col = b.board[x].color
      if (col == turn):
        max_space = x
  else:
    for x in range(24, 0, -1):
      col = b.board[x].color
      if (col == turn):
        max_space = (25 - x)

  return max_space

def allInFinalQuadrant(b, turn):
  '''Tests if all pieces are in final quadrant'''
  allInFQ = True
  if (turn == WHITE):
    for x in range(7, 25):
      if(b.board[x].color == WHITE):
        allInFQ = False
        break
  
  if (turn == BLACK):
    for x in range(1, 19):
      if (b.board[x].color == BLACK):
        allInFQ = False
        break

  return allInFQ


def testGameOver(b):
  '''Tests for game over condition (all pieces are in final home space)'''
  scores = b.getScore()
  done = -1

  if (scores[0] == 15):
    done = WHITE
  elif(scores[1] == 15):
    done = BLACK

  return done

def printTurn(turn):
  '''Print whose turn it is to console'''

  print ""
  if(turn == 0):
    print "Player one's turn ('o')"  
  else:
    print "Player two's turn ('x')"
  print ""
  
def switchTurn(turn):
  '''Switch turn from black to white or vice versa'''
  if (turn == 0):
    next_turn = 1
  else:
    next_turn = 0

  return next_turn

def rollDie(die):
  '''Rolls 2 die (returns 4 die if doubles)'''
  
  roll1 = die.roll()
  roll2 = die.roll()

  if (roll1 == roll2):
    totalRoll = [roll1, roll1, roll1, roll1]

  else:
    totalRoll = [roll1, roll2]

  totalRoll.sort()
  return totalRoll

def goesFirst(die):
  '''Rolls dice to see who goes first. Re-rolls on doubles and returns the \
  combined roll'''

  roll1 = die.roll()
  roll2 = die.roll()

  while (roll1 == roll2):
    roll1 = die.roll()
    roll2 = die.roll()

  if (roll1 > roll2):
    turn = 0
    # i.e. Player 1 (white) goes first

  else:
    turn = 1
    #i.e. Player 2 (black) goes first
  
  totalRoll = [roll1, roll2]
  totalRoll.sort()

  return (turn, totalRoll)

def getPipCount(b):
  b_pips = 0
  w_pips = 0

  for x in range(1, 25):
    #print type(b)
    cur_col = b.board[x].getColor()

    if (cur_col == -1):
      continue

    elif (cur_col == 0):
      space_pip_count = len(b.board[x].s) * x
      w_pips = w_pips + space_pip_count
      
    else:
      space_pip_count = len(b.board[x].s) * (25 -x)
      b_pips = b_pips + space_pip_count

  # Calc dist for pieces in white jail
  space_pip_count = len(b.board[26].s) * 25
  w_pips = w_pips + space_pip_count

  space_pip_count = len(b.board[27].s) * 25
  b_pips = b_pips + space_pip_count

  return (w_pips, b_pips)


if __name__ == "__main__":
  main()

