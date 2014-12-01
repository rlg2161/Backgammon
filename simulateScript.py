import subprocess
import backgammon
import datetime

def main():
  if (len(sys.argv) == 0):
    simulate_command(sys.argv[0], sys.argv[1])
  else:
    print "usage: <# strats>; <# games> "

def simulate_command(strats, games, print_counter = True, repeat = 1):
  start = datetime.today()
  start = str(start)

  subprocess.Popen('echo "%s"' %start, shell = True) 
  backgammon.generateSimulations(strats, 21, 10, games)
  end = datetime.today()
  end = str(end)
  subprocess.Popen('echo "%s"' %start, shell = True) 
  #print end

  summary_file = open("summaryFile.txt", 'w')
  success_strats_file = open("someSuccess.txt", 'r')

  for line in success_strats_file:
    print line
    print "\n\n\n\n\n"


def print_string(string):
  subprocess.Popen(['echo', string], shell =False)


if __name__ == '__main__':
  main()