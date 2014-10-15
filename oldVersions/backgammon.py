# A basic backgammon game

# 1 == True == BLACK  == 'x'
# 0 == False == WHITE == 'o'



import math
import random

def main():
  
  again = play()

  while(again):
    again = play()

class piece():
  '''Represents a board piece'''
  def __init__(self, color):
    if (color):
      self.color = 0
    else:
      self.color = 1 

  def __str__(self):
    if (self.color):
      return 'x'
    else:
      return 'o'

def die():
  '''Function to roll a single die'''
  roll = math.floor(random.random()*6) + 1
  return int(roll)

def rollDie():
  '''Rolls 2 die (returns 4 die if doubles)'''
  roll1 = die()
  roll2 = die()

  if (roll1 == roll2):
    totalRoll = [roll1, roll1, roll1, roll1]

  else:
    totalRoll = [roll1, roll2]

  return totalRoll

def initBoard():
  '''Initializes board to beginning of game'''
  board = []

  for x in range(0,28):
    pos = []
    board.append(pos)

  #fillCol(board[1], 1, 2)
  #fillCol(board[6], 0, 5)
  #fillCol(board[8], 0, 3)
  #fillCol(board[12], 1, 5)
  #fillCol(board[13], 0, 5)
  #fillCol(board[17], 1, 3)
  #fillCol(board[19], 1, 5)
  #fillCol(board[24], 0, 2)

  fillCol(board[1], 0, 2)
  fillCol(board[2], 0, 2)
  fillCol(board[3], 0, 2)
  fillCol(board[4], 0, 2)
  fillCol(board[5], 0, 2)
  fillCol(board[6], 0, 3)

  fillCol(board[19], 1, 3)
  fillCol(board[20], 1, 2)
  fillCol(board[21], 1, 2)
  fillCol(board[22], 1, 2)
  fillCol(board[23], 1, 2)
  fillCol(board[24], 1, 2)  
  
  return board

def fillCol(space, color, number):
  '''Fills spaces with desired number and type of pieces'''
  for x in range (0, number):
    p = piece(color)
    space.append(p)

def goesFirst():
  '''Determine who goes first'''
  p1roll = die()
  p2roll = die()

  while (p1roll == p2roll):
    # If equal, roll again - can add doubling functionality if desired
    p1roll = die()
    p2roll = die()

  if (p1roll > p2roll):
    turn = 0
    #print "Player one goes first"

  else:
    turn = 1
    #print "Player two goes first"

  return turn

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

def printBoard(board):
  '''Prints current state of board'''
  for x in range(0,len(board)):
    cur_space = board[x]
    if (x == 0):
      print "White Points Scored: ",
      for y in range(0, len(cur_space)):
        print cur_space[y],
      print ""
    elif (x > 0 and x < 25):
      print str(x) + ": ",
      for y in range(0, len(cur_space)):
        print cur_space[y],
      print ""
    elif (x == 25):
      print "Black Points Scored: ",
      for y in range(0, len(cur_space)):
        print cur_space[y],
      print ""
      print ""
    elif (x == 26):
      print "White Jail: ",
      for y in range(0, len(cur_space)):
        print cur_space[y],
      print ""
    else:
      print "Black Jail: ",
      for y in range(0, len(cur_space)):
        print cur_space[y],
      print ""
  print ""

def play():
  
  board = initBoard()
  turn = goesFirst()

  while((len(board[0]) < 15) and len(board[25]) < 15):
    printTurn(turn)
    turn = playTurn(board, turn)

  again_in = raw_input("Would you like to play again? \n Press y for yes and n for no:   ")

  if(again_in == "y" or again_in == "Y" or again_in == "yes" or again_in == "Yes"):
    again = 1
  else:
    again = 0

  return again

