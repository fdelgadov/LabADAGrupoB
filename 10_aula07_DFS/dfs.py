def dfs(array, x, y, color):
  # Este algoritmo pinta todos los casilleros 0 a partir de un casillero.
  # El método para el pintado es DFS. Un color esta representado por un caracter.
  # El algoritmo retorna el arreglo luego de ser pintado.

  array[x][y] = color
  dx = [x - 1, x, x + 1, x]
  dy = [y, y + 1, y, y - 1]
  for i in range(4):
    if dx[i] < len(array) and dy[i] < len(array[0]):
      value = array[dx[i]][dy[i]]
      if value == '0':
        dfs(array, dx[i], dy[i], color)

def display(array):
  for row in array:
    print(f'{row}')
  print()

# Test
array = [['#', '#', '#', '#', '#', '#'],
         ['#', '0', '0', '0', '0', '#'],
         ['#', '0', '0', '0', '0', '#'],
         ['#', '0', '0', '0', '0', '#'],
         ['#', '0', '0', '0', '#', '0'],
         ['#', '#', '#', '#', '0', '0']]
display(array)
dfs(array, 2, 2, '3')
display(array)
dfs(array, 4, 5, '4')
display(array)