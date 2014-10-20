# Dice class and associated methods

import math
import random

class oneDie():
  '''Represents one die (of variable side number)'''
  def __init__(self, sides = None):
    if (sides is None):
      self.num_sides = 6
    else:
      self.num_sides = sides

  def roll(self):
    get_roll = math.floor(random.random()*(self.num_sides)) + 1
    return int(get_roll)