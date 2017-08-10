import lib.dice as dice
import lib.state as state
import lib.stateTreeNode as stateTreeNode
import lib.learning as learning
import lib.plotResults as plotResults
import lib.move as move

from lib.strategies import linTransform as lin_transform_strategy
from lib.strategies import heuristic
from lib.strategies import randomMove
from lib.strategies import human as humanStrat

import backgammonTester

import copy
import math
import random
import datetime
import sys
import operator

stateList = []

def main():

  next = True

  while (next == True):
    programLoop()
    next_in = raw_input("Continue? Y/y/Yes/yes: ")
    if (next_in == "Y" or next_in == "y" or next_in == "Yes" or next_in == "yes"):
      continue
    else:
      next = False

def programLoop():

  print "Would you like to play against another person or the computer?"
  print ""
  print "0: two people to play each other"
  print "1: human vs. computer"
  print "2: comp vs. comp (strategy testing and simulation)"
  print "3: simulation"
  print "4: sim for learning "
  print "5: calculate learning values"
  print "6: plot results "
  print "7: GUI "
  option = raw_input("Please make your selection:   ")

  good_input = False

  while (good_input != True):
    try:
      int(option)
      good_input = True
      continue
    except:
      option = raw_input("Please enter the appropriate option: ")


  option = int(option)

  if (option == 0):
    # Human vs. Human
    print_flag = 1
    first_strat = 0
    second_strat = 0

    again = playMatch(15, first_strat, second_strat, print_flag, None, None)

    while(again):
      again = playMatch(15, first_strat, second_strat, print_flag, factors_list1, factors_list2)

  elif (option == 1):
    # Human v. Comp
    print "What strategies would you like the computer to use? They are, currently: "
    print "1: Random computer player"
    print "2: My own, custom algorithm"
    print "3: My own algo but customized to minimize opponent move values"
    print "4: Learned algo (make sure to run learning.py first)"
    print "... More to come ..."

    good_input = False
    print_flag = 1
    first_strat = 0
    factors_list1 = []
    second_strat = raw_input("\n" + "Please enter the desired computer strategy: ")
    while (good_input != True):
      second_strat = int(second_strat)
      if (second_strat == 4):
        stratFile = raw_input("What is the name of the computer strat file? Press enter to use default  ")
        factors_list1 = loadStratFile(stratFile)
        good_input = True
      else:
        good_input = True

    again = playMatch(15, first_strat, second_strat, print_flag, factors_list1, None)

    while(again):
      again = playMatch(15, first_strat, second_strat, print_flag, factors_list1, None)

  elif (option == 2):
    # Comp v. Comp
    print "What strategies would you like the computer to use? They are, currently: "
    print "1: Random computer player"
    print "2: My own, custom algorithm"
    print "3: My own algo but customized to minimize opponent move values"
    print "4: Learned algo (make sure to run learning.py first)"
    print "... More to come ..."

    good_input = False
    print_flag = True
    first_strat = raw_input("\n" + "Please enter the first desired computer strategy: ")
    factors_list1 = factors_list2 = []

    while (good_input != True):
      first_strat = int(first_strat)
      if (first_strat == 4):
        stratFile = raw_input("What is the name of the computer strat file? Press enter to use default  ")
        factors_list1 = loadStratFile(stratFile)
        good_input = True
      else:
        good_input = True


    good_input = False
    second_strat = raw_input("\n" + "Please enter the second desired computer strategy: ")
    while (good_input != True):
      second_strat = int(second_strat)
      if (second_strat == 4):
        stratFile = raw_input("What is the name of the computer strat file? Press enter to use default  ")
        factors_list2 = loadStratFile(stratFile)
        good_input = True
      else:
        good_input = True

    print first_strat
    print factors_list1

    print second_strat
    print factors_list2

    again = playMatch(15, first_strat, second_strat, print_flag, factors_list1, factors_list2)

    while(again):
      again = playMatch(15, first_strat, second_strat, print_flag, factors_list1, factors_list2)

  elif (option == 3):
    #On screen simulation
    num_sims = raw_input("How many matches would you like to simulate? ")
    try:
      num_sims = int(num_sims)
    except:
      num_sims = int(raw_input("Please enter a # of sims: "))
    print "What strategies would you like the computer to use? They are, currently: "
    print "1: Random computer player"
    print "2: My own, custom algorithm"
    print "3: My own algo but customized to minimize opponent move values"
    print "4: Learned algo (make sure to run learning.py first)"
    print "... More to come ..."
    first_strat = raw_input("Choice for comp 1: ")
    second_strat = raw_input("Choice for comp 2: ")

    factors_list1 = factors_list2 = []

    good_input = False

    while (good_input != True):
      first_strat = int(first_strat)
      if (first_strat == 4):
        stratFile = raw_input("What is the name of the computer strat file? Press enter to use default  ")
        factors_list1 = loadStratFile(stratFile)
        good_input = True
      else:
        good_input = True

    good_input = False

    while (good_input != True):
      second_strat = int(second_strat)
      if (second_strat == 4):
        stratFile = raw_input("What is the name of the computer strat file? Press enter to use default  ")
        factors_list2 = loadStratFile(stratFile)
        good_input = True
      else:
        good_input = True

    #num_sims, fia, factor, mps
    ppm = raw_input("How many points per match? ")

    a = "_" + str(num_sims) +"_" + str(ppm) + "_" + str(first_strat) + "_" + str(second_strat)


    #raw_input("wait")
    #print "verify a, then re-run program"
    simulateSession(first_strat, second_strat, num_sims, ppm, factors_list1, factors_list2, a)


  elif (option == 4):
    # Random strategy simulation to gather learning data
    num_games = raw_input("How many strats would you like to simulate? ")
    mps = raw_input("How many matches per strat? ")
    ppm = raw_input("How many points per match? ")
    name = raw_input("What would you like to name the output file? ")

    generateSimulations(int(num_games), 12, 10, int(mps), int(ppm), name)
    #print "change generateSimulations numer and restart program"

  elif (option == 5):
    #learning.py
    inFile = raw_input("What file would you like to draw learning examples from? ")
    sizeInput = raw_input("How many learning examples in the file? ")
    outFile = raw_input("What would you like to call file containing the resulting list of weights? ")
    print_flag_in = raw_input("Would you like to print intermediate steps and results -y/Y/yes/Yes?")
    print_flag = False

    if(print_flag_in == "y" or again_in == "Y" or again_in == "yes" or again_in == "Yes"):
      print_flag = True

    learning.learningFxn(inFile, int(sizeInput), outFile, print_flag)


  elif (option == 6):
    # plotResults.py
    inFile = raw_input("What file would you like to plot algorithm values from? ")
    factor = raw_input("What factor would you like to use? ")

    good_input = False

    while (good_input != True):
      try:
        f = int(factor)
        good_input = True
      except:
        factor = raw_input("What factor would you like to use? ")

    plotResults.plotResults(inFile, f)


  elif (option == 7):
    # backgammonTester.py
    inFile = 'tryStratFile2001.txt'
    backgammonTester.backgammonTester(inFile)

