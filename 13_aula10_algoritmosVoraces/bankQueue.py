# Bank Queue
import heapq

def bankQueue():
  inputArray = [int(x) for x in input().split()]
  N = inputArray[0]
  T = inputArray[1]

  amounts = [[] for i in range(T)]
  waitMore = []

  for i in range(N):
    inputArray = [int(x) for x in input().split()]
    amount = inputArray[0]
    time = inputArray[1]
    if time < T:
      heapq.heappush(amounts[time], amount)
    else:
      heapq.heappush(waitMore, amount)

  extra = 1
  maxAmount = 0
  time = 0
  while time < T:
    while extra > 0:
      if len(amounts[time]) == 0:
        extra += 1
        break

      # Selección de monto actual
      auxList = amounts[time]
      if len(waitMore) > 0 and amounts[time][-1] < waitMore[-1]:
        auxList = waitMore

      # Menor monto de tiempo superior
      hasMin = -1
      minAmount = float('inf')
      for i in range(time + 1, T):
        if len(amounts[i]) == 0 and hasMin == -1:
          break        
        #elif len(amounts[i]) > 1:
        elif len(amounts[i]) > 0:
          if amounts[i][0] < minAmount:
            minAmount = amounts[i][0]
            hasMin = i
      
      # Limpiar listas
      if hasMin != -1:
        if auxList[-1] >= minAmount or len(amounts[hasMin]) == 1:
          maxAmount += auxList.pop()
          if len(amounts[hasMin]) > 1:
            amounts[hasMin].pop(0)
        else:
          maxAmount += amounts[hasMin].pop(0)
      else:
        maxAmount += auxList.pop()

      extra -= 1

    if extra == 0:
      extra = 1
    time += 1

  return maxAmount

# Main
print(bankQueue())
"""
4 4
1000 1
2000 2
500 2
1200 0

3 4
1000 0
2000 1
500 1

4 4
1000 0
2000 2
500 1
1000 2

4 4
1000 0
1500 2
2000 3
1000 2
"""