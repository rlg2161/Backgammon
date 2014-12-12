import bgNeuralNetwork as NN 
import dice
import state
import copy
import math
import random
import stateTreeNode
import datetime
import learning
import plotResults
import backgammonTester
import sys
import operator

stateList = []

def main():
  
  #die = dice.oneDie(6)
  #state = createInitialState(die)
  #state.printState()

  #posStates = [state]
  #genAllPossMoves(posStates)

  

  #playWithNN(nn)

#def playWithNN(nn):

  #nnDict = NN.getAllNNinputs(net, posStates)

  #print nnDict

  #desiredState = max(nnDict.iteritems(), key=operator.itemgetter(1))[0]
  #print desiredState
  


  #Old main method
  next = True

  while (next == True):
    programLoop()
    next_in = raw_input("Continue? Y/y/Yes/yes: ")
    if (next_in == "Y" or next_in == "y" or next_in == "Yes" or next_in == "yes"):
      continue
    else:
      next = False

def programLoop():  

  net = NN.createNN(198)

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
  computer = raw_input("Please make your selection:   ")
  #print computer
  
  good_input = False

  while (good_input != True):
    try:
      int(computer)
      #computer = int(computer)
      good_input = True
      continue
      #else:
        #computer = raw_input("Please enter 0 to play against a person or 1 for computer or 2 for 2 computers against eachother:  ")
    except:
      computer = raw_input("Please enter the appropriate option: ")
  
  
  computer = int(computer)

  if (computer < 4):
    
    if (len(sys.argv) != 2 and len(sys.argv) != 3):
      str_arg1 = raw_input("What is the name of the first strat file? ")
      str_arg2 = raw_input("What is the name of the second strat file? ")

    if (len(sys.argv) >= 2):
      str_arg1 = str(sys.argv[1])
    if (len(sys.argv) == 3):
      str_arg2 = str(sys.argv[2])
    
    try:
      factors_list1 = []
      try_strat_file = open(str_arg1, 'r')

      num_games1 = try_strat_file.readline()
      num_games1 = num_games1.rstrip("\n")
      fia1 = try_strat_file.readline()
      fia1 =fia1.rstrip("\n")
      factor1 = try_strat_file.readline()
      factor1 = factor1.rstrip("\n")
      mps1 = try_strat_file.readline()
      mps1 = mps1.rstrip("\n")
      ppm1 = try_strat_file.readline()
      ppm1 = ppm1.rstrip("\n")


      line = try_strat_file.readline()
      splitLine = line.split()

      for item in splitLine:
        factors_list1.append(float(item))
      #print factors_list

      factors_list2 = []

      if (len(str_arg2) == 0):
        factors_list2 = factors_list1

      else:  
        try_strat_file = open(str_arg2, 'r')
        
        num_games2 = try_strat_file.readline()
        num_games2 = num_games2.rstrip("\n")
        fia2 = try_strat_file.readline()
        fia2 = fia2.rstrip("\n")
        factor2 = try_strat_file.readline()
        factor2 = factor2.rstrip("\n")
        mps2 = try_strat_file.readline()
        mps2 = mps2.rstrip("\n")
        ppm2 = try_strat_file.readline()
        ppm2 = ppm2.rstrip("\n")
        

        line = try_strat_file.readline()
        splitLine = line.split()

        for item in splitLine:
          factors_list2.append(float(item))
        #print factors_list
    
    except:
      print "Files could not be opened - please recheck file names and restart program"
      exit()
    if (computer < 3):
      #Single Game Play
      
      if (computer == 0):
        print_flag = 1
        first_strat = 0
        second_strat = 0

      elif (computer == 1):
        print "What strategies would you like the computer to use? They are, currently: "
        print "1: Random computer player"
        print "2: My own, custom algorithm"
        print "3: My own algo but customized to minimize opponent move values"
        print "4: Learned algo (make sure to run learning.py first)"
        print "... More to come ..."

        good_input = False
        print_flag = 1
        first_strat = 0
        second_strat = raw_input("\n" + "Please enter the desired computer strategy: ")
        while (good_input != True):
          try:
            second_strat = int(second_strat)
            good_input = True
          except:
            second_strat = raw_input("\n" + "Please enter the appropriate option: ")

      elif (computer == 2):
        print "What strategies would you like the computer to use? They are, currently: "
        print "1: Random computer player"
        print "2: My own, custom algorithm"
        print "3: My own algo but customized to minimize opponent move values"
        print "4: Learned algo (make sure to run learning.py first)"
        print "... More to come ..."

        good_input = False
        print_flag = True
        first_strat = raw_input("\n" + "Please enter the desired computer strategy: ")

        while (good_input != True):
          try:
            first_strat = int(first_strat)
            good_input = True
          except:
            first_strat = raw_input("\n" + "Please enter the appropriate option: ")

        second_strat = raw_input("\n" + "Please enter the desired computer strategy: ")
        while (good_input != True):
          try:
            second_strat = int(second_strat)
            good_input = True
          except:
            second_strat = raw_input("\n" + "Please enter the appropriate option: ")

      again = playMatch(net, 15, first_strat, second_strat, print_flag, factors_list1, factors_list2)

      while(again):
        again = playMatch(net, 15, first_strat, second_strat, print_flag, factors_list1, factors_list2)

    elif (computer == 3):
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

      #num_sims, fia, factor, mps
      a = "_" + str(num_games1) +"_" + str(fia1) + "_" + str(factor1) + "_" + str(mps1) + "_" + str(str_arg1)
      

      #raw_input("wait")
      #print "verify a, then re-run program"
      simulateSession(net, first_strat, second_strat, num_sims, factors_list1, factors_list2, a)
    

  elif (computer == 4):
    # Random strategy simulation to gather learning data
    num_games = raw_input("How many strats would you like to simulate? ")
    mps = raw_input("How many matches per strat? ")
    ppm = raw_input("How many points per match? ")
    name = raw_input("What would you like to name the output file? ")

    generateSimulations(int(num_games), 12, 10, int(mps), int(ppm), name)
    #print "change generateSimulations numer and restart program"

  elif (computer == 5): 
    #learning.py
    inFile = raw_input("What file would you like to draw learning examples from? ")
    sizeInput = raw_input("How many learning examples in the file? ")
    outFile = raw_input("What would you like to call file containing the resulting list of weights? ")
    print_flag_in = raw_input("Would you like to print intermediate steps and results -y/Y/yes/Yes?")
    print_flag = False
    
    if(print_flag_in == "y" or again_in == "Y" or again_in == "yes" or again_in == "Yes"):
      print_flag = True
    
    learning.learningFxn(inFile, int(sizeInput), outFile, print_flag)


  elif (computer == 6):
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


  else:
    # backgammonTester.py
    inFile = str_arg1
    backgammonTester.backgammonTester(inFile)

