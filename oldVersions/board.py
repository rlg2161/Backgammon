# Represents the backgammon playing board

import copy
import space

class board():
  '''Represents the board'''

  def __init__(self):
    self.spaceList = []
    for x in range(0,26):
      s = space.space()
      self.spaceList.append(s)
    js = space.jailSpace(0)
    self.spaceList.append(js)
    js = space.jailSpace(1)
    self.spaceList.append(js)

  def __str__(self):
    return_string = ""
    
    for x in range(0, len(self.spaceList)):
      cur_space = self.spaceList[x]
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


  def updateFromState(self, state):
    self.spaceList = copy.deepcopy(state.board.spaceList)
    #self.spaceList.printBoard()

  def getPipCount(board):
    b_pips = 0
    w_pips = 0

    for x in range(1, 25):
      #print type(b)
      cur_col = board.spaceList[x].getColor()

      if (cur_col == -1):
        continue

      elif (cur_col == 0):
        space_pip_count = len(board.spaceList[x]) * x
        w_pips = w_pips + space_pip_count
      
      else:
        space_pip_count = len(board.spaceList[x]) * (25 -x)
        b_pips = b_pips + space_pip_count

    # Calc dist for pieces in white jail
    space_pip_count = len(board.spaceList[26]) * 25
    w_pips = w_pips + space_pip_count

    space_pip_count = len(board.spaceList[27]) * 25
    b_pips = b_pips + space_pip_count

    return (w_pips, b_pips)

  def getScore(self):
    w_score = len(self.spaceList[0])
    b_score = len(self.spaceList[25])
    return (w_score, b_score)

  def initBoard(self):
    
    # NORMAL SETUP IN BELOW BLOCK

    self.spaceList[1].fillSpace(1, 2)
    self.spaceList[6].fillSpace(0, 5)
    self.spaceList[8].fillSpace(0, 3)
    self.spaceList[12].fillSpace(1, 5)
    self.spaceList[13].fillSpace(0, 5)
    self.spaceList[17].fillSpace(1, 3)
    self.spaceList[19].fillSpace(1, 5)
    self.spaceList[24].fillSpace(0, 2)

    #Board configuration for testing endgame
    #self.spaceList[0].fillSpace(0,2)
    #self.spaceList[1].fillSpace(0,2)
    #self.spaceList[2].fillSpace(0,2)
    #self.spaceList[3].fillSpace(0,2)
    #self.spaceList[4].fillSpace(0,3)
    #self.spaceList[5].fillSpace(0,3)
    #self.spaceList[6].fillSpace(0,3)
    #self.spaceList[7].fillSpace(0,2)
    #self.spaceList[8].fillSpace(0,2)
    #self.spaceList[9].fillSpace(0,2)
    #self.spaceList[10].fillSpace(0,3)
    #self.spaceList[11].fillSpace(0,3)
    #self.spaceList[12].fillSpace(0,3)
    #self.spaceList[19].fillSpace(1,3)
    #self.spaceList[20].fillSpace(1,3)
    #self.spaceList[21].fillSpace(1,3)
    #self.spaceList[22].fillSpace(1,2)
    #self.spaceList[23].fillSpace(1,2)
    #self.spaceList[24].fillSpace(1,2)
    #self.spaceList[25].fillSpace(1, 15)
    #self.spaceList[26].fillSpace(0, 3)
    #self.spaceList[27].fillSpace(1,3)

  def printBoard(self):
    for x in range(0, len(self.spaceList)):
      cur_space = self.spaceList[x]
      if (x == 0):
        print "White Points Scored: ",
        print str(cur_space)
        #for y in range(0, len(cur_space)):
          #print cur_space.s[y],
        #print ""
      elif (x > 0 and x < 25):
        print str(x) + ": ",
        print str(cur_space)
        #for y in range(0, len(cur_space.s)):
          #print cur_space.s[y],
        #print "    " + str(cur_space.color),
        #print ""
      elif (x == 25):
        print "Black Points Scored: ",
        print str(cur_space)
        #for y in range(0, len(cur_space.s)):
          #print cur_space.s[y],
        #print ""
        print ""
      elif (x == 26):
        print "White Jail: ",
        print str(cur_space)
        #for y in range(0, len(cur_space.s)):
          #print cur_space.s[y],
        #print "    " + str(cur_space.color),
        #print ""
      else:
        print "Black Jail: ",
        print str(cur_space)
        #for y in range(0, len(cur_space.s)):
          #print cur_space.s[y],
        #print "    " + str(cur_space.color),
        #print ""
    print "" 

  

