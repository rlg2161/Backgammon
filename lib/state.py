# Represents the current state of the game (Turn, Remaining Rolls,
# Piece Locations)

import copy
import math
import numpy as np

class state():

  def __init__(self, *args): #turn, roll):
    '''Constructor for first state object'''
    # args == (turn, roll)
    if (len(args) == 2):
      self.board = np.zeros(28)
      #for x in range(0,28):
        #self.board.append(0)
      self.board[1] = -2
      self.board[6] = 5
      self.board[8] = 3
      self.board[12] = -5
      self.board[13] = 5
      self.board[17] = -3
      self.board[19] = -5
      self.board[24] = 2

      self.turn = args[0]
      self.roll = args[1]

    # args == (state)
    if (len(args) == 1):
      self.board = copy.deepcopy(args[0].board)
      self.turn = args[0].turn
      self.roll = list(args[0].roll)



    if (len(args) == 0): #make custom state
      self.board = np.zeros(28)
      self.board[0] = 0
      self.board[1] = -2
      self.board[2] = 0
      self.board[3] = 0
      self.board[4] = 1
      self.board[5] =0
      self.board[6] = 5
      self.board[7] = 0
      self.board[8] = 7
      self.board[9] = 0
      self.board[10] = 2
      self.board[11] = 0
      self.board[12] = -5
      self.board[13] = 0
      self.board[14] = 0
      self.board[15] = 0
      self.board[16] = 0
      self.board[17] = -1
      self.board[18] = 0
      self.board[19] = -1
      self.board[20] = 0
      self.board[21] = 0
      self.board[22] = -1
      self.board[23] = 0
      self.board[24] = -5
      self.board[25] = 0
      self.board[26] = 0
      self.board[27] = 0

      self.turn = 1
      self.roll = []

    self.pip_count = self.getPipCount()

  def getPipCount(self):
    '''Calculate pip count'''
    w_pips = 0
    b_pips = 0

    for x in range(1, 25):
      if (self.board[x] == 0):
        continue
      elif (self.board[x] > 0):
        w_pips = w_pips + (self.board[x] * x)
      else:
        b_pips = b_pips + (int(math.fabs(self.board[x])) * (25-x))

    w_pips = int(w_pips + self.board[26] * 25)
    b_pips = b_pips + (int(math.fabs(self.board[27])) * 25)

    return (w_pips, b_pips)

  def updatePipCount(self):
    '''Update pip count'''
    self.pip_count = self.getPipCount()

  def updateFromState(self, other_state):
    '''Update a state to match another state'''
    self.roll = other_state.roll
    self.turn = other_state.turn
    self.board = other_state.board
    self.pip_count = other_state.pip_count

  def updateRoll(self, roll):
    '''Update Roll'''
    self.roll = list(roll)
    # Creates copy of roll list

  def compareStates(self, other_state):
    '''Compare a given state to another state to determine if they represent the
    same board configuration'''

    sameState = True

    if (len(self.roll) != len(other_state.roll)):
      sameState = False

    else:
      for x in range(0, 27):
        if (self.board[x] == other_state.board[x]):
          #print str(self.board[x]) + "   " + str(other_state.board[x])
          continue
        else:
          sameState = False
          #print "ORIG"
          #self.printState()
          #print "OTHER"
          #other_state.printState()
          break

    return sameState

  def compareStateToList(self, stateList):
    '''Compare state to list of states to determine if it is already in the list'''
    alreadyInList = False

    for posState in stateList:
      #counter = counter + 1
      #print "counter " +str(counter)
      if (self.compareStates(posState) == True):
        alreadyInList = True
        break

    return alreadyInList

  def switchTurn(self):
    '''Switch turn'''
    if (self.turn): #Black --> Black
      self.turn = 0
    else: #White --> Black
      self.turn = 1

  def testGameOver(self):
    '''Test game over conditions'''
    w_score = self.board[0]
    b_score = int(math.fabs(self.board[25]))

    done = -1

    if (w_score == 15):
      done = 0
    elif (b_score == 15):
      done = 1

    return done

  def allInFinalQuadrant(self):
    '''Checks if all pieces are in the final quadrant'''
    allInFQ = True
    if (self.turn):
      for x in range(1, 19):
        if (self.board[x] < 0):
          allInFQ = False
          break
    else:
      for x in range(7, 25):
        if (self.board[x] > 0):
          allInFQ = False
          break

    return allInFQ

  def lastOccupiedSpace(self):
    '''Returns tuple containing last occcupied space for both players'''
    furthest_white = 0
    furthest_black = 24

    if (self.board[26] > 0 ):
      furthest_white = 25
    if (self.board[27] < 0):
      furthest_black = 0

    for x in range(1, 25):
      if (self.board[x] > 0):
        if (x > furthest_white):
          furthest_white = x
      elif (self.board[x] < 0):
        if (x < furthest_black):
          furthest_black = x

    return (furthest_white, furthest_black)

  def furthestFromHome(self):
    '''Returns the furthest distance from home for the current player'''
    max_space = 0
    los = self.lastOccupiedSpace()

    if (self.turn):
      max_space = 25 - los[1]
    else:
      max_space = los[0]

    return max_space

  def pieceInJail(self):
    '''Returns true if current player has piece(s) in jail. Else, returns false'''
    if (self.board[26 + self.turn] != 0):
      return True
    else:
     return

  def existValidMoves(self):
    '''Check to see if valid moves exist'''
    val_moves = False

    if (len(self.roll) == 0):
      #no remaining rolls --> no valid moves
      #print "roll empty"
      return val_moves

    elif (self.pieceInJail()): #Current player has pieces in jail
      #print "Checking pieces in jail"
      space_from = 26 + self.turn
      if (self.turn): #Black
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

    else: #No pieces in Jail
      #print "no pieces in jail - checking other pieces"
      for x in range(1, 25):
        if (val_moves): #Break out of loop if valid move already found
          break

        if (self.turn): #Black
          #print "Black "
          if (self.board[x] >= 0):
            continue

          else:
            space_from = x

            for y in range(0, len(self.roll)):
              if (space_from + self.roll[y] > 25):
                pos_valid = self.checkSpaceTo(space_from, 25)
              else:
                pos_valid = self.checkSpaceTo(space_from, space_from + self.roll[y])

        else: #White
          #print "White ",
          if (self.board[x] <= 0):
            continue
          else:
            space_from = x
            for y in range(0, len(self.roll)):
              if (space_from + self.roll[y] < 0):
                pos_valid = self.checkSpaceTo(space_from, 0)
              else:
                pos_valid = self.checkSpaceTo(space_from, space_from - self.roll[y])


        if (pos_valid[0]):
          val_moves = True

    return val_moves

  def checkFwdMove(self, space_from, space_to):
    '''Ensure inputted move is a forward move'''
    fwd = True

    if (self.turn): #Black
      if (space_to < space_from):
        fwd = False
    else:
      if (space_to > space_from):
        fwd = False

    return fwd

  def checkSpaceTo(self, space_from, space_to):
    '''Check if desired space to move to is legal'''
    orig_space_from = space_from
    orig_space_to = space_to

    if (space_to <= 0):
      space_to = 0
    elif (space_to >= 25):
      space_to = 25

    valid_move = True

    if (space_from >= 26): #Moving piece from jail
      if (self.turn): #Black
        space_from = 0
      else: #White
        space_from = 25

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

    if (self.turn == 0 ): #White moving to black space
      if (self.board[space_to] < -1):
        valid_move = False
        move_dist = -4
        return (valid_move, orig_space_from, space_to, move_dist)

    elif (self.turn == 1): #Black moving to white space
      if (self.board[space_to] > 1):
        valid_move = False
        move_dist = -4
        return (valid_move, orig_space_from, space_to, move_dist)

    if (self.roll.count(move_dist) == 0):
      valid_move = False
      move_dist = -5
      return (valid_move, orig_space_from, space_to, move_dist)

    return (valid_move, orig_space_from, space_to, move_dist)

  def checkGammon(self, winner):

    if (winner == -1):
      return 0

    last_white, last_black = self.lastOccupiedSpace()

    points_for_win = 1

    if (winner == 0): #white won
      if (self.board[25] == 0):
        if (last_black < 7):
          points_for_win = 3
        else:
          points_for_win = 2

    if (winner == 1): #black won
      if(self.board[0] == 0):
        if(last_white > 18):
          points_for_win = 3
        else:
          points_for_win = 2

    return points_for_win

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

  def printState(self):
    print str(self)

  def __str__(self):
    return_string = '\n'

    if (self.turn == 0):
      return_string = return_string + "White's Turn" + "\n"
    else:
      return_string = return_string + "Black's Turn" + "\n"

    return_string = return_string + str(self.roll) + "\n"
    return_string = return_string + "White pip count: " + str(self.pip_count[0])
    return_string = return_string + " Black pip count: " + str(self.pip_count[1])
    return_string = return_string + "\n"
    return_string = return_string + self.convBoardToString()

    return return_string



  def convBoardToString(self):
    return_string = ""

    for x in range(0, len(self.board)):
      if (x == 0):
        return_string = return_string + "White Points Scored: "
        for y in range (0, int(math.fabs(self.board[x]))):
          return_string = return_string + "o "
        return_string = return_string + "\n"
      elif (x > 0 and x < 25):
        return_string = return_string + str(x) + ": "
        for y in range(0, int(math.fabs(self.board[x]))):
          if (self.board[x] > 0):
            return_string = return_string + "o "
          else:
            return_string = return_string + "x "
        return_string = return_string + "\n"
      elif (x == 25):
        return_string = return_string + "Black Points Scored: "
        for y in range(0, int(math.fabs(self.board[x]))):
          return_string = return_string + "x "
        return_string = return_string + "\n\n"
      elif (x == 26):
        return_string = return_string + "White Jail: "
        for y in range (0, int(math.fabs(self.board[x]))):
          return_string = return_string + "o "
        return_string = return_string + "\n"
      else:
        return_string = return_string + "Black Jail: "
        for y in range (0, int(math.fabs(self.board[x]))):
          return_string = return_string + "x "
        return_string = return_string + "\n"

    return return_string