def playMatch(net, num_points, first_strat, second_strat, print_flag, factors_list1, factors_list2):
  
  white_points = 0
  black_points = 0

  while (white_points < 15 and black_points < 15):
    winner, points = playSingleGame(net, first_strat, second_strat, print_flag, factors_list1, factors_list2)

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

def playSingleGame(net, first_strat, second_strat, print_flag, factors_list1, factors_list2):
  ''' Play a single game'''
  
  #lastGameFile = open('lastgame.txt', 'w')

  winner = -1
  points = 1
  

  if (first_strat == 0 and second_strat == 0): #Play 2 humans
    winner, points = playTwoHumans(first_strat, second_strat, print_flag)
 
  elif (first_strat == 0 and second_strat != 0): #Human vs. comp
    winner, points = playHumanVsComp(net, first_strat, second_strat, print_flag, factors_list1)

  elif(first_strat != 0 and second_strat != 0):
    winner, points = playCompVsComp(net, first_strat, second_strat, print_flag, factors_list1, factors_list2)

    
  #stateList.reverse()
  #while(len(stateList) > 0):
    #lastGameFile.write(str(stateList.pop()))
  #lastGameFile.close()
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
  

def checkGammon(state, winner):

  last_white, last_black = state.lastOccupiedSpace()

  points_for_win = 1

  if (winner == 0): #white won
    if (state.board[25] == 0):
      if (last_black < 7):
        points_for_win = 3
      else:
        points_for_win = 2

  if (winner == 1): #black won
    if(state.board[0] == 0):
      if(last_white > 18):
        points_for_win = 3
      else:
        points_for_win = 2

  return points_for_win

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
  
  points = checkGammon(state, winner)
  return (winner, points)

def playHumanVsComp(net, first_strat, second_strat, print_flag, factors_list):

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
    playCompTurn(net, state, second_strat, print_flag, factors_list)

  while (winner == -1):
    roll = die.rollDie()
    state.updateRoll(roll)
    state.switchTurn()
    if (state.turn == 0):
      playTurn(state, first_strat, 1)
    else:
      playCompTurn(net, state, second_strat, print_flag, factors_list)

    winner = state.testGameOver()

  if (winner == -1):
    state.printState()

  points = checkGammon(state, winner)
  return (winner, points)

