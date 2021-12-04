# Book Shop

def bookShop():
  """
  Este programa resuelve el siguiente ejercicio: Book Shop
  Link: https://cses.fi/problemset/task/1158

  Este programa retorna el máximo número de páginas que se pueden conseguir
  comprando libros dados el precio y páginas de los libros disponibles y la
  cantidad de dinero disponible.
  """
  inputLine = input()
  inputArray = inputLine.split()
  inputArray = [int(x) for x in inputArray]
  numBooks = inputArray[0]
  totalPrice = inputArray[1]

  inputLine = input()
  inputArray = inputLine.split()
  inputArray = [int(x) for x in inputArray]
  prices = inputArray

  inputLine = input()
  inputArray = inputLine.split()
  inputArray = [int(x) for x in inputArray]
  pages = inputArray

  bag = [[0 for y in range(totalPrice + 1)] for x in range(numBooks + 1)]

  for i in range(1, len(bag)):
    price = prices[i - 1]
    page = pages[i - 1]

    for j in range(1, len(bag[0])):
      if j - price < 0:
        bag[i][j] = bag[i - 1][j]
      elif bag[i - 1][j - price] + page > bag[i - 1][j]:
        bag[i][j] = bag[i - 1][j - price] + page
      else:
        bag[i][j] = bag[i - 1][j]
        
  return bag[-1][-1]

def display(a):
  """
  Este programa imprime de forma ordenada las filas y columnas de un arreglo
  bidimensional.
  """
  for i in a:
    print(i)

print(bookShop())

# Test
"""
Input:
4 10
4 8 5 3
5 12 8 1
"""
# print(f'bookShop(): {bookShop()}')

# Otros input
"""
4 10
4 8 5 3
5 12 8 1

10 10
1 2 10 6 5 1 7 4 10 4
6 3 8 1 7 3 8 6 5 6

4 10
4 8 6 3
5 12 8 1
"""