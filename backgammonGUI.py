# Basic GUI for my backgammon program

import Tkinter
import backgammon as bg 
import random
import math
import dice
import time

# CONFUSED ABOUT OBJECT HIERARCHY

canvasWidth = 520
canvasHeight = 260


class backgammonGUI():
  

  
  # Functions and Methods
  def redraw(self, state):
    self.drawBoard()
    self.drawPieces(state)
      
    self.board.pack()

  def drawBoard(self):

    self.board.create_rectangle(0,0, canvasWidth, canvasHeight, fill = '#CCCCCC')

    space_width = 38
    space_height = 100

    for x in range(0,6):
      coordTop = (space_width*x), 0, space_width + (space_width*x), 0,\
      ((space_width*x) + (space_width +space_width*x))/2, space_height
      coordBottom = (space_width*x), 260, space_width + (space_width*x), 260, \
      (((space_width*x)) + (space_width + space_width*x))/2, canvasHeight - space_height
      if (x % 2 == 0):
        color = '#522900'
        opp_color = '#FFFFCC'
      else:
        color = '#FFFFCC'
        opp_color = '#522900'

      self.board.create_polygon(coordTop, outline = color, fill = color)
      self.board.create_polygon(coordBottom, outline = opp_color, fill = opp_color)
      
    self.board.create_rectangle(228, 0, 255, 260, outline = '#6B4724', fill = '#6B4724')

    for x in range(0, 6):
      coordTop = 255 + (space_width*x), 0, 255 + space_width + (space_width*x), 0, \
      ((255 + (space_width*x)) + (255 + space_width + space_width*x))/2, space_height 
      coordBottom = 255 + (space_width*x), 260, 255 + space_width + (space_width*x), 260, \
      ((255 + (space_width*x)) + (255 + space_width + space_width*x))/2, canvasHeight - space_height 
      if (x % 2 == 0):
        color = '#522900'
        opp_color = '#FFFFCC'
      else:
        color = '#FFFFCC'
        opp_color = '#522900'

      self.board.create_polygon(coordTop, outline = color, fill = color)
      self.board.create_polygon(coordBottom, outline = opp_color, fill = opp_color)

    self.board.create_rectangle(483, 0, 520, 130, fill = '#522900')
    self.board.create_rectangle(483, 260, 520, 130, fill = '#FFFFCC')

  def drawPieces(self, state):
    
    #first quadrant
    for x in range(6, 0 , -1):
      if (state.board[x] > 0):
        color = '#FFFFFF'
      else:
        color = '#A37547'
      if (int(math.fabs(state.board[x])) < 6):
        for y in range(0, int(math.fabs(state.board[x]))):
          coords = ((38*(6-x))+255) + 9 , 0 + 20*y, (293 + (38*(6-x)))-9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0, 6):
          coords = ((38*(6-x))+255) + 9 , 0 + 20*y, (293 + (38*(6-x)))-9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(255 + (38*(6-x)) + 20, 110, text = str(int(math.fabs(state.board[x]))))

     
    #second quadrant
    for x in range(12, 6, -1):
      if (state.board[x] > 0):
        color = '#FFFFFF'
      else:
        color = '#A37547'
      if (int(math.fabs(state.board[x]))<6):
        for y in range(0, int(math.fabs(state.board[x]))):
          coords = (38*(12-x))+ 9, 0 + 20*y, (38 + (38*(12-x))) - 9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0,6):
          coords = (38*(12-x))+ 9, 0 + 20*y, (38 + (38*(12-x))) - 9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(38*(12-x) +20, 110, text = str(int(math.fabs(state.board[x]))))

    # third quadrant
    for x in range(18, 12, -1):
      if (state.board[x]  > 0):
        color  = '#FFFFFF'
      else:
        color = '#A37547'
      if (int(math.fabs(state.board[x])) < 6):
        for y in range(0, int(math.fabs(state.board[x]))):
          coords = (38*(x-13)) + 9, 260 - 20*y, 38 + (38*(x-13)) - 9, 240 - 20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0,6):
          coords = (38*(x-13))+9, 260 - 20*y, 38 + (38*(x-13)) - 9, 240 - 20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(38*(x-13) + 20, 150, text = str(int(math.fabs(state.board[x]))))
     
    #fourth quadrant
    for x in range(24, 18, -1):
      if (state.board[x] > 0):
        color = '#FFFFFF'
      else:
        color = '#A37547'
      if (int(math.fabs(state.board[x])) < 6):
        for y in range(0, int(math.fabs(state.board[x]))):
          coords = (38*(x-13) + 27) + 9, 260 - 20*y, 65 + (38*(x-13)) -9, 240 -  20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0,6):
          coords = (38*(x-13) + 27) + 9, 260 - 20*y, 65 + (38*(x-13)) -9, 240 -  20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(38*(x-13) +27 + 20, 150, text = str(int(math.fabs(state.board[x]))))
    
    # home spaces
    for x in range(0, int(math.fabs(state.board[0]))):
      coords = 485, 15 + (8*x), 518, 5 + (8*x)
      self.board.create_rectangle(coords, fill = '#FFFFFF')

    for x in range(0, int(math.fabs(state.board[25]))):
      coords = 485, 258 - (8*x), 518, 250 - (8*x)
      self.board.create_rectangle(coords, fill = '#A37547')


    #jail
    for x in range(0, int(math.fabs(state.board[26]))):
      coords = 231 , 127 - 20*x, 251  , 107 - 20*x
      self.board.create_oval(coords, fill = '#FFFFFF')

    for x in range(0, int(math.fabs(state.board[27]))):
      coords = 231, 133 + 20*x, 251, 153 + 20*x
      self.board.create_oval(coords, fill = '#A37547')

  def __init__(self, factors_list):

    self.factors_list = factors_list
    print self.factors_list
    self.moveFrom = -1
    self.moveTo = -1

    
    self.die = dice.oneDie(6)
    self.state = bg.createInitialState(self.die)
    #winner = -1 

    cur_roll = self.state.roll

    if (self.state.turn == 0):
      text_turn = "White's turn  "
    else:
      text_turn = "Black's turn  "
    
    #winner = state.testGameOver()

    # GUI instructions

    # Create main window
    self.main_window = Tkinter.Tk()
    self.main_window.title('Backgammon')

    # Create board frame
    self.board_frame = Tkinter.Frame()       # Display the board
    
    # Create frames for move buttons
    self.top_button_frame = Tkinter.Frame()     # Contains position buttons
    self.bottom_button_frame = Tkinter.Frame()

    # Makes frame for higher level buttons/display
    #self.roll_frame = Tkinter.Frame()
    self.control_frame = Tkinter.Frame()


    # Button Methods
    
    def newGameButton():
      print "\n\n\n"
      self.state = bg.createInitialState(self.die)
      cur_roll = self.state.roll

      if (self.state.turn == 0):
        text_turn = "White's turn  "
      else:
        text_turn = "Black's turn  "

      roll_message = 'Roll: ' + str(self.state.roll)
      self.roll.set(roll_message)
      self.turn.set(text_turn)
      self.redraw(self.state)

      if (self.state.turn == 1):
        print roll_message
        #self.state = bg.playStrategicCompTurn(self.state)
        bg.playCompTurn(self.state, 4, False self.factors_list)
      
        self.redraw(self.state)

        # Update and return move to other player
        r = self.die.rollDie()
        self.state.updateRoll(r)
        self.state.switchTurn()
      
        roll_message = 'Roll: ' + str(self.state.roll)
        self.roll.set(roll_message)
        turn_message = "White's Turn"
        self.turn.set(turn_message)


    def undoButton():
      print "Not implemented yet"

    def hereButton(number):
      if (len(self.state.roll) > 0):
        if (self.moveFrom == -1):
          self.moveFrom = number
        else:
          self.moveTo = number
          space_to_valid = self.state.checkSpaceTo(self.moveFrom, self.moveTo)
          if (space_to_valid[0]):
            #play
            space_from = space_to_valid[1]
            space_to = space_to_valid[2]
            move_dist = space_to_valid[3]

            # Execute move
            self.state.board[space_from] = self.state.board[space_from] - 1
          
          
            # Capture opponent piece and put it in jail
            if ((self.state.board[space_to] < 0 and self.state.turn == False)):
              if (int(math.fabs(self.state.board[space_to])) == 1):
                self.state.board[27] = self.state.board[27] - 1
                self.state.board[space_to] = 0

            # Move to space to
            self.state.board[space_to] = self.state.board[space_to] + 1
          
            #print state.roll
            self.state.roll.remove(move_dist)
            roll_message = 'Roll: ' + str(self.state.roll)
            self.roll.set(roll_message)
            self.state.updatePipCount()

          
            self.redraw(self.state)
            self.moveFrom = -1
            self.moveTo = -1 


          else:
            # Reset to allow moves to move retrevial to work
            self.moveFrom = -1
            self.moveTo = -1 
      

    def placeholderButton(num):
      self.moveFrom = int(num)
      print (self.moveFrom, self.moveTo)

    

    # Board Frame
    self.board = Tkinter.Canvas(self.board_frame, width = canvasWidth, height = canvasHeight)

    
    
    # Movement buttons
    #for x in range(0, 6):
      
    # Top Left
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(12))
    here_button.grid(row = 0, column = 0, columnspan = 1)
    #here_button.bind('<Button-1>', self.play(12))

    # Bottom Left
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(13))
    here_button.grid(row = 0, column = 0, columnspan = 1)

    # Top Left
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(11))
    here_button.grid(row = 0, column = 1, columnspan = 1)

    # Bottom Left
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(14))
    here_button.grid(row = 0, column = 1, columnspan = 1)

    # Top Left
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(10))
    here_button.grid(row = 0, column = 2, columnspan = 1)

    # Bottom Left
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(15))
    here_button.grid(row = 0, column = 2, columnspan = 1)

    # Top Left
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(9))
    here_button.grid(row = 0, column = 3, columnspan = 1)

    # Bottom Left
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(16))
    here_button.grid(row = 0, column = 3, columnspan = 1)

    # Top Left
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(8))
    here_button.grid(row = 0, column = 4, columnspan = 1)

    # Bottom Left
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(17))
    here_button.grid(row = 0, column = 4, columnspan = 1)

    # Top Left
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(7))
    here_button.grid(row = 0, column = 5, columnspan = 1)

    # Bottom Left
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(18))
    here_button.grid(row = 0, column = 5, columnspan = 1)




    #Placeholder buttons
    here_button = Tkinter.Button(self.top_button_frame, text = '', width = 1, command=lambda: placeholderButton(27))
    here_button.grid(row = 0, column = 6, columnspan = 1)

    here_button = Tkinter.Button(self.bottom_button_frame, text = '', width = 1, command=lambda: placeholderButton(26))
    here_button.grid(row = 0, column = 6, columnspan = 1)

    #for x in range(7, 14):

    #Top Right
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(6))
    here_button.grid(row = 0, column = 7, columnspan = 1)

    #Bottom Right
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(19))
    here_button.grid(row = 0, column = 7, columnspan = 1)

    #Top Right
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(5))
    here_button.grid(row = 0, column = 8, columnspan = 1)

    #Bottom Right
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(20))
    here_button.grid(row = 0, column = 8, columnspan = 1)

    #Top Right
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(4))
    here_button.grid(row = 0, column = 9, columnspan = 1)

    #Bottom Right
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(21))
    here_button.grid(row = 0, column = 9, columnspan = 1)

    #Top Right
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(3))
    here_button.grid(row = 0, column = 10, columnspan = 1)

    #Bottom Right
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(22))
    here_button.grid(row = 0, column = 10, columnspan = 1)

    #Top Right
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(2))
    here_button.grid(row = 0, column = 11, columnspan = 1)

    #Bottom Right
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(23))
    here_button.grid(row = 0, column = 11, columnspan = 1)

    #Top Right
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(1))
    here_button.grid(row = 0, column = 12, columnspan = 1)

    #Bottom Right
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(24))
    here_button.grid(row = 0, column = 12, columnspan = 1)

    #Top Right
    here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', width = 1, command=lambda: hereButton(0))
    here_button.grid(row = 0, column = 13, columnspan = 1)

    #Bottom Right
    here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', width = 1, command=lambda: hereButton(25))
    here_button.grid(row = 0, column = 13, columnspan = 1)



    # Control Frame
     
    self.turn = Tkinter.StringVar(value = text_turn)
    turn_label = Tkinter.Label(self.control_frame, width = '15', \
      bg = 'white', textvariable = self.turn)
    turn_label.pack(side = 'left')
    # Roll widget displays/keeps track of current roll
    self.roll = Tkinter.StringVar(value = 'Roll: ' + str(cur_roll))
    roll_label = Tkinter.Label(self.control_frame, width = '15', \
      bg = 'white', textvariable = self.roll)
    # pack the widget
    roll_label.pack(side = 'left')

    # Roll, double and undo buttons
    #if (playingGame):
    roll_button = Tkinter.Button(self.control_frame, text = 'Next Turn')
    roll_button.pack(side = 'left')
    roll_button.bind('<Button-1>', self.switchTurn)

    newGame_button = Tkinter.Button(self.control_frame, text = 'New Game', \
      command = newGameButton)
    newGame_button.pack(side = 'left')

    undo_button = Tkinter.Button(self.control_frame, text = 'Undo', \
      command = undoButton)
    undo_button.pack(side = 'right')

    


    #pack the frames

    self.control_frame.pack(side = 'top')
    self.top_button_frame.pack()
    self.board_frame.pack()
    self.bottom_button_frame.pack()
    self.redraw(self.state)

    # Play comp first turn if it goes first
    if (self.state.turn == 1):
      print self.state.roll
      self.state = bg.playCompTurn(self.state, 4, False self.factors_list)
      
      self.redraw(self.state)

      # Update and return move to other player
      r = self.die.rollDie()
      self.state.updateRoll(r)
      self.state.switchTurn()
    
      roll_message = 'Roll: ' + str(self.state.roll)
      self.roll.set(roll_message)
      turn_message = "White's Turn"
      self.turn.set(turn_message)

    # main loop
    Tkinter.mainloop()

  def switchTurn(self, event):
    r = self.die.rollDie()
    self.state.updateRoll(r)
    self.state.switchTurn()
    
    roll_message = 'Roll: ' + str(self.state.roll)
    self.roll.set(roll_message)
    
    if (self.state.turn == 0):
      turn_message = "White's Turn"
    else:
      turn_message = "Black's Turn"

    self.turn.set(turn_message)
    self.redraw(self.state)
    
 
    if (self.state.turn == 1): #Black
      print roll_message
      

      # Calculate and play turn
      #self.state = bg.playStrategicCompTurn(self.state)
      self.state = bg.playCompTurn(self.state, 4, False self.factors_list)
      self.redraw(self.state)
      
      # Update and return move to other player
      r = self.die.rollDie()
      self.state.updateRoll(r)
      self.state.switchTurn()
    
      roll_message = 'Roll: ' + str(self.state.roll)
      self.roll.set(roll_message)
      turn_message = "White's Turn"
      self.turn.set(turn_message)

      if (self.state.existValidMoves() == False):
        #self.turn.set("No valid moves")
        print "no valid moves"
        print "press next turn"

        #r = self.die.rollDie()
        #self.state.updateRoll(r)
        #self.state.switchTurn()
        
        #self.state = bg.playCompTurn(self.state, 4, False self.factors_list)
        #self.redraw(self.state)
    
        #r = self.die.rollDie()
        #self.state.updateRoll(r)
        #self.state.switchTurn()

        ##self.state = bg.playStrategicCompTurn(self.state)
        #if (self.state.existValidMoves() == False):
          #r = self.die.rollDie()
          #self.state.updateRoll(r)
          #self.state.switchTurn()
          
          #self.state = bg.playCompTurn(self.state, 4, False self.factors_list)
          #self.redraw(self.state)
      
          #r = self.die.rollDie()
          #self.state.updateRoll(r)
          #self.state.switchTurn()

          #roll_message = 'Roll: ' + str(self.state.roll)
          #self.roll.set(roll_message)
          #turn_message = "White's Turn"
          #self.turn.set(turn_message)


  

