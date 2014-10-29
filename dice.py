# Dice class and associated methods

import math
import random
import turn

class oneDie():
  '''Represents one die (of variable side number)'''
  def __init__(self, sides = None):
    if (sides is None):
      self.num_sides = 6
    else:
      self.num_sides = sides

#def roll(self):
  #get_roll = math.floor(random.random()*(self.num_sides)) + 1
  #return int(get_roll)

  def rollDie(self):
    '''Rolls 2 die (returns 4 die if doubles)'''
  
    roll1 = int(math.floor(random.random()*(self.num_sides)) + 1)
    roll2 = int(math.floor(random.random()*(self.num_sides)) + 1)

    if (roll1 == roll2):
      totalRoll = [roll1, roll1, roll1, roll1]

    else:
      totalRoll = [roll1, roll2]

    #totalRoll.sort()
    return totalRoll
 
  def goesFirst(self):
    '''Rolls dice to see who goes first. Re-rolls on doubles and returns the \
    combined roll'''

    roll1 = int(math.floor(random.random()*(self.num_sides)) + 1)
    roll2 = int(math.floor(random.random()*(self.num_sides)) + 1)

    #print [roll1, roll2]

    while (roll1 == roll2):
      roll1 = int(math.floor(random.random()*(self.num_sides)) + 1)
      roll2 = int(math.floor(random.random()*(self.num_sides)) + 1)

    if (roll1 > roll2):
      t = turn.turn(0)
      # i.e. Player 1 (white) goes first

    else:
      t = turn.turn(1)
      #i.e. Player 2 (black) goes first
  
    totalRoll = [roll1, roll2]
    #totalRoll.sort()

    #print t

    return (t, totalRoll)