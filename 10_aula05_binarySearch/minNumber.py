# Este algoritmo retorna el menor número de un arreglo ordenado rotado
# (desplazado)
# El algoritmo retorna el índice del número en el arreglo
# Si no encuentra el número retorna -1
def minNumber(array):
  if array[0] < array[-1]:
    return 0

  left = 0
  right = len(array) - 1
  first = array[0]
  while left < right - 1:
    mid = left + (right - left) // 2
    if array[mid] > first:
      left = mid
    else:
      right = mid
  if array[left] < array[right]:
    return left
  else:
    return right

array = [6, 7, 9, 15, 19, 2, 3]
print(f'minNumber(array): {minNumber(array)}')
array = [18, 23, 4, 5, 7, 10, 14, 16]
print(f'minNumber(array): {minNumber(array)}')
array = [9, 15, 19, 2, 3, 6, 7]
print(f'minNumber(array): {minNumber(array)}')
array = [2, 3, 6, 7, 9, 15, 19]
print(f'minNumber(array): {minNumber(array)}')