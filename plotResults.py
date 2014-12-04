import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import scipy
from scipy import ndimage
import learning

def main():
  a = "someSuccess_10000_12_10_10.txt"
  factor = 1000
  list_of_filenames = [a, a, a, a, a, a, a, a, a, a]
    
  file_lengths = []
  for x in range(1, 11, 1):
    file_lengths.append(x*factor)

  fl = getData(list_of_filenames, file_lengths)

  use_colors = {0: "red", 1: "blue", 2: "green", 3: "black", 4: "pink", 5: "orange", 6: "purple", \
  7: "cyan", 8: "magenta", 9: "white" }
  
  fig = plt.figure()
  ax = plt.subplot(111)

  # Add plot points
  for x in range (0, len(fl)):
    ax.plot(fl[x], 'ro', c = use_colors[x], label=str((x+1)*factor))
  
  #Resize plot
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width*.8, box.height])


  # Add legend
  temp = " trials"
  legend_list = []

  for x in range(0, len(fl)):
    
    legend_list.append((str((x+1)*factor) + temp))

  ax.legend(legend_list, bbox_to_anchor=(1.4, 1))
  
  # Labels
  plt.ylabel('score')
  plt.xlabel('factor')

  
  # Axes
  plt.xlim(-1, 25)
  minorLocator = MultipleLocator(1)
  plt.axes().xaxis.set_minor_locator(minorLocator)

  plt.show()
  


def getData(list_of_filenames, file_lengths):
  lof = list_of_filenames
  fl = file_lengths
  factorList = []

  for x in range(0, len(lof)):
    data = learning.getData(lof[x], fl[x])
    A = data[4]
    b = data[5]

    x_tuple = learning.normalEquation(A, b, False)
    
    shape = x_tuple[1] 
    x = x_tuple[0]

    factorList.append(x)

  return factorList


if __name__ == "__main__":
  main()

    
    