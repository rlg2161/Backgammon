class stateTreeNode():

  def __init__(self, state, stateValue):
    ''' Construct a state tree node'''
  
    self.nodeState = state #Actual state of the game
    self.score = stateValue
    self.child = None
    self.firstSibling = None

      
  def addChild(self, stateTreeNode):
    self.child = stateTreeNode

  def addSibling(self, stateTreeNode):
    self.firstSibling = stateTreeNode

  def updateScore(self, num):
    self.score = num

  
 
  def __str__(self):
    return_string = "Score of state: " + str(self.score) + "\n"
    return_string = return_string + str(self.nodeState)

    return return_string

  def __len__(self):
    #FIX THIS
    
    if (self == None):
      return 0

    elif (self.child == None and self.firstSibling == None):
      return 1

    else:
      counter = 1
      if (self.child != None):
        counter = counter + len(self.child)
      if (self.firstSibling != None):
        counter = counter + len(self.firstSibling)
      
      return counter


