#def bookShop(PricePage: list, numBooks: int, totalPrice: int):
def bookShop():
  """
  numBooks = int(input())
  totalPrice = int(input())

  prices = [int(input()) for x in range(numBooks)]
  pages = [int(input()) for x in range(numBooks)]

  #print(f'{numBooks} {totalPrice}\n{prices}\n{pages}')
  """
  #"""
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
  #"""

  bag = [[0 for y in range(totalPrice + 1)] for x in range(numBooks + 1)]

  for i in range(1, len(bag)):
    #price = PricePage[0][i - 1]
    #page = PricePage[1][i - 1]
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

# Test
"""
Input
4 10
4 8 5 3
5 12 8 1
"""
print(f'bookShop(): {bookShop()}')