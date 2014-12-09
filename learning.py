import numpy as np


def main():
  learningFxn("someSuccess_2001_12_10_10.txt", 2001, "tryStratFile2001.txt", True)

def learningFxn(inFileName, sizeInput, outFileName, print_flag):
  data = getData(inFileName, sizeInput)
  genFactors = data[0:5]
  if (print_flag):
    print genFactors
  A = data[5]
  b = data[6]
  
  try_strat_file = open(outFileName, 'w')

  x_tuple = normalEquation(A, b, True)

  shape = x_tuple[1]
  x = x_tuple[0]

  if (print_flag):
    print "shape"
    print shape

    print "x"
    print x
    #print x[1]
 
  for h in range(0, 5):
    try_strat_file.write(str(data[h]))
  
  for i in range(0, shape[0]):
    try_strat_file.write(str(x[i]) + " ")
  
  try_strat_file.close()
  

def normalEquation(A, b, print_flag):
  if (print_flag):
    print "A: "
    print A.shape
    print A

    print "b: "
    print b.shape

  #b.shape = (4074, 1)
  
  if (print_flag):
    print "b after col conversion: "
    print b.shape
    print b

  # Generate Optimal Move Weighting Array 

  ATranspose = A.transpose()
  if (print_flag):
    print "ATranspose: "
    print ATranspose
    print "ATranspose shape: ",
    print ATranspose.shape

    
  AT_A = np.dot(ATranspose, A)

  AT_Ainv = np.linalg.inv(AT_A)
  if (print_flag):
    print AT_Ainv
    print "inv shape: ",
    print AT_Ainv.shape


  AT_Ainv_AT = np.dot(AT_Ainv, ATranspose)
  if (print_flag):
    print "AT_Ainv_AT shape: ",
    print AT_Ainv_AT.shape
    print AT_Ainv_AT
  

    print b
    print b.shape

  x = np.dot(AT_Ainv_AT, b)

  if (print_flag):
    print "Final Weights: "
    print x
  
  shape = x.shape

  return (x, shape)

def getData(filename, length):
  A = None
  vectorList = []
  solutionList = []
  in_file = open(filename, 'r')
  test = ''
  
  num_games = in_file.readline()
  fia = in_file.readline()
  factor = in_file.readline()
  mps = in_file.readline()
  ppm = in_file.readline()

  #print str(num_games)
  #print str(fia)
  #print str(factor)
  #print str(mps)
  #print str(ppm)
  
  for x in range(0, length):
    #print x
    rand_score = in_file.readline()
    rand_score_split = rand_score.split()
    #print rand_score


    strat_score = in_file.readline()
    strat_score_split = strat_score.split()
    #print strat_score_split
    test = strat_score_split[4]
    #print test

    strat = in_file.readline()
    strat_split = strat.split()
    #print strat_split

    in_file.readline()
    in_file.readline()

    #if (int(test) < 7):
      #continue


    solutionList.append(int(test))
   
    for x in range(0, len(strat_split)):
      strat_split[x] = float(strat_split[x])
    
    #strat_split.insert(0, 1.0)

    vectorList.append(strat_split)
  
  b = np.array(solutionList)
  A = np.array(vectorList)

  return (num_games, fia, factor, mps, ppm, A, b)


if __name__ == '__main__':
  main()