def playCompVsComp(net, first_strat, second_strat, print_flag, factors_list1, factors_list2):
  
  #set up initial parameters
  die = dice.oneDie(6)
  state = createInitialState(die)
  winner = -1

  if (state.turn == 0):
    playCompTurn(net, state, first_strat, print_flag, factors_list1)
  else:
    playCompTurn(net, state, second_strat, print_flag, factors_list2)

  #raw_input("wait")
  while (winner == -1):
    roll = die.rollDie()
    state.updateRoll(roll)
    state.switchTurn()
    if (state.turn == 0):
      playCompTurn(net, state, first_strat, print_flag, factors_list1)
    elif(state.turn == 1):
      playCompTurn(net, state, second_strat, print_flag, factors_list2)

    winner = state.testGameOver()
  
  #state.printState()
  points = checkGammon(state, winner)
  return (winner, points)


def playCompTurn(net, state, strat, print_flag, factors_list):
  '''Determine computer moves depending on desired strategy'''
  if(int(strat) == 5):
    
    if (print_flag):
      state.printState()

      raw_input("wait")

    # Use neural net to select a move
    
    #Gen states
    posStates = [state]
    genAllPossMoves(posStates)
 
    #use net to get state values
    nnDict = NN.getAllNNinputs(net, posStates)

    #find highest one
    desiredState = max(nnDict.iteritems(), key=operator.itemgetter(1))[0]
    


    #update board to new position
    state.updateFromState(desiredState)

  if(int(strat) == 4):
    #Use factors list to play a 'random' strat
    if (print_flag):
      state.printState()

      raw_input("wait")
    #print "playcompturn" + str(factors_list)
    new_state = playStratCompTurn(state, factors_list)
    state.updateFromState(new_state)
    
  elif (int(strat) == 3):
    #Move with state tree
    if (print_flag):
      state.printState()

    new_state = moveWithStateTree(state)
    state.updateFromState(new_state)
    
  elif(int(strat) == 2):
    #Play my human-like algo
    
    if (print_flag):
      state.printState()

    new_state = playStrategicCompTurn(state)
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
          space_to_valid = playHumanTurn(state)
        elif (num_flag == 1): #Random computer player 
          space_to_valid = playRandCompTurn(state)
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


def simulateSession(net, first_strat, second_strat, number_matches, factors_list1, factors_list2, a):
  '''Simulates a given number of games and keeps track of results'''
  #ppm = points per match

  #name_learning_file = raw_input("What is the name of the learning file: ")

  #a = a + name_learning_file
  
  fname = "simSessionFile" + a + ".txt" 

  sim_session_file = open(fname, 'a')
  
  ppm = input ("How many points in each match: ")

  matches_won_by_white = 0
  matches_won_by_black = 0
  match_score_string = ""
  
  for x in range(0, number_matches):
    white_score = 0
    black_score = 0

    while (white_score < ppm and black_score < ppm):
      winner, points = playCompVsComp(net, first_strat, second_strat, False, factors_list1, factors_list2)
          
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
  sim_session_file.write(match_score_string)
  sim_session_file.write(fp1 + "\n" + fp2 + "\n")


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


  
def playStratCompTurn(state, factors_list):

  posStates = [state]
  genAllPossMoves(posStates)
    
  best = evalStratMove(factors_list, posStates)
  if (best == None):
    print "crashed in playStratCompTurn by returning Null"
    exit()
 
  return best
  

def evalStratMove(factors_list, posStates):
  
  '''Evaluate all moves in a list and return move with the highest score'''
  cur_max = -1000000
  best_move_state = None

  #copy_posStates = copy.deepcopy(posStates)
 
  statesToConsider = elimInvalidMoves(posStates)

  for x in range(0, len(statesToConsider)):
    
    #print "evalStratMove" + str(factors_list)
    temp = calcStratMove(statesToConsider[x], factors_list, 0)
    #print temp

    if (temp > cur_max):
      # If temp move better than current best, remove current best and store temp
      cur_max = temp
      best_move_state = statesToConsider[x]
      

  more_moves = best_move_state.existValidMoves()
  
  # Reporting bug where a full move is not returned
  if (more_moves == True):
    print "Error - not a final move state"
    print "Possible states to move from"
    for item in posStates:
      print item.existValidMoves()
      item.printState()
    
    print "Culled list for move calculation"
    for item in statesToConsider:
      print item.existValidMoves()
      item.printState()

    best_move_state.printState()
    exit(1)

  
  return best_move_state

