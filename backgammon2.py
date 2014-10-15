# A basic backgammon game that interfaces with console

import math
import random


WHITE = 0
BLACK = 1

def main():
  
  b = board()
  b.initBoard()

  b.printBoard()


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
    c = self.c
    if (c == WHITE):
      return 0
    elif (c == BLACK):
      return 25

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
        print "    " + str(cur_space.color),
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
        print ""
      else:
        print "Black Jail: ",
        for y in range(0, len(cur_space.s)):
          print cur_space.s[y]
        print ""
    print ""  


if __name__ == "__main__":
  main()

