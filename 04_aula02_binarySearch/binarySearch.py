def binarySearch(array, search):
  min = 0
  max = len(array) - 1
  while True:
    if max == min:
      if search == array[max]:
        return True
      else:
        return False
    pivotIdx = int((max + min)/2)
    print(f"{min} {max} {pivotIdx}") # debug
    if search < array[pivotIdx]:
      max = pivotIdx - 1
    else:
      min = pivotIdx + 1

# Test
a = [1, 4, 8, 12, 16, 19, 22, 26, 29, 30, 37, 44]
print(binarySearch(a, 25))