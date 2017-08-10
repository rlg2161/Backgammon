# Methods for strategies that calculate move value based on heurstics programmed by Yours Truly
# but lifted from paper referenced in README

import lib.move as move
import lib.state as state
import lib.stateTreeNode as stateTreeNode

import math
import random

def moveWithStateTree(state):
  '''Move for computer when using state tree based strategy for forecasting'''
  root = generateMoveTree(state)
  best_move = calcMoveFromStateTree(root)
  if (best_move != None):
    return best_move.nodeState
  else:
    return state

def playStrategicCompTurn(state):
  '''Plays a computer turn if a non-random strategy is being played'''
  posStates = [state]
  move.genAllPossMoves(posStates)

  best = evalMoves(posStates)
  return best

def calcMoveFromStateTree(root):
  posMove = root.child
  best_move = posMove
  move_val = -100000

  while (posMove != None):
    if (posMove.score > move_val):
      best_move = posMove
      move_val = posMove.score
    posMove = posMove.firstSibling

  return best_move

def generateMoveTree(st):
  '''Generate all possible game states two moves out and put it in a tree'''
  listOfRolls = [ [1,1,1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2,2,2], [2,3],\
  [2,4], [2,5], [2,6], [3,3,3,3], [3,4], [3,5], [3,6], [4,4,4,4], [4,5], [4,6],\
  [5,5,5,5], [5,6], [6,6,6,6] ]

  stateTreeFile = open('stateTreeFile.txt', 'w')
  stateScore = calcMoveValue1(st, st.turn)
  root = stateTreeNode.stateTreeNode(st, stateScore)

  if (root == None):
    #print "continue"
    return root
  else:
    genMoveTree(root, root.nodeState.turn)
    #print "Len root after genMoveTree(): " + str(len(root))

    return root


def genMoveTree(root, turn):
  '''Given a root (i.e. state), calculate all possible states (w/ move.genAllPossMoves()) and then
  calculate the average score of opponent when move.genAllPossMoves() is calculated for each
  roll for each given state'''
  listOfRolls = [ [1,1,1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2,2,2], [2,3],\
  [2,4], [2,5], [2,6], [3,3,3,3], [3,4], [3,5], [3,6], [4,4,4,4], [4,5], [4,6],\
  [5,5,5,5], [5,6], [6,6,6,6] ]

  #print "genMoveTree()"
  rState = root.nodeState
  #print rState
  stateList = [rState]

  if (rState.existValidMoves() == False):
    #print "no valid moves"
    # elim extra generation when no moves exist
    return

  else:
    move.genAllPossMoves(stateList)
    stateList = threeBestMoves(stateList)
    #print "len(stateList): " + str(len(stateList))

    #counter = 0
    if (len(stateList) == 1):
      if (stateList[0].turn == 0):
        nextNodeScore = calcMoveValue2(stateList[0], 1)
      else:
        nextNodeScore = calcMoveValue2(stateList[0], 0)
      nextNode = stateTreeNode.stateTreeNode(stateList[0], nextNodeScore)
      root.addChild(nextNode)
      return


    if (len(stateList) >= 1):
      #print "comparing similar moves"
      for item in stateList:
        #counter = counter + 1
        #print "counter: " + str(counter)
        nextNodeScore = 0
        nextNode = stateTreeNode.stateTreeNode(item, nextNodeScore)

        cumeScore = 0
        for roll in listOfRolls:
          cpy_state = state.state(item)
          cpy_state.updateRoll(roll)
          cpy_state.switchTurn()
          oppStateList = [cpy_state]
          move.genAllPossMoves(oppStateList)
          move.elimInvalidMoves(oppStateList)
          for x in range(0, len(oppStateList)):

            mv_val = calcMoveValue2(oppStateList[x], cpy_state.turn)
            if (roll == listOfRolls[0] or roll == listOfRolls[6] or roll == listOfRolls[11]\
              or roll == listOfRolls[15] or roll == listOfRolls[18] or roll == listOfRolls[20]):
              mv_val = mv_val/2 #acct for fact that these rolls are half as likely as other rolls
            #print mv_val
            #raw_input("wait")
            cumeScore = cumeScore + mv_val
        cumeScore = cumeScore/len(oppStateList)
        #print cumeScore
        nextNode.updateScore(cumeScore)


        if (root.child == None):
          #print "adding child"
          root.addChild(nextNode)
        else:
          #print "adding sibling"
          sib = root.child.firstSibling
          if (sib == None):
            root.child.addSibling(nextNode)
          else:
            while (sib.firstSibling != None):
              sib = sib.firstSibling
            sib.addSibling(nextNode)

      return

