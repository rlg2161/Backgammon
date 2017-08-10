import copy
import math
import random

import lib.state as state


def playRandCompTurn(state):
  '''Calculate and return a valid, random Computer move'''
  space_from = getCompSpaceFrom(state)
  space_to = getCompSpaceTo(state, space_from)
  space_to_valid = state.checkSpaceTo(space_from, space_to)

  return space_to_valid

def getCompSpaceFrom(state):
  '''Get space_from for computer player'''
  if (state.board[26 + state.turn] != 0):
    #print "Computer must move piece from Jail. "
    space_from = 26 + state.turn
    return space_from

  else:
    roll_copy = copy.deepcopy(state.roll)
    roll_copy.sort()
    test = roll_copy.pop()
    if (state.allInFinalQuadrant()):
      #All pieces in final quadrant
      if (state.furthestFromHome() <= test):
        # If largest roll is greater than or equal to distance from home of farthest piece
        if (state.turn == 0):
          space_from = state.furthestFromHome()
        else:
          space_from = 25 - state.furthestFromHome()
      else:
        #If largest roll is smaller than furthest away piece
        move_from = False
        while(move_from == False):
          test_space = int(math.floor(random.random()*24) + 1)
          if ((state.board[test_space] > 0 and state.turn == False) or (state.board[test_space] < 0 \
            and state.turn == True)):
            move_from = True
            space_from = test_space
    else:
      # No pieces in jail and not all in final quadrant
      move_from = False
      while(move_from == False):
        test_space = int(math.floor(random.random()*24) + 1)
        if ((state.board[test_space] > 0 and state.turn == False) or (state.board[test_space] < 0 \
            and state.turn == True)):
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

  if (state.turn == 1):
    if (space_from == 26 + state.turn):
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


  elif (state.turn == 0):
    if (space_from == 26 + state.turn):
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
