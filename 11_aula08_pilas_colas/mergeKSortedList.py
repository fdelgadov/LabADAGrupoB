import heapq

def mergeKSortedList(arr):
  # Este programa fusiona y ordena los números de una lista de listas

  heap = []
  for i in arr:
    for j in i:
      heapq.heappush(heap, j)

  return heapq.nsmallest(len(heap), heap)

# Test
arr = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(f'{arr}\n{mergeKSortedList(arr)}')

arr = [[1, 5, 2], [6, 2, 4], [5, 3, 3, 9]]
print(f'{arr}\n{mergeKSortedList(arr)}')

arr = [[5, 5, 5], [3, 2, 1, 6, 1, 1], [7, 8]]
print(f'{arr}\n{mergeKSortedList(arr)}')