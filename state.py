# Represents the current state of the game (Turn, Remaining Roll Values,
# Piece locations and Pip Count)

import math
import copy
import space


class state(): 

  def __init__(self, board, turn, roll):
    self.board = copy.deepcopy(board)
    self.turn = copy.copy(turn)
    self.roll = list(roll)
    self.pip_count = self.board.getPipCount()

  def __str__(self):
    return_string = '\n'
    
    return_string = return_string + str(self.turn) + "\n"
    
    return_string = return_string + str(self.roll) + "\n" + "\n"
    return_string = return_string + "White pip count: " + str(self.pip_count[0])
    return_string = return_string + " Black pip count: " + str(self.pip_count[1])
    return_string = return_string + "\n" 
    return_string = return_string + str(self.board)

    return return_string

  def compareStates(self, other_state):
    '''Compare a given state to another state to determine if they are the same'''
    sameState = True
    
    if (self.turn.turn != other_state.turn.turn):
      sameState = False
    
    if (len(self.roll) != len(other_state.roll)):
      sameState = False

    else:
      for x in range (0, 27):
        if (len(self.board.spaceList[x]) == len(other_state.board.spaceList[x])):
          continue
        else:
          sameState = False
          break

    return sameState

  def updateFromState(self, other_state):
    '''Update a state to match another state'''
    self.roll = other_state.roll
    self.turn = other_state.turn
    self.board = other_state.board
    self.pip_count = other_state.board.getPipCount()

  def updateRoll(self, roll):
    self.roll = list(roll)

  def updatePipCount(self):
    self.pip_count = self.board.getPipCount()

  def printState(self):
    if (self.turn.turn == 0):
      print "White's Turn"
    else:
      print "Black's Turn"

    print self.roll
    print " " 
    print "White pip count: " + str(self.pip_count[0]),
    print "Black pip count: " + str(self.pip_count[1])
    self.board.printBoard()

  def testGameOver(self):
    ''' Tests for game over conditions'''
    scores = self.board.getScore()
    done = -1

    if (scores[0] == 15):
      done = 0
    elif(scores[1] == 15):
      done = 1

    return done

  def allInFinalQuadrant(self):
    '''Checks if all pieces are in the final quadrant'''
    allInFQ = True
    if (self.turn.turn): #Black's turn
      for x in range (1, 19):
        if (self.board.spaceList[x].getColor() == 1):
          allInFQ = False
          break
    else:
      for x in range(7, 25):
        if (self.board.spaceList[x].getColor() == 0):
          allInFQ = False
          break

    return allInFQ

  def lastOccupiedSpace(self):
    furthest_white = 0
    furthest_black = 24

    for x in range(1, 25):
      cur_space = self.board.spaceList[x]
      cur_space_color = cur_space.getColor()

      if (cur_space_color == 0): #White
        if (x > furthest_white):
          furthest_white = x

      elif (cur_space_color == 1): #Black
        if (x < furthest_black):
          furthest_black = x

    if (len(self.board.spaceList[26]) > 0):
      furthest_white = 25
    if (len(self.board.spaceList[27]) > 0):
      furthest_black = 0
    
    return (furthest_white, furthest_black)


  def furthestFromHome(self):
    '''Returns the furthest distance from home for the current player'''
    max_space = 0

    if (self.turn.turn): #Black's turn
      for x in range(24, 0, -1):
        col = self.board.spaceList[x].getColor()
        if (col == self.turn.turn):
          max_space = (25-x)

    elif (self.turn.turn == 0): # White's turn
      for x in range(1, 25):
        col = self.board.spaceList[x].getColor()
        if (col == self.turn.turn):
          max_space = x

    return max_space

  def pieceInJail(self): 
    '''Returns true if current player has piece(s) in jail. Else, returns false'''
    board = self.board
    turn = self.turn.turn
    
    if (len(board.spaceList[26+turn]) > 0):
      return True
    else:
      return False

  def existValidMoves(self):
    '''Check to see if valid moves exist - otherwise, flip the turn'''

    val_moves = False

    if (len(self.roll) == 0):
      # no remaining rolls --> no valid moves
      print "no remaining rolls"
      return val_moves

    elif(self.pieceInJail()):
      #print "piece in jail"
      space_from = 26+self.turn.turn
      if (self.turn.turn): #Black
        for x in range(0, len(self.roll)):
          pos_valid = self.checkSpaceTo(space_from, self.roll[x])
          if (pos_valid[0]):
            val_moves = True
            break

      else: #White
        for x in range(0, len(self.roll)):
          pos_valid = self.checkSpaceTo(space_from, 25-self.roll[x])
          if (pos_valid[0]):
            val_moves = True
            break

    else:
      #print "no pieces in jail"
      for x in range(1,25):
        cur_space = self.board.spaceList[x]

        if (val_moves):
          break

        elif (cur_space.getColor() != self.turn.turn):
          continue

        else:
          space_from = x
          
          for y in range(0, len(self.roll)):
            if (self.turn.turn == 1):
              #print "Black's turn w/ nobody in jail"
              if(space_from + self.roll[y] > 25):
                pos_valid = self.checkSpaceTo(space_from, 25)
              else:
                pos_valid = self.checkSpaceTo(space_from, space_from + self.roll[y])

            elif (self.turn.turn == 0):
              #print "White's turn with no-one in jail"
              if (space_from - self.roll[y] < 0):
                pos_valid = self.checkSpaceTo(space_from, 0)
              else:
                pos_valid = self.checkSpaceTo(space_from, space_from - self.roll[y])

            if (pos_valid[0]):
              val_moves = True
              break

        #print pos_valid

    return val_moves

  def checkFwdMove(self, space_from, space_to):
    '''Check if inputted move is a forward move'''
    
    if (self.turn.turn == 0):
      if (space_to < space_from):
        return True
      else:
        return False
    else:
      if (space_to > space_from):
        return True
      else:
        return False


  def checkSpaceTo(self, space_from, space_to):
    '''Check if space desired to move to is legal'''
    orig_space_from = space_from
    orig_space_to = space_to

    if (space_to <= 0):
      space_to = 0
    elif (space_to >= 25):
      space_to = 25

    valid_move = True
    

    if (isinstance(self.board.spaceList[space_from], space.jailSpace)):
      # When moving from jail, adjust "space from" to make distance calculations work
      space_from = self.board.spaceList[space_from].getMoveFrom()

    move_dist = int(math.fabs(space_from - space_to))

    if ((space_to > 25 or space_to < 0) and self.allInFinalQuadrant() == False):
      valid_move = False
      move_dist = -1
      return (valid_move, orig_space_from, space_to, move_dist)

    if (self.checkFwdMove(space_from, space_to) == False):
      valid_move = False
      move_dist = -2
      return (valid_move, orig_space_from, space_to, move_dist)

    if (space_to <= 0 or space_to >= 25):
      if (self.allInFinalQuadrant()):
        check_last_space = self.furthestFromHome()
        roll_copy = copy.copy(self.roll)
        roll_copy.sort()
        test = roll_copy.pop()

        if ((math.fabs(space_from - space_to) == check_last_space) and \
          (test >= check_last_space)):
          move_dist = test

      else:
       valid_move = False
       move_dist = -3
       return (valid_move, orig_space_from, space_to, move_dist)       

    if (self.board.spaceList[space_to].getColor() != self.turn.turn):
      if (len(self.board.spaceList[space_to]) > 1):
        valid_move = False
        move_dist = -4
        return (valid_move, orig_space_from, space_to, move_dist)
        
    if (self.roll.count(move_dist) == 0):
      valid_move = False
      move_dist = -5
      return (valid_move, orig_space_from, space_to, move_dist)
      
    return (valid_move, orig_space_from, space_to, move_dist)

  def printError(self, num):
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












    