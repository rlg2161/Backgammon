import numpy as np


def main():
  getData('someSuccess.txt')

def getData(filename):
  gameMatrix = None
  vectorList = []
  in_file = open(filename, 'r')
  test = ''
  
  try:
    while (True):
      rand_score = in_file.readline()
      rand_score_split = rand_score.split()

      strat_score = in_file.readline()
      strat_score_split = strat_score.split()

      strat = in_file.readline()
      strat_split = strat.split()
      for x in range(0, len(strat_split)):
        strat_split[x] = float(strat_split[x])

      in_file.readline()
      test = in_file.readline()
      #if (test == '1'):
        #print "TEST " + str(test)
        #raw_input("wait")

      #print int(rand_score_split[3])
      #print int(strat_score_split[3])
      strat_split.insert(0, 1.0)
      print strat_split

      #arr = np.array(strat_split)

      #print arr
      #print arr.shape
      print len(strat_split)

      vectorList.append(strat_split)
      #print vectorList
      #raw_input("wait")
  
  except:
    #print len(vectorList)
    #gameMatrix = np.matrix(vectorList)
    #print gameMatrix.shape



  #raw_input("wait")



  




if __name__ == '__main__':
  main()