import numpy as np


def main():
  data = getData('someSuccess.txt')
  A = data[0]
  b = data[1]
  
  try_strat_file = open("tryStratFile.txt", 'w')

  print "A: "
  print A.shape
  print A

  print "b: "
  print b.shape
  b.shape = (158, 1)
  print "b after col conversion: "
  print b.shape
  print b

  # Generate Optimal Move Weighting Array 

  ATranspose = A.transpose()
  print "ATranspose: "
  print ATranspose
  print "ATranspose shape: ",
  print ATranspose.shape

  #nextMatrix = np.dot(ATranspose, A)
  #print nextMatrix
  #print "nextMatrix shape: ",
  #print nextMatrix.shape
  
  AT_A = np.dot(ATranspose, A)

  AT_Ainv = np.linalg.inv(AT_A)
  print AT_Ainv
  print "inv shape: ",
  print AT_Ainv.shape


  AT_Ainv_AT = np.dot(AT_Ainv, ATranspose)

  print "AT_Ainv_AT shape: ",
  print AT_Ainv_AT.shape
  print AT_Ainv_AT
  

  print b
  print b.shape

  x = np.dot(AT_Ainv_AT, b)

  print "Final Weights: "
  print x
  shape = x.shape
  print shape

  for i in range(0, shape[0]):
    try_strat_file.write(str(x[i,0]) + " ")
  
  try_strat_file.close()


def getData(filename):
  A = None
  vectorList = []
  solutionList = []
  in_file = open(filename, 'r')
  test = ''
  
  for x in range(0, 158):
    rand_score = in_file.readline()
    rand_score_split = rand_score.split()

    strat_score = in_file.readline()
    strat_score_split = strat_score.split()
    test = strat_score_split[3]
    test_val = int(test)

    strat = in_file.readline()
    strat_split = strat.split()

    in_file.readline()
    in_file.readline()

    #if (test_val < 25 ):
      # so as to only keep track of and use "good" strategies to learn
      
      #continue

    solutionList.append(int(strat_score_split[3]))
   
    for x in range(0, len(strat_split)):
      strat_split[x] = float(strat_split[x])
    
    #strat_split.insert(0, 1.0)

    vectorList.append(strat_split)
  
  b = np.array(solutionList)
  A = np.array(vectorList)

  return (A, b)


if __name__ == '__main__':
  main()