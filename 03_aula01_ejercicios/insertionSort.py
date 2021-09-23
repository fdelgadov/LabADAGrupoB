# Este programa ordena de manera creciente un arreglo, utilizando el algoritmo
# insertionSort. Calcula e imprime el tiempo que tomó el proceso, en segundos

import time

def insertionSort(array: list):
  for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
      array[i + 1] = array[i]
      i -= 1
    array[i + 1] = key

# Test
array = list(range(10000, 0, -1))
tic = time.perf_counter()
insertionSort(array)
tac = time.perf_counter()
print(f"InsertionSort: {tac - tic:0.4f} segundos")