def calcStratMove(state, fl, print_flag):

  move_value = 0

  turn = state.turn
  ##fl == factors_list
  
  temp = state.lastOccupiedSpace()
  last_white_space = temp[0]
  last_black_space = temp[1]

  pip_count = state.getPipCount()

  if (state.turn == 0): #white
    if(state.allInFinalQuadrant() == True and last_black_space > last_white_space):
      strat = 2
    else:
      strat = 1
  elif(state.turn == 1): #black
    if(state.allInFinalQuadrant() == True and last_black_space < last_white_space):
      strat = 2
    else:
      strat = 1
   

  # Score Resets
  white_uncovered_score = 0        #1
  black_uncovered_score = 0
  white_blocade_score = 0
  black_blocade_score = 0          #4
  
  white_covered_score = 0          #5
  black_covered_score = 0
  white_highest_blocade_count = 0
  black_highest_blocade_count = 0  #8
  
  # Factors but not scores
  white_blocade_count = 0          #9
  black_blocade_count = 0
  
  white_blot_points = 0
  black_blot_points = 0            #12

  
  for x in range(0, 25): # Tun through board for scores
    #White blocade 
    if (state.board[x] <= 1):
      if (white_blocade_count > white_highest_blocade_count):
        white_highest_blocade_count = white_blocade_count
      white_blocade_count = 0
    
    #Black blocade
    if (state.board[x] >= -1): #Non-black space on black's turn
      if (black_blocade_count > black_highest_blocade_count):
        black_highest_blocade_count = black_blocade_count
      black_blocade_count = 0
      
    # Points for uncovered pieces
    #White uncovered
    if (state.board[x] == 1):
      if(white_blocade_count > white_highest_blocade_count):
        white_highest_blocade_count = white_blocade_count
      white_blocade_count = 0
      if (x > last_black_space): 
        if (strat == 1):
          white_blot_points = fl[0] * ((25-x)*fl[1])
        elif (strat == 2):
          white_blot_points = fl[12] * ((25-x)*fl[13])
      white_uncovered_score = white_uncovered_score + white_blot_points
	
    # Black Uncovered
    if (state.board[x] == -1):
      if(black_blocade_count > black_highest_blocade_count):
        black_highest_blocade_count = black_blocade_count
      black_blocade_count = 0
      if (x < last_white_space): 
        black_blot_points = fl[2*strat] * ((x)*fl[3*strat])
      black_uncovered_score = black_uncovered_score + black_blot_points
      #print str(x) + " " + str(black_uncovered_score)

    # Points for blocades
    #White blocades
    if ((state.board[x]) >= 2):
      white_covered_score += 1*fl[4*strat]
      white_blocade_count += 1
      if (white_blocade_count > 1):
        white_blocade_score += white_blocade_count*fl[5*strat]
        #print str(x) + " " + str(white_blocade_count)

    #Black blocades
    if ((state.board[x]) <= -2):
      black_covered_score += 1*fl[6*strat]
      black_blocade_count += 1
      if (black_blocade_count > 1):
        black_blocade_score += black_blocade_count*fl[7*strat]
        #print str(x) + " " + str(white_blocade_count)
  
  white_points_scored = state.board[0]*fl[strat*8]
  black_points_scored = state.board[25]*fl[strat*10]
  white_jail_score = state.board[26]*fl[strat*9]  
  black_jail_score = state.board[27]*fl[strat*11]


  if (state.turn == 1):  
    score_tuple = (-1*white_points_scored,
    black_points_scored,
    -1*white_jail_score,
    black_jail_score,
    white_uncovered_score,
    -1*black_uncovered_score,
    -1*white_blocade_score,
    black_blocade_score,          
    -1*white_covered_score,          
    black_covered_score,
    -1*white_highest_blocade_count,
    black_highest_blocade_count) 

  elif (state.turn == 0):
    score_tuple = (white_points_scored,
    -1*black_points_scored,
    white_jail_score,
    -1*black_jail_score,
    -1*white_uncovered_score,
    black_uncovered_score,
    white_blocade_score,
    -1*black_blocade_score,          
    white_covered_score,          
    -1*black_covered_score,
    white_highest_blocade_count,
    -1*black_highest_blocade_count)

  for x in range(0, len(score_tuple)):
    move_value = move_value + score_tuple[x]*fl[x]

  if (print_flag):
    print "move value: " + str(move_value),
    print "   score_tuple: " + str(score_tuple)
    state.printState()
	
	
  return move_value


def moveWithStateTree(state):
  '''Move for computer when using state tree based strategy for forecasting'''
  root = generateMoveTree(state)
  best_move = calcMoveFromStateTree(root)
  if (best_move != None):
    return best_move.nodeState 
  else:
    return state

def calcMoveFromStateTree(root):
  posMove = root.child
  best_move = posMove
  move_val = -100000
  
  while (posMove != None):
    if (posMove.score > move_val):
      best_move = posMove
      move_val = posMove.score
    posMove = posMove.firstSibling
  
  return best_move

def generateMoveTree(st):
  '''Generate all possible game states two moves out and put it in a tree'''
  listOfRolls = [ [1,1,1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2,2,2], [2,3],\
  [2,4], [2,5], [2,6], [3,3,3,3], [3,4], [3,5], [3,6], [4,4,4,4], [4,5], [4,6],\
  [5,5,5,5], [5,6], [6,6,6,6] ]

  stateTreeFile = open('stateTreeFile.txt', 'w')
  stateScore = calcMoveValue1(st, st.turn)
  root = stateTreeNode.stateTreeNode(st, stateScore)
    
  if (root == None):
    #print "continue"
    return root
  else:
    genMoveTree(root, root.nodeState.turn)
    #print "Len root after genMoveTree(): " + str(len(root))
    
    return root
  

