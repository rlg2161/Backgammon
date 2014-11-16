# Represents a backgammon board space

import piece

class space():
  '''Object represents a space on the board'''

  def __init__(self):
    self.s = []
    self.color = -1

  def updateColor(self, color):
    self.color = color

  def getColor(self):
    return self.color

  def peek(self):
    temp = self.s.pop()
    piece = temp
    self.s.append(temp) 
    return piece

  def fillSpace(self, color, number):
    for x in range (0, number):
      p = piece.piece(color)
      self.s.append(p)
    self.updateColor(color)

  def __len__(self):
    return len (self.s)

  def __str__(self):
    space_string = ""
    if (self.color): #If space is black
      for x in range(0, len(self)):
        space_string = space_string + "x "
    else:
      for x in range(0, len(self)):
        space_string = space_string + "o "

    return space_string



class jailSpace(space):
  '''Represents a jail space'''

  def __init__(self,col):
    self.s = []
    self.color = col

  def getMoveFrom(self):
    c = self.color
    if (c == 0):
      return 25
    elif (c == 1):
      return 0