def playTurn(board, turn):
  '''Plays a single player's turn'''
  
  roll = rollDie()
  roll.sort()
  v_moves = existValidMoves(board, roll, turn)

  while (v_moves):
    if(len(roll)>0):
      printBoard(board)
      print roll

      # Get from and to spaces from user
      # if user enters invalid to space, get both from and to spaces again
    
      valid_move = False

      while (valid_move == False):
        space_from = getSpaceFrom(board, turn)
        space_to = getSpaceTo()
        space_to_valid = checkSpaceTo(board, turn, space_from, space_to, roll)
        valid_move = space_to_valid[0]

      # assign the move values from checkSpaceTo()
      space_to = space_to_valid[1]
      move_dist = space_to_valid[2]

      # Execute the move 
      move_piece = board[space_from].pop()

      if(len(board[space_to]) == 0):
        board[space_to].append(move_piece)

      elif(len(board[space_to]) > 1):
        board[space_to].append(move_piece)

      else:
        test = board[space_to].pop()
        if (test.color == turn):
          board[space_to].append(test)
          board[space_to].append(move_piece)
        else:
          if(turn == 0):
            board[27].append(test)
            board[space_to].append(move_piece)
          else:
            board[26].append(test)
            board[space_to].append(move_piece)

      roll.remove(move_dist)
    
    v_moves = existValidMoves(board, roll, turn)

  next_turn = switchTurn(turn)
  return next_turn

def existValidMoves(board, roll, turn):
  '''Check to see if valid moves exist - if no, will return false and turn will end'''
  
  valid = False

  if (turn == 0):
  
    #Check if valid moves exist if pieces are in jail
    if(len(board[26]) > 0):
      space_from = 0
      for y in range(0, len(roll)):
        pos_valid = checkSpaceTo(board, turn, space_from, space_from + roll[y], roll)
        if (pos_valid[0]):
          valid = pos_valid[0]
          break
    
    #Check normal board Spaces
    else:
      for x in range(1, 25):
        cur_space = board[x]
    
        if (len(cur_space) == 0):
          continue
    
        else:
          #check color
          piece = cur_space.pop()
          col = piece.color
          cur_space.append(piece)

          if (col == turn):
            #check if there are any valid moves
            space_from = x
            for y in range(0, len(roll)):
              pos_valid = checkSpaceTo(board, turn, space_from, space_from + roll[y], roll)
              if (pos_valid[0]):
                valid = pos_valid[0]
                break

    return valid

  else:
    #Check if valid moves exist if pieces are in jail
    if(len(board[26+turn]) > 0):
      space_from = 25
      for y in range(0, len(roll)):
        pos_valid = checkSpaceTo(board, turn, space_from, space_from - roll[y], roll)
        if (pos_valid[0]):
          valid = pos_valid[0]
          break
    
    #Check normal board Spaces
    else:
      for x in range(1, 25):
        cur_space = board[x]
    
        if (len(cur_space) == 0):
          continue
    
        else:
          #check color
          piece = cur_space.pop()
          col = piece.color
          cur_space.append(piece)

          if (col == turn):
            #check if there are any valid moves
            space_from = x
            for y in range(0, len(roll)):
              pos_valid = checkSpaceTo(board, turn, space_from, space_from - roll[y], roll)
              if (pos_valid[0]):
                valid = pos_valid[0]
                break

    return valid
  

def getSpaceFrom(board, turn):
  if(len(board[26+turn]) > 0):
    print "You must move your piece from Jail."
    space_from = (26+turn)
  else:
    move_from = False
    while (move_from == False):
      space_from = raw_input("Please input the space you would like to move from: ")
      try:
        space_from = int(space_from)
        space_color = testSpaceFrom(board, space_from)
        if(space_color == turn):
          move_from = True
      except:
        print "That was not a valid input."

  return space_from

def getSpaceTo():
  space_to = raw_input("Please input the space you would like to move to: ")
  try:
    space_to = int(space_to)
  except:
    print "That was not a valid input."
  return space_to

