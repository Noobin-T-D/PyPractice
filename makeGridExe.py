import sys, getopt
import makeGridFile


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


def main(argv):
  if(len(argv) > 0):
    makeGridWithOpts(argv)
  else:
    makeGridFile.makeGrid(5, 5, 'X')


main(sys.argv[1:])