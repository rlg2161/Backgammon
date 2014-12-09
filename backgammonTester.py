# Wrapper program for backgammon GUI, playing methods and AI (to be added later)

import backgammon as bg 
import backgammonGUI as bgGUI 
import dice

def main():

  backgammonTester('try_strat_file2001.txt', 'r')


def backgammonTester(stratFile):
  try_strat_file = open(stratFile, 'r')
  factors_list = []
  
  for x in range(0,4):
    try_strat_file.readline()

  line = try_strat_file.readline()
  splitLine = line.split()


  for item in splitLine:
    factors_list.append(float(item))
  

  gui = bgGUI.backgammonGUI(factors_list)
  




if __name__ == "__main__":
  main()