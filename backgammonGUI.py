# Basic GUI for my backgammon program

import Tkinter
import backgammon2 as bg 
import random
import math
import dice

# CONFUSED ABOUT OBJECT HIERARCHY

canvasWidth = 520
canvasHeight = 260

class backgammonGUI:
  
  # Functions and Methods
  def redraw(self, board):
    self.drawBoard()
    self.drawPieces(board)
      
    self.board.pack()
    Tkinter.mainloop()

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

  def drawPieces(self, board):
    
    #first quadrant
    for x in range(6, 0 , -1):
      if (board.board[x].color == 0):
        color = '#FFFFFF'
      else:
        color = '#A37547'
      if (len(board.board[x].s) < 6):
        for y in range(0, len(board.board[x].s)):
          coords = ((38*(6-x))+255) + 9 , 0 + 20*y, (293 + (38*(6-x)))-9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0, 6):
          coords = ((38*(6-x))+255) + 9 , 0 + 20*y, (293 + (38*(6-x)))-9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(255 + (38*(6-x)) + 20, 110, text = str(len(board.board[x].s)))

     
    #second quadrant
    for x in range(12, 6, -1):
      if (board.board[x].color == 0):
        color = '#FFFFFF'
      else:
        color = '#A37547'
      if (len(board.board[x].s)<6):
        for y in range(0, len(board.board[x].s)):
          coords = (38*(12-x))+ 9, 0 + 20*y, (38 + (38*(12-x))) - 9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0,6):
          coords = (38*(12-x))+ 9, 0 + 20*y, (38 + (38*(12-x))) - 9, 20 + 20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(38*(12-x) +20, 110, text = str(len(board.board[x].s)))

    # third quadrant
    for x in range(18, 12, -1):
      if (board.board[x].color == 0):
        color = '#FFFFFF'
      else:
        color = '#A37547'
      if (len(board.board[x].s) < 6):
        for y in range(0, len(board.board[x].s)):
          coords = (38*(x-13)) + 9, 260 - 20*y, 38 + (38*(x-13)) - 9, 240 - 20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0,6):
          coords = (38*(x-13))+9, 260 - 20*y, 38 + (38*(x-13)) - 9, 240 - 20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(38*(x-13) + 20, 150, text = str(len(board.board[x].s)))
     
    #fourth quadrant
    for x in range(24, 18, -1):
      if (board.board[x].color == 0):
        color = '#FFFFFF'
      else:
        color = '#A37547'
      if (len(board.board[x].s) < 6):
        for y in range(0, len(board.board[x].s)):
          coords = (38*(x-13) + 27) + 9, 260 - 20*y, 65 + (38*(x-13)) -9, 240 -  20*y
          self.board.create_oval(coords, fill = color)
      else:
        for y in range(0,6):
          coords = (38*(x-13) + 27) + 9, 260 - 20*y, 65 + (38*(x-13)) -9, 240 -  20*y
          self.board.create_oval(coords, fill = color)
        self.board.create_text(38*(x-13) +27 + 20, 150, text = str(len(board.board[x].s)))
    
    # home spaces
    for x in range(0, len(board.board[0].s)):
      coords = 485, 20 + (8*x), 518, 10 + (8*x)
      self.board.create_rectangle(coords, fill = '#FFFFFF')

    for x in range(0, len(board.board[25].s)):
      coords = 485, 258 - (8*x), 518, 250 - (8*x)
      self.board.create_rectangle(coords, fill = '#A37547')


    #jail
    for x in range(0, len(board.board[26].s)):
      coords = 231 , 127 - 20*x, 251  , 107 - 20*x
      self.board.create_oval(coords, fill = '#FFFFFF')

    for x in range(0, len(board.board[27].s)):
      coords = 231, 133 + 20*x, 251, 153 + 20*x
      self.board.create_oval(coords, fill = '#A37547')

  def __init__(self, board, roll, turn):

    # Necessary Variables
    
    die = dice.oneDie(6)
    #gf = bg.goesFirst(die)
    if (turn == 0):
      text_turn = "White's turn  "
    else:
      text_turn = "Black's turn  "

    #turn = gf[0]
    cur_roll = roll
   
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
    def rollButton():
      cur_roll = bg.rollDie(die)
      message = 'Roll: ' + str(cur_roll)
      roll.set(message)
      return

    def doubleButton():
      print "Not implemented yet"

    def undoButton():
      print "Not implemented yet"

    def hereButton():
      print self
      return self

    def placeholderButton():
      return
    

    # Board Frame
    self.board = Tkinter.Canvas(self.board_frame, width = canvasWidth, height = canvasHeight)

    # Movement buttons
    for x in range(0, 6):

      here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', command = hereButton)
      here_button.grid(row = 0, column = x, columnspan = 1)

      here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', command = hereButton)
      here_button.grid(row = 0, column = x, columnspan = 1)

    here_button = Tkinter.Button(self.top_button_frame, text = '', command = placeholderButton)
    here_button.grid(row = 0, column = 6, columnspan = 1)

    here_button = Tkinter.Button(self.bottom_button_frame, text = '', command = placeholderButton)
    here_button.grid(row = 0, column = 6, columnspan = 1)

    for x in range(7, 14):

      here_button = Tkinter.Button(self.top_button_frame, text = u'\u2193', command = hereButton)
      here_button.grid(row = 0, column = x, columnspan = 1)

      here_button = Tkinter.Button(self.bottom_button_frame, text = u'\u2191', command = hereButton)
      here_button.grid(row = 0, column = x, columnspan = 1)

    # Control Frame
     
    turn = Tkinter.StringVar(value = text_turn)
    turn_label = Tkinter.Label(self.control_frame, width = '15', \
      bg = 'white', textvariable = turn)
    turn_label.pack(side = 'left')
    # Roll widget displays/keeps track of current roll
    roll = Tkinter.StringVar(value = 'Roll: ' + str(cur_roll))
    roll_label = Tkinter.Label(self.control_frame, width = '15', \
      bg = 'white', textvariable = roll)
    # pack the widget
    roll_label.pack(side = 'left')

    # Roll, double and undo buttons
    roll_button = Tkinter.Button(self.control_frame, text = 'Next Turn', \
      command = rollButton)
    roll_button.pack(side = 'left')

    double_button = Tkinter.Button(self.control_frame, text = 'Double', \
      command = doubleButton)
    double_button.pack(side = 'left')

    undo_button = Tkinter.Button(self.control_frame, text = 'Undo', \
      command = undoButton)
    undo_button.pack(side = 'right')

    


    #pack the frames

    #self.roll_frame.pack(side = 'left')
    #self.button_frame.pack(side = 'right')
    self.control_frame.pack(side = 'top')
    self.top_button_frame.pack()
    self.board_frame.pack()
    self.bottom_button_frame.pack()