def genMoveTree(root, turn):
  '''Given a root (i.e. state), calculate all possible states (w/ genAllPossMoves()) and then
  calculate the average score of opponent when genAllPossMoves() is calculated for each
  roll for each given state''' 
  listOfRolls = [ [1,1,1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,2,2,2], [2,3],\
  [2,4], [2,5], [2,6], [3,3,3,3], [3,4], [3,5], [3,6], [4,4,4,4], [4,5], [4,6],\
  [5,5,5,5], [5,6], [6,6,6,6] ]

  #print "genMoveTree()"
  rState = root.nodeState
  #print rState
  stateList = [rState]

  if (rState.existValidMoves() == False):
    #print "no valid moves"
    # elim extra generation when no moves exist 
    return

  else:
    genAllPossMoves(stateList)
    stateList = threeBestMoves(stateList)
    #print "len(stateList): " + str(len(stateList))

    #counter = 0
    if (len(stateList) == 1):
      if (stateList[0].turn == 0):
        nextNodeScore = calcMoveValue2(stateList[0], 1)
      else:
        nextNodeScore = calcMoveValue2(stateList[0], 0)
      nextNode = stateTreeNode.stateTreeNode(stateList[0], nextNodeScore)
      root.addChild(nextNode)
      return 


    if (len(stateList) >= 1):
      #print "comparing similar moves"
      for item in stateList:
        #counter = counter + 1
        #print "counter: " + str(counter)
        nextNodeScore = 0
        nextNode = stateTreeNode.stateTreeNode(item, nextNodeScore)
        
        cumeScore = 0
        for roll in listOfRolls:
          cpy_state = state.state(item)
          cpy_state.updateRoll(roll)
          cpy_state.switchTurn()
          oppStateList = [cpy_state]
          genAllPossMoves(oppStateList)
          elimInvalidMoves(oppStateList)
          for x in range(0, len(oppStateList)):
                  
            mv_val = calcMoveValue2(oppStateList[x], cpy_state.turn)
            if (roll == listOfRolls[0] or roll == listOfRolls[6] or roll == listOfRolls[11]\
              or roll == listOfRolls[15] or roll == listOfRolls[18] or roll == listOfRolls[20]):
              mv_val = mv_val/2 #acct for fact that these rolls are half as likely as other rolls
            #print mv_val
            #raw_input("wait")
            cumeScore = cumeScore + mv_val
        cumeScore = cumeScore/len(oppStateList)  
        #print cumeScore
        nextNode.updateScore(cumeScore)


        if (root.child == None):
          #print "adding child"
          root.addChild(nextNode)
        else:
          #print "adding sibling"
          sib = root.child.firstSibling
          if (sib == None):
            root.child.addSibling(nextNode)
          else:
            while (sib.firstSibling != None):
              sib = sib.firstSibling
            sib.addSibling(nextNode)

      return

def threeBestMoves(stateList):
  '''Identify and return list of up to 3 best possible moves for player given all poss states'''
  best = -10000
  bestState = None
  best2 = -10000
  best2State = None
  best3 = -10000
  best3State = None

  for st in stateList:
    move_val = calcMoveValue1(st, st.turn)
    if (move_val > best):
      temp1 = best
      temp1State = bestState
      temp2 = best2
      temp2State = best2State

      best = move_val
      bestState = st 
      best2 = temp1
      best2State = temp1State
      best3 = temp2
      best3State = temp2State
      #print "best"
      continue
       
    elif (move_val > best2):
      temp2 = best2
      temp2State = best2State

      best2 = move_val
      best2State = st
      best3 = temp2
      best3State = temp2State
      #print "second best"
      continue

    elif (move_val > best3):
      best3 = move_val
      best3State = st 
      #print "third best"
      continue

  bestList = [bestState]
  if (best2State != None):
    if (math.fabs(best2 - best) < 1):
      bestList.append(best2State)
  if (best3State != None):
    if (math.fabs(best3 - best) < 1):
      bestList.append(best2State)
  
  #for item in bestList:
    #print str(item)

  return bestList