def loadStratFile(fileName):
  print fileName
  if (fileName == ""):
    fileName = "tryStratFile2001.txt"
  try:
    try_strat_file = open(fileName, 'r')
  except:
    print "Bad strategy file name entered. Using default "
    fileName = "tryStratFile2001.txt"
    try_strat_file = open(fileName, 'r')

  factors_list = []
  num_games1 = try_strat_file.readline()
  num_games1 = num_games1.rstrip("\n")
  print num_games1
  fia1 = try_strat_file.readline()
  fia1 =fia1.rstrip("\n")
  print fia1
  mps1 = try_strat_file.readline()
  mps1 = mps1.rstrip("\n")
  print mps1
  ppm1 = try_strat_file.readline()
  ppm1 = ppm1.rstrip("\n")
  print ppm1


  line = try_strat_file.readline().rstrip(' ')
  splitLine = line.split(' ')
  print "Line: " + line
  print splitLine

  for item in splitLine:
    factors_list.append(float(item))
  print "factorsList: ",
  print factors_list
  return factors_list



def playMatch(num_points, first_strat, second_strat, print_flag, factors_list1, factors_list2):

  white_points = 0
  black_points = 0

  while (white_points < 15 and black_points < 15):
    winner, points = playSingleGame(first_strat, second_strat, print_flag, factors_list1, factors_list2)

    if (winner == 0):
      white_points = white_points + points
    else:
      black_points = black_points + points

    if (print_flag):
      print "White Points: " + str(white_points)
      print "Black Points: " + str(black_points)

  again_in = raw_input("Would you like to play again?\nEnter y/Y/yes/Yes for another game:  ")
  if(again_in == "y" or again_in == "Y" or again_in == "yes" or again_in == "Yes"):
    again = True
  else:
    again = False

  return again

