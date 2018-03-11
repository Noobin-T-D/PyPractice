import sys, getopt

def printGrid(grid):
  for row in grid:
    rowStr = '';
    for item in row:
      rowStr = rowStr + item + ' '
    print(rowStr)


def makeGrid(r, c, char):
  list = []
  for i in range(c):
    list.append(char)

  grid = []
  for i in range(r):
    grid.append(list[0:])

  printGrid(grid)


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
  
  makeGrid(r, c, x)


def main(argv):
  if(len(argv) > 0):
    makeGridWithOpts(argv)
  else:
    makeGrid(5, 5, 'X')


main(sys.argv[1:])