# Enunciado:
# Encuentre el primer valor mayor o igual que x

# Este algoritmo retorna el índice del primer número mayor o igual que x en el
# arreglo.
# Retorna -1 si ningún número es mayor o igual

def firstMajorNumber(array, x):
  left = 0
  right = len(array) - 1
  while left <= right:
    mid = left + (right - left) // 2
    if array[mid] == x:
      return mid
    if array[mid] < x:
      left = mid + 1
    else:
      right = mid - 1
  if len(array) <= mid + 1:
    return -1
  if x < array[mid]:
    return mid
  else:
    return mid + 1

# Test
array = [2, 14, 23, 52, 65]
print(array)
print(f'firstMajorNumber(array, 100): {firstMajorNumber(array, 100)}')
print(f'firstMajorNumber(array, 10): {firstMajorNumber(array, 10)}')

array = [2, 14, 23, 52, 65, 100, 1233]
print(array)
print(f'firstMajorNumber(array, 70): {firstMajorNumber(array, 70)}')
print(f'firstMajorNumber(array, 1): {firstMajorNumber(array, 1)}')
print(f'firstMajorNumber(array, 23): {firstMajorNumber(array, 23)}')
print(f'firstMajorNumber(array, 10): {firstMajorNumber(array, 10)}')