def playSingleGame(first_strat, second_strat, print_flag, factors_list1, factors_list2):
  ''' Play a single game'''

  winner = -1
  points = 1


  if (first_strat == 0 and second_strat == 0): #Play 2 humans
    winner, points = playTwoHumans(first_strat, second_strat, print_flag)

  elif (first_strat == 0 and second_strat != 0): #Human vs. comp
    winner, points = playHumanVsComp(first_strat, second_strat, print_flag, factors_list1)

  elif(first_strat != 0 and second_strat != 0):
    winner, points = playCompVsComp(first_strat, second_strat, print_flag, factors_list1, factors_list2)

  if (print_flag):
    if (winner == 0):
      if (points == 1):
        print "Player One ('o') was the winner."
      elif (points == 2):
        print "Player One ('o') was the winner with a gammon (2 points)."
      else:
        print "Player One ('o') was the winner with a backgammon (3 points)."
    else:
      if (points == 1):
        print "Player Two ('x') was the winner."
      elif (points == 2):
        print "Player Two ('x') was the winner with a gammon (2 points)."
      else:
        print "Player Two ('x') was the winner with a backgammon (3 points)."

  return(winner, points)

def playTwoHumans(first_strat, second_strat, print_flag):
  '''Function to manage gameplay between 2 humans'''

  #set up initial parameters
  die = dice.oneDie(6)
  state = createInitialState(die)
  winner = -1

  playTurn(state, first_strat, print_flag)

  while (winner == -1):
    roll = die.rollDie()
    state.updateRoll(roll)
    state.switchTurn()

    playTurn(state, second_strat, print_flag)

    winner = state.testGameOver()

  points = state.checkGammon(winner)
  return (winner, points)

def playHumanVsComp(first_strat, second_strat, print_flag, factors_list):

  #set up initial parameters
  die = dice.oneDie(6)
  state = createInitialState(die)
  winner = -1

  if (state.turn == 0):
    # White/Human player goes first
    playTurn(state, first_strat, print_flag)

  else:
    #Comp first
    print "Comp first"
    playCompTurn(state, second_strat, print_flag, factors_list)

  while (winner == -1):
    roll = die.rollDie()
    state.updateRoll(roll)
    state.switchTurn()
    if (state.turn == 0):
      playTurn(state, first_strat, 1)
    else:
      playCompTurn(state, second_strat, print_flag, factors_list)

    winner = state.testGameOver()

  if (winner == -1):
    state.printState()

  points = state.checkGammon(winner)
  return (winner, points)

def playCompVsComp(first_strat, second_strat, print_flag, factors_list1, factors_list2):

  #set up initial parameters
  die = dice.oneDie(6)
  state = createInitialState(die)
  winner = -1

  if (state.turn == 0):
    playCompTurn(state, first_strat, print_flag, factors_list1)
  else:
    playCompTurn(state, second_strat, print_flag, factors_list2)

  #raw_input("wait")
  while (winner == -1):
    # state.printState()
    roll = die.rollDie()
    state.updateRoll(roll)
    state.switchTurn()
    if (state.turn == 0):
      playCompTurn(state, first_strat, print_flag, factors_list1)
    elif(state.turn == 1):
      playCompTurn(state, second_strat, print_flag, factors_list2)

    winner = state.testGameOver()

  points = state.checkGammon(winner)
  return (winner, points)


def playCompTurn(state, strat, print_flag, factors_list):
  '''Determine computer moves depending on desired strategy'''

  if(int(strat) == 4):
    #Use factors list to play a 'random' strat
    if (print_flag):
      state.printState()

    #   raw_input("wait")
    #print "playcompturn" + str(factors_list)
    new_state = lin_transform_strategy.playStratCompTurn(state, factors_list)
    state.updateFromState(new_state)

  elif (int(strat) == 3):
    #Move with state tree
    if (print_flag):
      state.printState()

    new_state = heuristic.moveWithStateTree(state)
    state.updateFromState(new_state)

  elif(int(strat) == 2):
    #Play my human-like algo

    if (print_flag):
      state.printState()

    new_state = heuristic.playStrategicCompTurn(state)
    state.updateFromState(new_state)

  elif (int(strat) == 1):
    if (print_flag):
      state.printState()
    playTurn(state, int(strat), False)



