# Contains methods to validate moves but not logic for calculating moves.
import copy
import math
import state

def genAllPossMoves(posStates):
  '''Recursively generate all possible moves given a game-state'''
  if (len(posStates) > 10000):
    print "Runaway recursion :( - game exited"
    overflowMovesList = open('overflowMovesList.txt', 'w')
    for item in posStates:
      overflowMovesList.write(str(item))
    overflowMovesList.close()
    print len(posStates)
    exit(1)
  givenState = posStates[0]

  if (givenState.existValidMoves() == False):
    test = False
    for st in posStates:
      if (st.existValidMoves() == True):
        test = True
        break

    if (test == True):
      posStates.remove(givenState)
      genAllPossMoves(posStates)

    else:
      return posStates


  else: #There exists at least one valid move
    # CURRENT PLAYER HAS PIECE IN JAIL
    if ((givenState.turn == 0 and givenState.board[26] > 0 or \
      givenState.turn == 1 and givenState.board[27] < 0)):
      #print "piece in jail"

      for x in range(0, len(givenState.roll)):
        cpy_state = state.state(givenState)
        if (cpy_state.turn == 0): #White
          space_to_valid = cpy_state.checkSpaceTo(26, 25 - cpy_state.roll[x])
        else: # Black
          space_to_valid = cpy_state.checkSpaceTo(27, cpy_state.roll[x])
        #### IF VALID MOVE, THEN EXECUTE
        if (space_to_valid[0] == True):

          #UPDATE values
          space_from = space_to_valid[1]
          space_to = space_to_valid[2]
          move_dist = space_to_valid[3]

          # REMOVE piece being moved
          if (cpy_state.turn): #Black
            cpy_state.board[27] = cpy_state.board[27] + 1
          else: #White
            cpy_state.board[26] = cpy_state.board[26] - 1


          # CAPTURE opponent piece and put it in jail
          if ((cpy_state.board[space_to] < 0 and cpy_state.turn == False) or \
            (cpy_state.board[space_to] > 0 and cpy_state.turn == True)):
            if (int(math.fabs(cpy_state.board[space_to])) == 1):
              if (cpy_state.turn): #Black
                cpy_state.board[26] = cpy_state.board[26] + 1
              else: #White
                cpy_state.board[27] = cpy_state.board[27] - 1
              cpy_state.board[space_to] = 0

          # ADD piece to new space
          if (cpy_state.turn): #Black
            cpy_state.board[space_to] = cpy_state.board[space_to] - 1
          else: #White
            cpy_state.board[space_to] = cpy_state.board[space_to] + 1

          cpy_state.roll.remove(cpy_state.roll[x])
          cpy_state.updatePipCount()

          if (cpy_state.compareStateToList(posStates) == False):
            #print "not getting here?"
            posStates.append(cpy_state)


    # CURRENT PLAYER HAS NO PIECES IN JAIL
    else:
      for x in range(1, 25):

        # No one to move
        if (givenState.board[x] == 0):
          continue

        # Current space owned by other player
        elif ((givenState.board[x] < 0 and givenState.turn == 0) \
          or (givenState.board[x] > 0 and givenState.turn == 1)):
          #print "wrong color"
          continue

        # Current space a valid space_from
        else:
          for y in range(0, len(givenState.roll)):
            cpy_state = state.state(givenState)
            if (cpy_state.turn == 0): #White
              space_to_valid = cpy_state.checkSpaceTo(x, x - cpy_state.roll[y])
            else: #Black
              space_to_valid = cpy_state.checkSpaceTo(x, x + cpy_state.roll[y])
            #print space_to_valid
            if (space_to_valid[0] == True):
              #print "Exist valid move?"
              space_from = space_to_valid[1]
              space_to = space_to_valid[2]
              move_dist = space_to_valid[3]

              # Execute move
              if (cpy_state.turn == 1): #Black
                cpy_state.board[space_from] = cpy_state.board[space_from] + 1
              elif (cpy_state.turn == 0): #White
                cpy_state.board[space_from] = cpy_state.board[space_from] - 1


              # Capture opponent piece and put it in jail
              if ((cpy_state.board[space_to] < 0 and cpy_state.turn == 0) or \
                (cpy_state.board[space_to] > 0 and cpy_state.turn == 1)):
                if (int(math.fabs(cpy_state.board[space_to])) == 1):
                  if (cpy_state.turn): #Black
                    cpy_state.board[26] = cpy_state.board[26] + 1
                  else: #White
                    cpy_state.board[27] = cpy_state.board[27] - 1
                  cpy_state.board[space_to] = 0

              if (cpy_state.turn): #Black
                cpy_state.board[space_to] = cpy_state.board[space_to] - 1
              else: #White
                cpy_state.board[space_to] = cpy_state.board[space_to] + 1

              cpy_state.roll.remove(cpy_state.roll[y])
              cpy_state.updatePipCount()

              if (cpy_state.compareStateToList(posStates) == False):
                posStates.append(cpy_state)
                #cpy_state.printState()
          #print x
          #print len(posStates)

    #print len(posStates)
    posStates.remove(givenState)
    #print len(posStates)
    genAllPossMoves(posStates)


def elimInvalidMoves(stateList):
  '''Eliminates moves from stateList that are not "complete" turns (i.e. not all
    dice are used) so that they can not be considered and illegally returned by
    move checking functions'''
  if (len(stateList) == 1):
    return stateList

  else:
    new_list = []

    for state in stateList:
      if (len(state.roll) == 0 or state.testGameOver() >= 0):
        new_list.append(state)

    if (len(new_list) > 0):
      return new_list


    else:
      min_pip_sum = 1000

      for state in stateList:
        tempW, tempB = state.getPipCount()
        if ((tempW + tempB) < min_pip_sum):
          min_pip_sum = (tempW + tempB)

      for state in stateList:
        tempW, tempB = state.getPipCount()
        if ((tempW + tempB) <= min_pip_sum):
          new_list.append(state)

      if (len(new_list) ==0):
        print "Error in elimInvalidMoves"
        print len(stateList)
        for item in stateList:
          item.printState()
        exit(1)

      return new_list
