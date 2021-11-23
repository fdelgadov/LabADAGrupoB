# Este programa busca un número en una lista utilizando el método de búsqueda
# binaria.
# El programa retorna el índice del número en la lista.
# Retorna -1 cuando no lo encuentra.
def binarySearch(array, target):
  left = 0
  right = len(array) - 1
  while left <= right:
    mid = left + (right - left) // 2
    if array[mid] == target:
      return mid
    if array[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

array = [2, 14, 23, 52, 65]
print(f'binarySearch(array, 14): {binarySearch(array, 14)}')