def genAllPossMoves(posStates):
  '''Recursively generate all possible moves given a game-state'''
  if (len(posStates) > 10000):
    print "Runaway recursion :( - game exited"
    overflowMovesList = open('overflowMovesList.txt', 'w')
    for item in posStates:
      overflowMovesList.write(str(item))
    overflowMovesList.close()
    print len(posStates)
    exit(1)
  givenState = posStates[0]

  if (givenState.existValidMoves() == False):
    test = False
    for st in posStates:
      if (st.existValidMoves() == True):
        test = True
        break

    if (test == True):
      posStates.remove(givenState)
      genAllPossMoves(posStates)

    else:
      return posStates

    
  else: #There exists at least one valid move
    # CURRENT PLAYER HAS PIECE IN JAIL
    if ((givenState.turn == 0 and givenState.board[26] > 0 or \
      givenState.turn == 1 and givenState.board[27] < 0)):
      #print "piece in jail"
      
      for x in range(0, len(givenState.roll)):
        cpy_state = state.state(givenState)
        if (cpy_state.turn == 0): #White
          space_to_valid = cpy_state.checkSpaceTo(26, 25 - cpy_state.roll[x])
        else: # Black
          space_to_valid = cpy_state.checkSpaceTo(27, cpy_state.roll[x])
        #### IF VALID MOVE, THEN EXECUTE
        if (space_to_valid[0] == True):
          
          #UPDATE values
          space_from = space_to_valid[1]
          space_to = space_to_valid[2]
          move_dist = space_to_valid[3]

          # REMOVE piece being moved
          if (cpy_state.turn): #Black
            cpy_state.board[27] = cpy_state.board[27] + 1
          else: #White
            cpy_state.board[26] = cpy_state.board[26] - 1
      
      
          # CAPTURE opponent piece and put it in jail
          if ((cpy_state.board[space_to] < 0 and cpy_state.turn == False) or \
            (cpy_state.board[space_to] > 0 and cpy_state.turn == True)):
            if (int(math.fabs(cpy_state.board[space_to])) == 1):
              if (cpy_state.turn): #Black
                cpy_state.board[26] = cpy_state.board[26] + 1
              else: #White
                cpy_state.board[27] = cpy_state.board[27] - 1
              cpy_state.board[space_to] = 0

          # ADD piece to new space
          if (cpy_state.turn): #Black
            cpy_state.board[space_to] = cpy_state.board[space_to] - 1
          else: #White
            cpy_state.board[space_to] = cpy_state.board[space_to] + 1
          
          cpy_state.roll.remove(cpy_state.roll[x])
          cpy_state.updatePipCount()

          if (cpy_state.compareStateToList(posStates) == False):
            #print "not getting here?"
            posStates.append(cpy_state)
            
        
    # CURRENT PLAYER HAS NO PIECES IN JAIL
    else:
      for x in range(1, 25):
        
        # No one to move
        if (givenState.board[x] == 0):
          continue

        # Current space owned by other player
        elif ((givenState.board[x] < 0 and givenState.turn == 0) \
          or (givenState.board[x] > 0 and givenState.turn == 1)):
          #print "wrong color"
          continue
          
        # Current space a valid space_from
        else: 
          for y in range(0, len(givenState.roll)):
            cpy_state = state.state(givenState)
            if (cpy_state.turn == 0): #White
              space_to_valid = cpy_state.checkSpaceTo(x, x - cpy_state.roll[y])
            else: #Black
              space_to_valid = cpy_state.checkSpaceTo(x, x + cpy_state.roll[y])
            #print space_to_valid
            if (space_to_valid[0] == True):
              #print "Exist valid move?"
              space_from = space_to_valid[1]
              space_to = space_to_valid[2]
              move_dist = space_to_valid[3]

              # Execute move
              if (cpy_state.turn == 1): #Black
                cpy_state.board[space_from] = cpy_state.board[space_from] + 1
              elif (cpy_state.turn == 0): #White
                cpy_state.board[space_from] = cpy_state.board[space_from] - 1
          
          
              # Capture opponent piece and put it in jail
              if ((cpy_state.board[space_to] < 0 and cpy_state.turn == 0) or \
                (cpy_state.board[space_to] > 0 and cpy_state.turn == 1)):
                if (int(math.fabs(cpy_state.board[space_to])) == 1):
                  if (cpy_state.turn): #Black
                    cpy_state.board[26] = cpy_state.board[26] + 1
                  else: #White
                    cpy_state.board[27] = cpy_state.board[27] - 1
                  cpy_state.board[space_to] = 0

              if (cpy_state.turn): #Black
                cpy_state.board[space_to] = cpy_state.board[space_to] - 1
              else: #White
                cpy_state.board[space_to] = cpy_state.board[space_to] + 1
              
              cpy_state.roll.remove(cpy_state.roll[y])
              cpy_state.updatePipCount()

              if (cpy_state.compareStateToList(posStates) == False):
                posStates.append(cpy_state)
                #cpy_state.printState()
          #print x
          #print len(posStates)

    #print len(posStates)
    posStates.remove(givenState)
    #print len(posStates)
    genAllPossMoves(posStates)



