import numpy as np


def main():
  data = getData('someSuccess1.txt')
  gameMatrix = data[0]
  solutionVector = data[1]
  
  try_strat_file = open("tryStratFile.txt", 'w')

  print gameMatrix.shape
  print gameMatrix
  print solutionVector.shape
  print solutionVector

  # Generate Optimal Move Weighting Array 

  gameMatrixTranspose = gameMatrix.transpose()
  #print gameMatrixTranspose
  print "gameMatrixTranspose shape: ",
  print gameMatrixTranspose.shape

  #nextMatrix = np.dot(gameMatrixTranspose, gameMatrix)
  #print nextMatrix
  #print "nextMatrix shape: ",
  #print nextMatrix.shape

  inv = np.linalg.inv(np.dot(gameMatrixTranspose, gameMatrix))
  print inv
  print "inv shape: ",
  print inv.shape

  step1 = np.dot(gameMatrixTranspose, solutionVector)
  print "step1 shape: ",
  print step1.shape
  print step1
  step1.shape = (106, 1)
  print "step1 shape after reshape: ",
  print step1.shape
  print step1

  step2 = np.dot(inv, step1)

  print "Final Weights: "
  print step2
  shape = step2.shape
  print shape

  for x in range(0, shape[0]):
    try_strat_file.write(str(step2[x,0]) + " ")
  
  try_strat_file.close()


def getData(filename):
  gameMatrix = None
  vectorList = []
  solutionList = []
  in_file = open(filename, 'r')
  test = ''
  
  for x in range(0, 1500):
    rand_score = in_file.readline()
    rand_score_split = rand_score.split()

    strat_score = in_file.readline()
    strat_score_split = strat_score.split()
    test = strat_score_split[3]
    test_val = int(test)
    #raw_input("wait")

    strat = in_file.readline()
    strat_split = strat.split()

    in_file.readline()
    in_file.readline()

    if (test_val < 25 ):
      # so as to only keep track of and use "good" strategies to learn
      
      continue

    solutionList.append(int(strat_score_split[3]))
    #print strat_score_split
    #print int(strat_score_split[3])
    #raw_input("wait")

    #strat = in_file.readline()
    #strat_split = strat.split()
    for x in range(0, len(strat_split)):
      strat_split[x] = float(strat_split[x])

    #in_file.readline()
    #in_file.readline()
    
    strat_split.insert(0, 1.0)

    vectorList.append(strat_split)
  
  solutionVector = np.array(solutionList)
  gameMatrix = np.matrix(vectorList)

  return (gameMatrix, solutionVector)


if __name__ == '__main__':
  main()