# Wrapper program for backgammon GUI, playing methods and AI (to be added later)

import backgammon as bg 
import backgammonGUI as bgGUI 
import dice

def main():

  #die = dice.oneDie(6)

  try_strat_file = open('tryStratFile.txt', 'r')
  factors_list = []
  
  line = try_strat_file.readline()
  splitLine = line.split()

  for item in splitLine:
    factors_list.append(float(item))
  

  gui = bgGUI.backgammonGUI(factors_list)
  




if __name__ == "__main__":
  main()