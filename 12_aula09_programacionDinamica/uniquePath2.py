def uniquePath2(obstacleGrid: list):
  """
  Este algoritmo resuelve el siguiente ejercicio:
  Unique Path II
  https://leetcode.com/problems/unique-paths-ii/

  Este algoritmo retorna el número de caminos únicos que puede seguir un robot
  para llegar a la meta. El robot se ubica en la posición superior izquierda y
  la meta en la posición inferior derecha de un arreglo. El arreglo
  representa un mapa con caminos (0) y obstáculos (1).
  """

  OBSTACLE = 1
  roads = [[0 for y in x] for x in obstacleGrid]
  m = len(roads)
  n = len(roads[0])

  if obstacleGrid[0][0] == OBSTACLE:
    return 0
  if m == 1 and n == 1:
    return 1

  roads[0][0] = 1
  for col in range(1, n):
    if obstacleGrid[0][col] != OBSTACLE:
      left = roads[0][col - 1]
      roads[0][col] = left

  for row in range(1, m):
    for col in range(n):
      if obstacleGrid[row][col] != OBSTACLE:
        top = roads[row - 1][col]
        left = roads[row][col - 1]
        roads[row][col] = top + left
  
  return roads[-1][-1]

def display(a):
  """
  Este programa imprime de forma ordenada las filas y columnas de un arreglo
  bidimensional.
  """
  for i in a:
    print(i)

# Test
obstacles = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]]
display(obstacles)
print(f'uniquePath2(obstacles): {uniquePath2(obstacles)}\n')

obstacles = [
  [0, 0, 0, 1, 1],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0]]
display(obstacles)
print(f'uniquePath2(obstacles): {uniquePath2(obstacles)}\n')

obstacles = [
  [0, 0, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 0, 0]]
display(obstacles)
print(f'uniquePath2(obstacles): {uniquePath2(obstacles)}\n')

obstacles = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0],
  [1, 0, 1],
  [0, 0, 0]]
display(obstacles)
print(f'uniquePath2(obstacles): {uniquePath2(obstacles)}\n')

obstacles = [
  [0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 0, 0, 0]]
display(obstacles)
print(f'uniquePath2(obstacles): {uniquePath2(obstacles)}\n')