# libraries imported here for grabbing arguments from the command line
import sys, getopt

# import all the functions in makeGridFile
# a function with name funcName imported this way can be called as makeGridFile.funcName(arguments...)
import makeGridFile


# parses the command line arguments and passes them to the makeGrid function
def makeGridWithOpts(argv):
  r = 0
  c = 0
  x = 'X'
  
  opts = getopt.getopt(argv, 'r:c:x:')
  for opt, arg in opts[0]:
    if opt == '-r':
      r = int(arg)
    elif opt == '-c':
      c = int(arg)
    elif opt == '-x':
      x = arg
  
  makeGridFile.makeGrid(r, c, x)


# the function that is activated when the file is run
# decides whether to use command line arguments or default settings to make grid
def main(argv):
  if(len(argv) > 0):
    makeGridWithOpts(argv)
  else:
    makeGridFile.makeGrid(5, 5, 'X')


# called via command line
# eg. (in command line)
#   python makeGridExe.py -r 5 -c 3 -x *
#   outputs -->  *****
#                *****
#                *****
main(sys.argv[1:])