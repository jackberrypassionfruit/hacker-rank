from copy import deepcopy

def smartBomb(j, i, grid):
  if grid[j][i] != 4:
    grid[j][i] = 0

def round(grid):
  for j in range(len(grid)):
      for i in range(len(grid[0])):
        grid[j][i] += 1
      
  # Blowing up surrounding bombs first
  for j in range(len(grid)):
      for i in range(len(grid[0])):
        if grid[j][i] == 4: 
          # print('i: ', i, 'j: ', j)
          smartBomb(j, i, grid)
          # Maxes and mins keep us from blowing up outside the game area
          smartBomb(min( j+1, len(grid)-1 ), i, grid)
          smartBomb(max( j-1, 0), i, grid)
          smartBomb(j, min( i+1, len(grid[0])-1 ), grid)
          smartBomb(j, max( i-1, 0), grid)
  
  # Then blowing up bombs themselves
  # Because round() operates in place, this way remembers the bombs yet to blow up
  for j in range(len(grid)):
        for i in range(len(grid[0])):
          if grid[j][i] == 4: 
            grid[j][i] = 0
  return grid

def bomberMan(n, grid):
  if n == 0:
    return grid
  # To save computation time, we'll record the outcomes only up to 9, because they repeat after that
  grids = []
  
  
  # Converting each row from string to list, so I can manipulate
  for rowI in  range(len(grid)):
    grid[rowI] = list(grid[rowI])
  
  # Changing the periods and Os to numbers, which represent the state of the bombs
  for j in range(len(grid)):
    for i in range(len(grid[0])):
      if grid[j][i] == 'O': 
        # print('i: ', i, 'j: ', j)
        grid[j][i] = 1
      else:
        grid[j][i] = 0
        
        
  # Playing the game
  for i in range(9):
    if i < 1:
      for j in range(len(grid)):
        for i in range(len(grid[0])):
          if grid[j][i] != 0:
            grid[j][i] += 1
    else:
      grid = round(grid)
    grids.append(deepcopy(grid))
    
  # makes sure my answer is within the finite number or grids that I stored in memory
  result = grids[n % 9 % 5 + 5 - 1]
      
  # Converting back to string form
  for rowNum in range(len(result)):
    for colNum in range(len(result[0])):
      # grid[rowNum][colNum] = str(grid[rowNum][colNum])
      if result[rowNum][colNum] != 0:
        result[rowNum][colNum] = 'O'
      else:
        result[rowNum][colNum] = '.'
    result[rowNum] = ''.join(result[rowNum])
    
  
  ## Print the result grid
  for row in result:
    print(row) 
  
  # return result
  
grid1 = [
  '.......', 
  '...O...', 
  '....O..', 
  '.......', 
  'OO.....', 
  'OO.....'
]

grid2 = [
  '...',
  '.O.',
  '...'
]

grid3 = [
  '.......', 
  '...O...', 
  'OO..O..', 
  '...O...', 
  'OO.....', 
  '.O.....'
]

grid4 = [
  '......OO...O.',
  '...O...O.....',
  '..OO.......O.',
  '......OO...OO',
  'O......O....O',
  '......OO...O.',
  'OOO..........',
  '......OO...O.',
  
]


print(bomberMan(0, grid1))