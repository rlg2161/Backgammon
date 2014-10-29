# Represents a turn 

class turn():
  '''Represents whose turn it is and what type of player they are'''

  def __init__(self, num):
    self.turn = num

  def __str__(self):
    if (self.turn):
      r_string = "Black's turn ('x') "
    else:
      r_string = "White's turn ('o') "
    return r_string

  def switchTurn(self):
    '''Switch turn from black to white or vice versa'''
    if (self.turn == 0):
      next_turn = True
    else:
      next_turn = False

    self.turn = next_turn