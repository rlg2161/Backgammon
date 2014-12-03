import numpy as np


def main():
  data = getData('someSuccess_1000_12_10_10.txt')
  A = data[0]
  b = data[1]
  
  try_strat_file = open("tryStratFile.txt", 'w')

  x_tuple = normalEquation(A, b, True)

  shape = x_tuple[1]
  x = x_tuple[0]

  print "shape"
  print shape

  print "x"
  print x
  #print x[1]

  for i in range(0, shape[0]):
    #print i
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
  
  for x in range(0, length):
    rand_score = in_file.readline()
    rand_score_split = rand_score.split()

    strat_score = in_file.readline()
    strat_score_split = strat_score.split()
    test = strat_score_split[3]

    strat = in_file.readline()
    strat_split = strat.split()

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

  return (A, b)


if __name__ == '__main__':
  main()