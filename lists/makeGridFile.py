# used by makeGrid to print contents nicely to console
def printGrid(grid):
  for row in grid:
    rowStr = '';
    for item in row:
      rowStr = rowStr + item + ' '
    print(rowStr)

# constructs grid with r rows and c columns and fills each element with value of char
# returns grid and prints grid to screen
# call by:
#   makeGrid(2, 3, 'G')
# prints to console:
#   G G G
#   G G G
# returns:
#   [
#     ['G', 'G', 'G',],
#     ['G', 'G', 'G',]
#   ]
def makeGrid(r, c, char):
  list = []
  for i in range(c):
    list.append(char)

  grid = []
  for i in range(r):
    grid.append(list[0:])

  printGrid(grid)