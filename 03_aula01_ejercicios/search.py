# Este programa permite saber si un elemento está en un arreglo y calcula e
# imprime el tiempo que tomó el proceso, en segundos

import time

def search(search, array):
  for item in array:
    if search == item:
      return True
  
  return False

# Test
array = list(range(10000, 0, -1))
tic = time.perf_counter()
search(14, array)
tac = time.perf_counter()
print(f"Search(14): {tac - tic:0.4f} segundos")
array = list(range(1000000, 0, -1))
tic = time.perf_counter()
search(1245, array)
tac = time.perf_counter()
print(f"Search(1245): {tac - tic:0.4f} segundos")