def elimInvalidMoves(stateList):
  '''Eliminates moves from stateList that are not "complete" turns (i.e. not all
    dice are used) so that they can not be considered and illegally returned by
    move checking functions'''
  if (len(stateList) == 1):
    return stateList

  else: 
    new_list = []

    for state in stateList:
      if (len(state.roll) == 0 or state.testGameOver() >= 0):
        new_list.append(state)

    if (len(new_list) > 0):
      return new_list
      

    else:
      min_pip_sum = 1000

      for state in stateList:
        tempW, tempB = state.getPipCount()
        if ((tempW + tempB) < min_pip_sum):
          min_pip_sum = (tempW + tempB)

      for state in stateList:
        tempW, tempB = state.getPipCount()
        if ((tempW + tempB) <= min_pip_sum):
          new_list.append(state)

      if (len(new_list) ==0):
        print "Error in elimInvalidMoves"
        print len(stateList)
        for item in stateList:
          item.printState()
        exit(1)

      return new_list


def evalMoves(posStates):
  '''Evaluate all moves in a list and return move with the highest score'''
  cur_max = -1000000
  best_move = []

  elimInvalidMoves(posStates)

  for x in range(0, len(posStates)):

    temp = calcMoveValue1(posStates[x], posStates[x].turn)
    #print temp

    if (temp > cur_max):
      # If temp move better than current best, remove current best and store temp
      cur_max = temp
      best_move = []
      best_move.append(posStates[x])

    elif (temp == cur_max):
      # If temp is equal to current best, store both moves and decide which one later
      best_move.append(posStates[x])

  #print "Best Move Value: " + str(cur_max)
  
  if (len(best_move) == 1):
    best = best_move[0]
  else:
    test = random.random()*len(best_move)
    best = best_move[int(math.floor(test))]

  return best

def calcMoveValue1(state, turn):
  '''Calculate the value of a move for a strategy-based computer to determine best move'''
  uncovered_score = 0
  opp_jail_score = 0
  blocade_score = 0
  blocade_count = 0
  covered_score = 0

  temp = state.lastOccupiedSpace()
  last_white_space = temp[0]
  last_black_space = temp[1]
  

  # Only count once
  if (turn == 0): #White
      # Points for opp pieces in jail
      opp_jail_score = 8*((math.fabs(state.board[27])))
      # Points for scoring pieces
      points_scored = 4*(state.board[0])

  else: #Black
    opp_jail_score = 8*((state.board[26]))
    points_scored = 4*(state.board[25])


  for x in range(0, 25):
        
    if ((state.board[x] >= 0 and turn == 1) or \
      (state.board[x] <=0 and turn == 0)):
      blocade_count = 0
      continue

    else:
      # Points for uncovered pieces
      if (int(math.fabs(state.board[x])) == 1):
        blot_points = 0
        blocade_count = 0
        if (state.turn == 0): #White
          if (x > last_black_space): 
            blot_points = 5 * ((25-x)*.125)
        elif (state.turn == 1): #Black
          if (x < last_white_space):
            blot_points = 5*((x)*.125)
        
        uncovered_score = uncovered_score + blot_points

      # Points for blocades
      if (int(math.fabs(state.board[x])) >= 2):
        covered_score += 1
        blocade_count += 1
        if (blocade_count > 1):
          blocade_score += blocade_count*2

  #print "points scored: " + str(points_scored) + " opponent jail score: " + str(opp_jail_score) \
  #+ " blocade score: " + str(blocade_score) + \
  #" covered score: " + str(covered_score) + " Uncovered score: -" + str(uncovered_score)
  #print state.board
  move_value = points_scored + opp_jail_score + blocade_score + covered_score - uncovered_score
  return move_value

def calcMoveValue2(state, turn):
  '''Alternate method for calculating move value'''
  own_jail_score = 0
  blot_score = 0
  blocade_score = 0
  points_scored = 0
  blocade_count = 0
  last = state.lastOccupiedSpace()

  if (turn == 0):
    own_jail_score = 8*((math.fabs(state.board[26])))
    points_scored = 4*state.board[0]
  else:
    own_jail_score = 8*((math.fabs(state.board[27])))
    points_scored = 4*state.board[25]

  for x in range(0, 25):
    
    if ((state.board[x] >= 0 and turn == 1) or \
      (state.board[x] <=0 and turn == 0)):
      blocade_count = 0
      continue
    else:
      if (int(math.fabs(state.board[x])) == 1):
        blot_points = 0
        if (turn == 0): #White
          if (x > last[1]): # Not behind black's last piece
            blot_points = 5 * ((25-x)*.2)
        elif (turn == 1): #Black
          if (x < last[0]): # Not behing white's last piece
            blot_points = 5 * ((x)*.2)
        blot_score = blot_score + blot_points

      if (int(math.fabs(state.board[x])) >=2):
        blocade_count += 1
        if (blocade_count > 1):
          blocade_score += blocade_count*2


  move_value = own_jail_score + blot_score - points_scored - blocade_score 
  return move_value
  
