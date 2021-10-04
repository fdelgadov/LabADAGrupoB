import time

def binarySearch(array, search):
  min = 0
  max = len(array) - 1
  pivotIdx = -1
  while True:
    #print(f"{min} {max} {pivotIdx}") # debug
    if max <= min:
      if search == array[max]:
        return True
      else:
        return False
    pivotIdx = int((max + min)/2)
    #print(f"{min} {max} {pivotIdx}") # debug
    if search < array[pivotIdx]:
      max = pivotIdx - 1
    elif search > array[pivotIdx]:
      min = pivotIdx + 1
    else:
      return True

# Test
a = [1, 4, 8, 12, 16, 19, 22, 26, 29, 30, 37, 44]
print(binarySearch(a, 25))
print(binarySearch(a, 16))

a = [x for x in range(1, 10000)]
tic = time.perf_counter()
print(binarySearch(a, 4265))
tac = time.perf_counter()
print(f"Binary Search 10000: {tac - tic:0.4f} segundos")

a = [x for x in range(3, 100000)]
tic = time.perf_counter()
print(binarySearch(a, 42650))
tac = time.perf_counter()
print(f"Binary Search 100000: {tac - tic:0.4f} segundos")

a = [x for x in range(1, 100000)]
tic = time.perf_counter()
print(binarySearch(a, 42653))
tac = time.perf_counter()
print(f"Binary Search 100000: {tac - tic:0.4f} segundos")

a = [x for x in range(1, 1000000)]
tic = time.perf_counter()
print(binarySearch(a, 426533))
tac = time.perf_counter()
print(f"Binary Search 1000000: {tac - tic:0.4f} segundos")

a = [x for x in range(1, 100000000)]
tic = time.perf_counter()
print(binarySearch(a, 42653334))
tac = time.perf_counter()
print(f"Binary Search 100000000: {tac - tic:0.4f} segundos")