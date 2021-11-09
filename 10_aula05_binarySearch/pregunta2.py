# Enunciado:
# Encuentre el primer valor mayor o igual que x

# Este algoritmo retorna el primer número mayor o igual que x en el
# arreglo.
# Retorna -1 si ningún número es mayor o igual

def firstMajorNumber(array, x):
  left = 0
  right = len(array) - 1
  while left <= right:
    mid = left + (right - left) / 2
    mid = int(mid)
    if array[mid] == x:
      return mid
    if array[mid] < x:
      left = mid + 1
    else:
      right = mid - 1
  mid += 1
  if len(array) <= mid:
    return -1
  else:
    return mid

array = [2, 14, 23, 52, 65]
print(f'binarySearch(array, 14): {firstMajorNumber(array, 100)}')
array = [2, 14, 23, 52, 65, 100, 1233]
print(f'binarySearch(array, 14): {firstMajorNumber(array, 70)}')