def playTurn(state, num_flag, print_mode):
  '''Plays one turn'''
  stateList.append(copy.deepcopy(state))
  if (num_flag == 0 or num_flag == 1):
    val_moves = state.existValidMoves()

    if (val_moves == False):
      #stateList.append(copy.deepcopy(state))
      if (print_mode):
        print "No valid moves"
        state.printState()


    while (val_moves == True):
      #stateList.append(copy.deepcopy(state))
      if (print_mode):
        state.printState()

      valid_move = False


      while (valid_move == False):
        # Generate player moves and check if they are valid
        if (num_flag == 0): #Human Player
          space_to_valid = humanStrat.playHumanTurn(state)
        elif (num_flag == 1): #Random computer player
          space_to_valid = randomMove.playRandCompTurn(state)
        valid_move = space_to_valid[0]

        if (valid_move != True and state.turn == 0):
          # If invalid, print relevant error
          if (print_mode):
            state.printError(space_to_valid[3])


      #assign valid move values to actual move varialbes
      space_from = space_to_valid[1]
      space_to = space_to_valid[2]
      move_dist = space_to_valid[3]

      # Execute move
      if (state.turn): #Black
        state.board[space_from] = state.board[space_from] + 1
      else: #White
        state.board[space_from] = state.board[space_from] - 1


      # Capture opponent piece and put it in jail
      if ((state.board[space_to] < 0 and state.turn == False) or \
        (state.board[space_to] > 0 and state.turn == True)):
        if (int(math.fabs(state.board[space_to])) == 1):
          if (state.turn): #Black
            state.board[26] = state.board[26] + 1
          else: #White
            state.board[27] = state.board[27] - 1
          state.board[space_to] = 0

      if (state.turn): #Black
        state.board[space_to] = state.board[space_to] - 1
      else: #White
        state.board[space_to] = state.board[space_to] + 1

      #print state.roll
      state.roll.remove(move_dist)
      #print state.roll
      state.updatePipCount()

      val_moves = state.existValidMoves()


      #print val_moves

    if (print_mode):
      state.printState()


def simulateSession(first_strat, second_strat, number_matches, points_per_match, factors_list1, factors_list2, a):
  '''Simulates a given number of games and keeps track of results'''
  #ppm = points per match

  #name_learning_file = raw_input("What is the name of the learning file: ")

  #a = a + name_learning_file
  ppm = int(points_per_match)
  fname = "simSessionFile" + a + ".txt"

  sim_session_file = open(fname, 'a')

  matches_won_by_white = 0
  matches_won_by_black = 0
  match_score_string = ""

  for x in range(0, number_matches):
    white_score = 0
    black_score = 0

    while (white_score < ppm and black_score < ppm):
      winner, points = playCompVsComp(first_strat, second_strat, False, factors_list1, factors_list2)

      if (winner == 0):
        white_score = white_score + points
      elif(winner == 1):
        black_score = black_score + points

    print "Match " + str(x + 1) + " completed - ",
    #print winner
    if (white_score > black_score):
      print "White won"
      matches_won_by_white += 1
    else:
      print "Black won"
      matches_won_by_black += 1

    val = str(white_score - black_score) + "\n"
    print val,
    match_score_string = match_score_string + val



  if (matches_won_by_white > matches_won_by_black):
    print "White wins"
  else:
    print "Black wins"

  fp1 = "White's score for this round was: " + str(matches_won_by_white) + \
  " while playing " + str(first_strat)
  fp2 = "Black's score for this round was: " + str(matches_won_by_black) + \
  " while playing " + str(second_strat)

  print fp1
  print fp2

  #sim_session_file.write("learning w/ " + num_games + "\n")
  # sim_session_file.write(match_score_string)
  # sim_session_file.write(fp1 + "\n" + fp2 + "\n")
  sim_session_file.close()


