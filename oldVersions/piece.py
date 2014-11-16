# Represents a piece class in backgammon

class piece():
  '''Represents a board piece'''

  def __init__(self, color):
    if (color):
      self.color = 1
    else:
      self.color = 0

  def __str__(self):
    if (self.color):
      return 'x'
    else:
      return 'o'