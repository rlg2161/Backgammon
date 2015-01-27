#!/usr/bin/env python
import sys
import backgammon as bg

if (len(sys.argv) != 5):
  print "Usage == ./genSimsScript.py <# strats to sim> <# matches> <# points per match> <output file name>"
  sys.exit(0)
else:
  num_games = int(sys.argv[1])
  mps = int(sys.argv[2])
  ppm = int(sys.argv[3])
  out_file = sys.argv[4]

  bg.generateSimulations(num_games, 12, 10, mps, ppm, out_file)

#backgammon.py


#def main():
  #if (len(sys.argv) == 0):
    #simulate_command(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
  #else:
    #print "usage: <num_games> <mps> <ppm> <file_name> "

#def simulate_command(num_games, mps, ppm, name):
  #start = datetime.today()
  #start = str(start)

  #print start
  #backgammon.generateSimulations(int(num_games), 12, 10, int(mps), int(ppm), name)
  #end = datetime.today()
  #end = str(end)
  #print end

  #summary_file = open("summaryFile.txt", 'w')
  #success_strats_file = open("someSuccess.txt", 'r')

  #for line in success_strats_file:
    #print line
    #print "\n\n\n\n\n"


#def print_string(string):
  #subprocess.Popen(['echo', string], shell =False)