def playStrategicCompTurn(state):
  '''Plays a computer turn if a non-random strategy is being played'''
  posStates = [state]
  genAllPossMoves(posStates)
  #posMovesList = open('posMovesList.txt', 'w')
  #for item in posStates:
    #posMovesList.write(str(item))
  #posMovesList.close()
  
  best = evalMoves(posStates)
  return best
  
def playRandCompTurn(state):
  '''Calculate and return a valid, random Computer move'''
  space_from = getCompSpaceFrom(state)
  space_to = getCompSpaceTo(state, space_from)
  space_to_valid = state.checkSpaceTo(space_from, space_to)

  return space_to_valid

def getCompSpaceFrom(state):
  '''Get space_from for computer player'''
  if (state.board[26 + state.turn] != 0):
    #print "Computer must move piece from Jail. "
    space_from = 26 + state.turn
    return space_from

  else:
    roll_copy = copy.deepcopy(state.roll)
    roll_copy.sort()
    test = roll_copy.pop()
    if (state.allInFinalQuadrant()):
      #All pieces in final quadrant
      if (state.furthestFromHome() <= test):
        # If largest roll is greater than or equal to distance from home of farthest piece
        if (state.turn == 0):
          space_from = state.furthestFromHome()
        else:
          space_from = 25 - state.furthestFromHome()
      else:
        #If largest roll is smaller than furthest away piece
        move_from = False
        while(move_from == False):
          test_space = int(math.floor(random.random()*24) + 1)
          if ((state.board[test_space] > 0 and state.turn == False) or (state.board[test_space] < 0 \
            and state.turn == True)):
            move_from = True
            space_from = test_space
    else:
      # No pieces in jail and not all in final quadrant
      move_from = False
      while(move_from == False):
        test_space = int(math.floor(random.random()*24) + 1)
        if ((state.board[test_space] > 0 and state.turn == False) or (state.board[test_space] < 0 \
            and state.turn == True)):
          move_from = True
          space_from = test_space
 
    return space_from

def getCompSpaceTo(state, space_from):
  '''Returns the comps selected space plus the largest remaining dice roll'''
  rollcpy = copy.deepcopy(state.roll)
  
  
  if (random.random() > .5):
    # Check the higher or lower value 50% of time - allows both high and low rolls to be
    # checked by comp
    rollcpy.reverse()
  
  test = rollcpy.pop()

  if (state.turn == 1):
    if (space_from == 26 + state.turn):
      # If comp is in jail
            
      space_to = test
    

    elif (state.allInFinalQuadrant() == False):
      # Comp not in jail && not all in final quadrant
      space_to = space_from + test
    
    else:
      # If all pieces in final quadrant 
      space_to = space_from + test
      if (space_to > 25):
        space_to = 25
      
  
  elif (state.turn == 0):
    if (space_from == 26 + state.turn):
      # If comp is in jail
      space_to = 25-test

    elif (state.allInFinalQuadrant() == False):
      # Comp not in jail && not all in final quadrant
      space_to = space_from - test

    else:
      # If all pieces in final quadrant 
      space_to = space_from - test
      if (space_to < 0):
        space_to = 0

  return space_to

def playHumanTurn(state):
   '''Receive move from human and check its validity'''
   space_from = getSpaceFrom(state)
   space_to = getSpaceTo()
   space_to_valid = state.checkSpaceTo(space_from, space_to)

   return space_to_valid

def getSpaceFrom(state):
  '''Get space from user'''
  if (state.board[26 + state.turn] != 0):
    print "You must move your piece from Jail"
    space_from = (26 + state.turn)

  else:
    move_from = False
    while (move_from == False):
      space_from = raw_input("Please input the space you would like to move from: ")
      try:
        space_from = int(space_from)
      except:
        print "That was not a valid input."

      if (space_from < 27 and space_from >= 0):
        if ((state.board[space_from] > 0 and state.turn == 0) or (state.board[space_from] < 0\
          and state.turn == 1)):
          move_from = True

  return space_from

def getSpaceTo():
  '''Get space to move to from user'''
  again = True
  while (again):
    space_to = raw_input("Please input the space you would like to move to: ")
    try:
      space_to = int(space_to)
      again = False
    except:
      print "That was not a valid input."
  
  return space_to


def createInitialState(die):
  '''Create initial game state given a die object'''
    
  gf = die.goesFirst()

  t = gf[0]
  r = gf[1]

  st = state.state(t, r)

  return st

if __name__ == "__main__":
  main()