
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