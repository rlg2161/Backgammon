# A basic backgammon game that interfaces with console

import math
import random


WHITE = 0
BLACK = 1

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

class oneDie():
  
  def __init__(self, sides = None):
    if (sides is None):
      self.num_sides = 6
    else:
      self.num_sides = sides

  def roll(self):
    get_roll = math.floor(random.random()*(self.num_sides)) + 1
    return int(get_roll)

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
    
    self.board[1].fillSpace(1, 2)
    self.board[6].fillSpace(0, 5)
    self.board[8].fillSpace(0, 3)
    self.board[12].fillSpace(1, 5)
    self.board[13].fillSpace(0, 5)
    self.board[17].fillSpace(1, 3)
    self.board[19].fillSpace(1, 5)
    self.board[24].fillSpace(0, 2)

    #self.board[1].fillSpace(0,2)
    #self.board[2].fillSpace(0,2)
    #self.board[3].fillSpace(0,2)
    #self.board[4].fillSpace(0,2)
    #self.board[5].fillSpace(0,2)
    #self.board[6].fillSpace(0,3)
   
    #self.board[19].fillSpace(1,3)
    #self.board[20].fillSpace(1,2)
    #self.board[21].fillSpace(1,2)
    #self.board[22].fillSpace(1,2)
    #self.board[23].fillSpace(1,2)
    #self.board[24].fillSpace(1,2)


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

def main():
  
  again = play()

  while(again):
    again = play()
  

def play():
  '''Play a game'''
  b = board()
  b.initBoard()
  die = oneDie(6)

  gf = goesFirst(die)
  turn = gf[0]
  roll = gf[1]
  
  printTurn(turn)
  turn = playTurn(b, roll, turn)
  b.printBoard()

  winner = -1
  

  while(winner == -1):
    printTurn(turn)
    roll = rollDie(die)
    turn = playTurn(b, roll, turn)
    winner = testGameOver(b)

  b.printBoard()

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
            pos_valid = checkSpaceTo(b, turn, space_from, space_from + roll[y], roll)
          if (turn == WHITE):
            pos_valid = checkSpaceTo(b, turn, space_from, space_from - roll[y], roll)
          if (pos_valid[0]):
            val_moves = True
            break
  
  return val_moves


def playTurn(b, roll, turn):
  '''Play one turn - return turn value of other player'''
  val_moves = existValidMoves(b, roll, turn)
  print roll
  if (val_moves == False):
    print "No valid moves exist - next player's turn."
  while (val_moves):
    b.printBoard()
    

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
    if (len(roll) > 0):
      print roll

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
    print "Failed test 1"
    valid_move = False
    return (valid_move, space_to, -1)
    # move_dist = -1 --> tried to move off the board

  # If a piece is in jail, it will start counting the moves from space 0 or 25 respectively
  if (isinstance(b.board[space_from], jailSpace)):
    print space_from
    space_from = b.board[space_from].getMoveFrom()
    print space_from

  # Check its forwards
  if (checkFwdMove(space_from, space_to, turn) == False):
    print "Failed test 2"
    valid_move = False
    return (valid_move, space_to, -2)
    # move_dist = -2 --> tried to move backwards

  # Check you are not removing pieces prematurely
  if(space_to == 0 or space_to == 25):
    if(allInFinalQuadrant(b, turn)):
      #If all pieces are in final quadrant
      check_last_space = lastOccupiedSpace(b, turn)
      temp = roll.pop()
      test = temp
      roll.append(temp)

      if ((math.fabs(space_from - space_to) == check_last_space) and \
        (test >= check_last_space)):
        return (valid_move, space_to, test)

    else:
      print "Failed test 3"
      valid_move = False
      return (valid_move, space_to, -3)
      # move_dist = -3 --> tried to score points when not allowed

  # Check space_to is not a stack of the other color
  if((b.board[space_to].color != turn)):
    if(len(b.board[space_to].s) > 1):
      print "Failed test 4"
      valid_move = False
      return (valid_move, space_to, -4)
      # move_dist = -4 --> tried to move to an occupied square of the other color


  # Check that the move distance is a remaining roll
  move_dist = math.fabs(space_from - space_to)
  if (roll.count(int(move_dist)) == 0):
    print "Failed test 5"
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

  if (scores[0] == 13):
    done = WHITE
  elif(scores[1] == 13):
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