def checkSpaceTo(board, turn, space_from, space_to, roll):
  '''Determine if the space entered is a valid move - return validity, the space 
     moved to and the distance of the move'''

  move_to = False

  if (space_to > 25 or space_to < 0):
    #Ensure that area outside of array bounds is not tested
    return (False, space_to, 0)

  else:
    # If tries to move backward, invalidate the move
    if (checkFwdMove(space_from, space_to, turn) == False):
      return (False, space_to, 0)
  
    # Makes sure all pieces are in final quadrant before allowing them to be removed
    if (space_to == 0 or space_to == 25):
      if(allInFinalQuadrant(board, turn) != True):
        #print "Cannot score points if all pieces are not in final quadrant"
        return (False, space_to, 0)

    # If not in jail
    if (space_from < 26):
      # Allow pieces to be removed if roll is greater than distance from home of the 
      # farthest piece 
      
      #
      # Section that needs to be fixed
      # Works for white (sort of)
      # Doesn't work for black
      #

      if (allInFinalQuadrant(board,turn)):

        test = roll.pop()
        temp = test 
        roll.append(test)
        roll.sort()
        locLast = locLastPiece(board, turn)
        print locLast
        
        if (locLast < temp):
          if (turn == 0): 
            print "Getting here"
            return (True, 25, temp)
          else:
            print "getting hurr"
            return (True, 0, temp)
        else:
          space_color = testSpaceTo(board, space_to)
          move_dist = int(math.fabs(space_from - space_to))

      else:
        space_color = testSpaceTo(board, space_to)
        move_dist = int(math.fabs(space_from - space_to))

      #####
      ####
      ###
      ##
      #
    
    #If in White Jail
    elif (space_from == 26):
      space_color = testSpaceTo(board, space_to)
      move_dist = int(math.fabs(space_to))

    #If in Black Jail
    else:
      space_color = testSpaceTo(board, space_to)
      move_dist = int(math.fabs(25 - space_to))
  
    # if all above conditions are met, flip boolean to verify move as valid
    if((space_color == turn or space_color == -1) and (roll.count(move_dist) > 0)):
       move_to = True
 
    return (move_to, space_to, move_dist)

def checkFwdMove(space_from, space_to, turn):
  
  if (turn == 0 and space_from == 26):
    #White is in jail - any move will be a forward move
    return True

  if (turn == 0):
    if (space_from > space_to):
      print "You can only move forward"
      return False
    else: 
      return True
  else:
    if (space_from < space_to):
      print "You can only move forward"
      return False
    else:
      return True

def allInFinalQuadrant(board, turn):
  total = 0

  if (turn == 0):
    for x in range(1, 19):
      cur_space = board[x]
      if (len(cur_space) > 0):
        piece = cur_space.pop()
        col = piece.color
        cur_space.append(piece)

        if (col == turn):
          total = total + len(cur_space)

  elif (turn == 1): 
    for x in range(7, 25):
      cur_space = board[x]
      if (len(cur_space) > 0):
        piece = cur_space.pop()
        col = piece.color
        cur_space.append(piece)

        if (col == turn):
          total = total + len(cur_space)

  if (total == 0):
    return True
  else:
    return False

def locLastPiece(board, turn):
  loc = -1
  if (turn == 1):
    for x in range(6, 0, -1):
      cur_space = board[x]
      if (len(cur_space) > 0):
        loc = x
        break
  if (turn == 0):
    for x in range(19, 25):
      cur_space = board[x]
      if (len(cur_space) > 0):
        loc = 25-x
        break
  return loc



def testSpaceTo(board, num):
  cur_space = board[num]

  if (len(cur_space) == 0 or len(cur_space) == 1):
    return -1
  
  else:
    piece = cur_space.pop()
    space_color = piece.color
    cur_space.append(piece)
    return space_color

def testSpaceFrom(board, num):
  cur_space = board[num]

  if (len(cur_space) == 0):
    return -1

  else:
    piece = cur_space.pop()
    space_color = piece.color
    cur_space.append(piece)
    return space_color    



if __name__ == "__main__":
  main()