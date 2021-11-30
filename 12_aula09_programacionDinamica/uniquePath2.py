def uniquePath2(obstacleGrid: list):
  """
  Este algoritmo resuelve el siguiente ejercicio:
  Unique Path II
  https://leetcode.com/problems/unique-paths-ii/
  """
  ROBOT = 2
  GOAL = 3
  OBSTACLE = 1
  ROAD = 1

  roads = [[0 for y in x] for x in obstacleGrid]
  uniquePaths = 0

  # Robot position
  row = 0
  col = 0

  obstacleGrid[0][0] = ROBOT
  obstacleGrid[-1][-1] = GOAL

  for col in range(len(roads[0])):
    if row != 0 or roads[row - 1][col] == ROAD:
      down = obstacleGrid[row][col]

      if down != OBSTACLE:
        roads[row][col] = 1

      if obstacleGrid[row][col] == GOAL:
        uniquePaths += 1

  print(f'{row} {col}')

"""
  right = obstacleGrid[row][col + 1]
  while right != OBSTACLE:
    down = obstacleGrid[row + 1][col]

    if down != OBSTACLE:
      roads[row][col] = 1
    else:
      roads[row][col] = 0

    col += 1
    if col >= len(roads):
      col = 0
      row += 1
    right = obstacleGrid[row][col]
"""
# Test
obstacles = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]]
uniquePath2(obstacles)