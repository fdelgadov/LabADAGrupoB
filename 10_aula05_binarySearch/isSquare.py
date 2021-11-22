# Este algoritmo determina si el número ingresado es un número cuadrado
# utilizando el método de búsqueda binaria
# El algoritmo trabaja con un arreglo "imaginario" de la forma [0, ..., n]
# Retorna True si el número es cuadrado; de lo contrario, False.
def isSquare(number):
  left = 0
  right = number
  while left <= right:
    mid = left + (right - left) / 2
    mid = int(mid)
    quotient = int(number / mid)
    if quotient == mid:
      if number % mid == 0:
        return True
      else:
        return False
    if quotient > mid:
      left = mid + 1
    else:
      right = mid - 1
  return False

# Test
x = 9
print(f'isSquare({x}): {isSquare(x)}')
x = 10
print(f'isSquare({x}): {isSquare(x)}')
x = 4
print(f'isSquare({x}): {isSquare(x)}')
x = 7
print(f'isSquare({x}): {isSquare(x)}')
x = 49
print(f'isSquare({x}): {isSquare(x)}')
x = 39
print(f'isSquare({x}): {isSquare(x)}')
x = 36
print(f'isSquare({x}): {isSquare(x)}')
x = 2
print(f'isSquare({x}): {isSquare(x)}')
x = 3
print(f'isSquare({x}): {isSquare(x)}')
x = 144
print(f'isSquare({x}): {isSquare(x)}')