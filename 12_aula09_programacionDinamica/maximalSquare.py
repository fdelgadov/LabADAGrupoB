def maximalSquare(matrix: list[list[str]]):
  """
  Este programa resuelve el ejercicio: Maximal Square
  Link: https://leetcode.com/problems/maximal-square/

  El programa retorna el area del cuadrado más grande encontrado en una matriz 
  de 1's y 0's. El cuadrado debe contener solo 1's.
  """
  rows = len(matrix)
  cols = len(matrix[0])
  maxSquareArr = [[0 for y in range(cols + 1)] for x in range(rows + 1)]
  maxSquare = 0

  for i in range(1, rows + 1):
    for j in range(1, cols + 1):
      if matrix[i - 1][j - 1] == '1':
        top = maxSquareArr[i - 1][j]
        left = maxSquareArr[i][j - 1]
        topLeft = maxSquareArr[i - 1][j - 1]
        maxSquareArr[i][j] = min(top, left, topLeft) + 1
        maxSquare = max(maxSquare, maxSquareArr[i][j])
  
  return maxSquare * maxSquare

# Test
test = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]]
print(maximalSquare(test))

test = [
  ["0","1"],
  ["1","0"]]
print(maximalSquare(test))