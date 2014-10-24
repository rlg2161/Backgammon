# A basic backgammon game that interfaces with console

import dice
import math
import copy
import random


WHITE = 0
BLACK = 1
stateList = [] # keeps track of every move and remaining dice at that time
               # creates a LL of game states for undo's

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
    return color

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

#class oneDie():
  #'''Represents one die (of variable side number)'''
  #def __init__(self, sides = None):
    #if (sides is None):
      #self.num_sides = 6
    #else:
      #self.num_sides = sides

  #def roll(self):
    #get_roll = math.floor(random.random()*(self.num_sides)) + 1
    #return int(get_roll)

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

  def printState(self):
    if (self.turn == 0):
      print "White's Turn"
    else:
      print "Black's Turn"

    print self.roll
    print " " 
    self.board.printBoard()

  def __str__(self):
    return_string = ''
    
    if (self.turn == 0):
      return_string = return_string + "White's Turn"
    else:
      return_string = return_string + "Black's Turn"

    return_string = return_string + str(self.roll)
    return_string = return_string + "\n" 
    return_string = return_string + str(self.board)

    return return_string


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
    turn = playHumanTurn(b, roll, turn)
    #b.printBoard()

    while(winner == -1):
      printTurn(turn)
      roll = rollDie(die)
      turn = playHumanTurn(b, roll, turn)
      winner = testGameOver(b)

    #b.printBoard()
    lastState = state(b, turn, roll)
    #lastState.printState()
    stateList.append(lastState)
    
    
  elif (comp == 1): #Play against a computer
    # Human player is always white
    printTurn(turn)

    if (turn == 0):
      turn = playHumanTurn(b, roll, turn)

    else:
      turn = playCompTurn(b, roll, turn)

    while(winner == -1):
      printTurn(turn)
      roll = rollDie(die)
      if (turn == 0):
        turn = playHumanTurn(b, roll, turn)
      else:
        turn = playCompTurn(b, roll, turn)
      winner = testGameOver(b)

    lastState = state(b, turn, roll)
    #lastState.printState()
    stateList.append(lastState)

  else: # play 2 computers
    printTurn(turn)
    turn = playCompTurn(b, roll, turn)

    while(winner == -1):
      printTurn(turn)
      roll = rollDie(die)
      turn = playCompTurn(b, roll, turn)
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

  #board.printBoard()
  
  if (len(b.board[26+turn].s) > 0):
    return True
  else:
    return False
   

def existValidMoves(b, roll, turn):
  '''Check to see if valid moves exist - if they do not, flip the turn'''
  
  val_moves = False

  if (len(roll) == 0):
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
            print pos_valid
            break
  
  return val_moves

def playCompTurn(b, roll, turn):
  ''' Play one turn for computer - return the turn value of the other player'''
  
  val_moves = existValidMoves(b, roll, turn)

  if (val_moves == False):
    turnState = state(b, turn, roll)
    stateList.append(turnState)
    print "No valid moves exist - next player's turn."
    turnState.printState()
    #lastGameFile.write(turnState.printState())

  while (val_moves):

    turnState = state(b, turn, roll)
    stateList.append(turnState)
    
    turnState.printState()
    #lastGameFile.write(turnState.printState())

    valid_move = False

    while (valid_move == False):
      # Generate computer moves and check if they are valid
      print "Valid move tuple: " + str(existValidMoves(b, roll, turn)) + str(roll)
      space_from = getCompSpaceFrom(b, turn, roll)
      space_to = getCompSpaceTo(b, roll, turn, space_from) # will have to include a last quadrant logical section
      space_to_valid = checkSpaceTo(b, turn, space_from, space_to, roll)
      valid_move = space_to_valid[0]
      if (valid_move != True):
        print space_from, space_to
        printError(space_to_valid[2])

    #assign valid move values to actual move varialbes
    space_to = space_to_valid[1]
    move_dist = space_to_valid[2]

    print (space_from, space_to)

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
    print val_moves

  next_turn = switchTurn(turn)
  return next_turn


def playHumanTurn(b, roll, turn):
  '''Play one turn - return turn value of other player'''
  
  val_moves = existValidMoves(b, roll, turn)
  #print roll
  if (val_moves == False):
    turnState = state(b, turn, roll)
    stateList.append(turnState)    
    print "No valid moves exist - next player's turn."
    turnState.printState()
    #lastGameFile.write(turnState.printState())
  
  while (val_moves):

    turnState = state(b, turn, roll)
    stateList.append(turnState)
    
    turnState.printState()
    #lastGameFile.write(turnState.printState())
    
    valid_move = False

    while (valid_move == False):
      # Get valid target from and to spaces
      space_from = getSpaceFrom(b, turn)
      space_to = getSpaceTo()
      space_to_valid = checkSpaceTo(b, turn, space_from, space_to, roll)
      valid_move = space_to_valid[0]
      if (valid_move != True):
        printError(space_to_valid[2])

    # assign valid move values from checkSpaceTo()
    space_to = space_to_valid[1]
    move_dist = space_to_valid[2]

    # Execute move
    move_piece = b.board[space_from].s.pop()

    if (isinstance(b.board[space_from], jailSpace) == False):
      # If space_from is empty and not a jail space, update color to -1
      if (len(b.board[space_from].s) == 0):
        b.board[space_from].updateColor(-1)

    #col = getColor(board[space_to])
    #if (col != turn):
       # If it turns out we need to get color before updating space color

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

def getCompSpaceFrom(b, turn, roll):
  '''Get space from the computer'''
  if(len(b.board[26 + turn].s) >0):
    print "Computer must move piece from Jail."
    space_from = (26 + turn)
  else:
    test = roll.pop()
    if (allInFinalQuadrant(b, turn)):
      if (lastOccupiedSpace(b,turn) < test):
        if (turn == 0):
          space_from = lastOccupiedSpace(b,turn)
        else:
          space_from = 25 - lastOccupiedSpace(b,turn)
      else:
        move_from = False
        while (move_from == False):
          test_space = int(math.floor(random.random()*(24)) + 1)
          if (b.board[test_space].color == turn):
            move_from = True
            space_from = test_space
    else:
      move_from = False
      while (move_from == False):
        test_space = int(math.floor(random.random()*(24)) + 1)
        if (b.board[test_space].color == turn):
          move_from = True
          space_from = test_space

    roll.append(test)
  
  #print space_from
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
    if(allInFinalQuadrant(b, turn) == False):
      valid_move = False
      return (valid_move, space_to, -3)
      
    else:
      # move_dist = -3 --> tried to score points when not allowed#If all pieces are in final quadrant
      check_last_space = lastOccupiedSpace(b, turn)
      temp = roll.pop()
      test = temp
      roll.append(temp)

      if ((math.fabs(space_from - space_to) == check_last_space) and \
        (test >= check_last_space)):
        return (valid_move, space_to, test)

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

  return(valid_move, space_to, move_dist)    

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



if __name__ == "__main__":
  main()

