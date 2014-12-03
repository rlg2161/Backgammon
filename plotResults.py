import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import scipy
from scipy import ndimage
import learning

def main():
  a = "someSuccess_10000_12_10_10.txt"
  list_of_filenames = [a, a, a, a, a, a, a]#, a, a, a]
  file_lengths = [100, 200, 300, 400, 500, 600, 700]#, 800, 900, 1000]
  fl = getData(list_of_filenames, file_lengths)

  use_colors = {0: "red", 1: "blue", 2: "green", 3: "black", 4: "pink", 5: "orange", 6: "purple", \
  7: "cyan", 8: "magenta", 9: "white" }
  
  for x in range (0, len(fl)):
    plt.plot(fl[x], 'ro', c = use_colors[x])
  
  plt.ylabel('score')
  plt.xlabel('factor')
  plt.xlim(-1, 24)

  

  minorLocator = MultipleLocator(1)

  plt.axes().xaxis.set_minor_locator(minorLocator)


  plt.show()
  
  #print fl[0]


def getData(list_of_filenames, file_lengths):
  lof = list_of_filenames
  fl = file_lengths
  factorList = []

  for x in range(0, len(lof)):
    data = learning.getData(lof[x], fl[x])
    A = data[0]
    b = data[1]

    x_tuple = learning.normalEquation(A, b, False)
    
    shape = x_tuple[1] 
    x = x_tuple[0]

    factorList.append(x)

  return factorList


if __name__ == "__main__":
  main()

    
    