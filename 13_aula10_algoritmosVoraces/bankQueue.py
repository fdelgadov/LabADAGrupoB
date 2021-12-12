# Bank Queue
def bankQueue():
  inputArray = [int(x) for x in input().split()]
  N = inputArray[0]
  T = inputArray[1]

  amounts = []
  times = []
  queue = [x for x in range(N)]

  maxAmount = 0

  for i in range(N):
    inputArray = [int(x) for x in input().split()]
    amounts.append(inputArray[0])
    times.append(inputArray[1])

  for time in range(T):
    auxQueue = []
    auxAmount = 0
    auxMax = 0
    auxMaxIdx = -1

    for i in queue:
      if times[i] == time:
        auxAmount = max(auxAmount, amounts[i])
      else:
        auxQueue.append(i)
        if auxMax < amounts[i]:
          auxMax = amounts[i]
          auxMaxIdx = i

    if auxAmount != 0:
      maxAmount += auxAmount
    elif auxMax != 0:
      maxAmount += auxMax
      auxQueue.remove(auxMaxIdx)
      auxMax = 0
      auxMaxIdx = -1

    queue = auxQueue
  
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