def generateSimulations(num_sims, fia, factor, mps, ppm, name):
  ''' Generate and run random simulations to generate data for learning'''
  #fia == factors_in_algo
  #mps == matches_per_strat
  #ppm = points per match

  if (name == ""):
    a = "_" + str(num_sims) +"s_" + str(mps) + "m_" + str(ppm) + "p"
    fname = "stratListviaGen" + a + ".txt"

  else:
    fname = name + ".txt"

  good_strats_file = open(fname, "w")

  good_strats_file.write(str(num_sims) + "\n")
  good_strats_file.write(str(fia) + "\n")
  good_strats_file.write(str(factor) + "\n")
  good_strats_file.write(str(mps) + "\n")
  good_strats_file.write(str(ppm) + "\n")

  #factors_file = open("factors_file.txt", "w")
  die = dice.oneDie()

  for x in range(0, num_sims):
    matches_won_by_white = 0
    matches_won_by_black = 0
    rand_matches_won_by_white = 0
    rand_matches_won_by_black = 0
    agg_match_score = 0
    agg_rand_match_score = 0

    print "Strategy " +str(x+1) + " of " + str(num_sims)
    #For each simulation num_sim random strategies will be created
    factors_list = []
    for i in range(0, 2):
      fl = genFactorsList(fia, factor)
      for item in fl:
        factors_list.append(item)

    for x in range(0, mps):

      black_rand_points = 0
      white_rand_points = 0

      while (black_rand_points < ppm and white_rand_points < ppm):

        winnerRand, points = playCompVsComp(4, 1, False, factors_list, None)


        if (winnerRand == 1):
          black_rand_points = black_rand_points + points
        else:
          white_rand_points = white_rand_points + points

      if (white_rand_points >= ppm):
        rand_matches_won_by_white += 1
      else:
        rand_matches_won_by_black += 1

      print (white_rand_points, black_rand_points)

      agg_rand_match_score = agg_rand_match_score + (white_rand_points - black_rand_points)

    print "vs. random: " + str(rand_matches_won_by_white) + " " + str(agg_rand_match_score)


    for x in range(0, mps):
      white_points = 0
      black_points = 0

      while (white_points < ppm and black_points < ppm):
        winner, points = playCompVsComp(4, 2, False, factors_list, None)

        if (winner == 1):
          black_points = black_points + points
        else:
          white_points = white_points + points

      if (white_points >= ppm):
        matches_won_by_white += 1
      else:
        matches_won_by_black += 1

      print (white_points, black_points)

      agg_match_score = agg_match_score + (white_points - black_points)

    print "vs. strat: " + str(matches_won_by_white) + " " + str(agg_match_score)

    good_strats_string = ""
    good_strats_string = good_strats_string + "Points vs. Random: " + str(rand_matches_won_by_white) + " " + str(agg_rand_match_score) + "\n"
    good_strats_string = good_strats_string + "Points vs. Strat: " + str(matches_won_by_white) + " "+ str(agg_match_score) + "\n"

    #good_strats_file.write("Points vs. Random: " + str(white_rand_points) + " " + str(black_rand_points) + "\n")
    #good_strats_file.write("Points vs. Strat: " + str(white_points) + " "+ str(black_points) + "\n")

    #print "Points vs. Random: " + str(rand_matches_won_by_white) + " " + str(agg_rand_match_score)
    #print "Points vs. Strat: " + str(matches_won_by_white) + " "+ str(agg_match_score)

    for item in factors_list:
      #print str(item) + ", "
      good_strats_string = good_strats_string + str(item) + " "

    good_strats_string = good_strats_string + "\n\n\n"

    print good_strats_string

    good_strats_file.write(good_strats_string)
    good_strats_file.flush()

  good_strats_file.close()

def genFactorsList(fia, factor):
  factors_list = []
  for x in range(0, 12):
    strat_val = factor*random.random()
    factors_list.append(strat_val)

  factors_list[1] = factors_list[1]
  factors_list[3] = factors_list[3]

  return factors_list


def createInitialState(die):
  '''Create initial game state given a die object'''

  gf = die.goesFirst()

  t = gf[0]
  r = gf[1]

  st = state.state(t, r)

  return st

if __name__ == "__main__":
  main()
