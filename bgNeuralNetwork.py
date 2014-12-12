import numpy as np
import pybrain
import pickle
import math
import backgammon as bg 
import dice


def main():
  nn = createNN(198)
  print nn
  #saveNN(nn, 'firstNN.p')

  wMove = None
  bMove = None

  die = dice.oneDie(6)
  state = bg.createInitialState(die)
  winner = -1

  if (state.turn == 0):
    wMove = bg.playCompTurn(nn, state, 5, True, [])
  else:
    bMove = bg.playCompTurn(nn, state, 5, True, [])

  state.printState()

  if (wMove != None):
    print wMove
  else:
    print bMove




def createNN(sizeInputLayer):
  '''Create a Neural Network to train'''
  # Largely based on pybrain documentation
  
  # Create Net
  nn = pybrain.structure.FeedForwardNetwork()
  
  # Create layers
  inLayer = pybrain.structure.LinearLayer(sizeInputLayer, name ='in')
  hiddenLayer = pybrain.structure.SigmoidLayer(40, name ='hidden')
  #hiddenLayer2 = pybrain.structure.SigmoidLayer(3, name = 'win/gammon/backgammon')
  outLayer = pybrain.structure.LinearLayer(1, name ='out')

  #Add modules
  nn.addInputModule(inLayer)
  nn.addModule(hiddenLayer)
  #nn.addModule(hiddenLayer2)
  nn.addOutputModule(outLayer)

  # Create connections
  in_to_hidden = pybrain.structure.FullConnection(inLayer, hiddenLayer, name = "i-->h1")
  #hidden1_to_hidden2 = pybrain.structure.FullConnection(hiddenLayer1, hiddenLayer2, name = "h1-->h2")
  hidden_to_out = pybrain.structure.FullConnection(hiddenLayer, outLayer, name = "h1-->o")

  # add connections
  nn.addConnection(in_to_hidden)
  #nn.addConnection(hidden1_to_hidden2)
  nn.addConnection(hidden_to_out)

  # initialize net
  nn.sortModules()

  return nn

def loadNN(paramsFile):
  in_file = open(paramsFile, 'r')
  net = pickle.load(in_file)
  in_file.close()
  return net

def saveNN(nn, paramsFile):
  out_file = open(paramsFile, 'w')
  pickle.dump(nn, out_file)
  out_file.close()

def getNNoutput(nn, nnStateRep):
  return nn.activate(nnStateRep)


def getAllNNinputs(nn, stateList):
  
  NNdict = { }

  for st in stateList:
    NNValues = getNNValues(st)
    NNdict[st] = getNNoutput(nn, NNValues)

  return NNdict


def getNNValues(state):
  #use Tesauro's values to generate a 198 unit neural network
  NNinputArr = np.zeros(198)
  #[0:1] == binary turn values
  #[2:3] == scores/15
  #[4:5] == pieces in jail/2
  #[6:197] == encoding for each space
    # [6:9] == white encoding on space 1
    # [10:13] == black encoding on space 1
    # [14:17] == white encoding on space 2
    # ...


  # input turn values
  if (state.turn == 0):
    NNinputArr[0] = 1
  else:
    NNinputArr[1] = 1

  # get points scored
  NNinputArr[2] = state.board[0]/15
  NNinputArr[3] = state.board[25]/15

  # get jail scores
  NNinputArr[4] = state.board[26]/2
  NNinputArr[5] = state.board[27]/2

  # get individual space scores
  for x in range(1,25): #24 spaces on board
    counter = (x-1)*8
    pos = 6 + counter
    if (state.board[x] == 0):
      continue

    if (state.board[x] > 0): #white position
      NNinputArr[pos] = 1

      if (state.board[x] == 2):
        NNinputArr[pos+1] = 1
      if (state.board[x] == 3):
        NNinputArr[pos + 1] = 1
        NNinputArr[pos + 2] = .5
      if (state.board[x] == 4):
        NNinputArr[pos + 1] = 1
        NNinputArr[pos + 2] = 1
      if (state.board[x] > 4):
        NNinputArr[pos + 1] = 1
        NNinputArr[pos + 2] = 1
        NNinputArr[pos + 3] = (state.board[x] -4)/2


    if (state.board[x] < 0): #black position
      NNinputArr[pos + 4] = 1
    
      if (state.board[x] == -2):
        NNinputArr[pos+5] = 1
      if (state.board[x] == -3):
        NNinputArr[pos + 5] = 1
        NNinputArr[pos + 6] = .5
      if (state.board[x] == -4):
        NNinputArr[pos + 5] = 1
        NNinputArr[pos + 6] = 1
      if (state.board[x] < -4):
        NNinputArr[pos + 5] = 1
        NNinputArr[pos + 6] = 1
        NNinputArr[pos + 7] = (math.fabs(state.board[x]) -4)/2

    #print x
    #print NNinputArr[pos:(pos+8)]
    
  return NNinputArr

if __name__ == "__main__":
  main()