def threeBestMoves(stateList):
  '''Identify and return list of up to 3 best possible moves for player given all poss states'''
  best = -10000
  bestState = None
  best2 = -10000
  best2State = None
  best3 = -10000
  best3State = None

  for st in stateList:
    move_val = calcMoveValue1(st, st.turn)
    if (move_val > best):
      temp1 = best
      temp1State = bestState
      temp2 = best2
      temp2State = best2State

      best = move_val
      bestState = st
      best2 = temp1
      best2State = temp1State
      best3 = temp2
      best3State = temp2State
      #print "best"
      continue

    elif (move_val > best2):
      temp2 = best2
      temp2State = best2State

      best2 = move_val
      best2State = st
      best3 = temp2
      best3State = temp2State
      #print "second best"
      continue

    elif (move_val > best3):
      best3 = move_val
      best3State = st
      #print "third best"
      continue

  bestList = [bestState]
  if (best2State != None):
    if (math.fabs(best2 - best) < 1):
      bestList.append(best2State)
  if (best3State != None):
    if (math.fabs(best3 - best) < 1):
      bestList.append(best2State)

  #for item in bestList:
    #print str(item)

  return bestList


def evalMoves(posStates):
  '''Evaluate all moves in a list and return move with the highest score'''
  cur_max = -1000000
  best_move = []

  move.elimInvalidMoves(posStates)

  for x in range(0, len(posStates)):

    temp = calcMoveValue1(posStates[x], posStates[x].turn)
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

def calcMoveValue1(state, turn):
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
  if (turn == 0): #White
      # Points for opp pieces in jail
      opp_jail_score = 8*((math.fabs(state.board[27])))
      # Points for scoring pieces
      points_scored = 4*(state.board[0])

  else: #Black
    opp_jail_score = 8*((state.board[26]))
    points_scored = 4*(state.board[25])


  for x in range(0, 25):

    if ((state.board[x] >= 0 and turn == 1) or \
      (state.board[x] <=0 and turn == 0)):
      blocade_count = 0
      continue

    else:
      # Points for uncovered pieces
      if (int(math.fabs(state.board[x])) == 1):
        blot_points = 0
        blocade_count = 0
        if (state.turn == 0): #White
          if (x > last_black_space):
            blot_points = 5 * ((25-x)*.125)
        elif (state.turn == 1): #Black
          if (x < last_white_space):
            blot_points = 5*((x)*.125)

        uncovered_score = uncovered_score + blot_points

      # Points for blocades
      if (int(math.fabs(state.board[x])) >= 2):
        covered_score += 1
        blocade_count += 1
        if (blocade_count > 1):
          blocade_score += blocade_count*2

  move_value = points_scored + opp_jail_score + blocade_score + covered_score - uncovered_score
  return move_value

def calcMoveValue2(state, turn):
  '''Alternate method for calculating move value'''
  own_jail_score = 0
  blot_score = 0
  blocade_score = 0
  points_scored = 0
  blocade_count = 0
  last = state.lastOccupiedSpace()

  if (turn == 0):
    own_jail_score = 8*((math.fabs(state.board[26])))
    points_scored = 4*state.board[0]
  else:
    own_jail_score = 8*((math.fabs(state.board[27])))
    points_scored = 4*state.board[25]

  for x in range(0, 25):

    if ((state.board[x] >= 0 and turn == 1) or \
      (state.board[x] <=0 and turn == 0)):
      blocade_count = 0
      continue
    else:
      if (int(math.fabs(state.board[x])) == 1):
        blot_points = 0
        if (turn == 0): #White
          if (x > last[1]): # Not behind black's last piece
            blot_points = 5 * ((25-x)*.2)
        elif (turn == 1): #Black
          if (x < last[0]): # Not behing white's last piece
            blot_points = 5 * ((x)*.2)
        blot_score = blot_score + blot_points

      if (int(math.fabs(state.board[x])) >=2):
        blocade_count += 1
        if (blocade_count > 1):
          blocade_score += blocade_count*2


  move_value = own_jail_score + blot_score - points_scored - blocade_score
  return move_value
