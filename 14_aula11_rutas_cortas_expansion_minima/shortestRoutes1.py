# Shortest Routes
def shortestRoutes1():
  inputArray = [int(x) for x in input().split()]
  n = inputArray[0]
  m = inputArray[1]

  INF = float('inf')
  adjMat = [[INF for x in range(n)] for y in range(n)]

  for i in range(m):
    inputArray = [int(x) for x in input().split()]
    if adjMat[inputArray[0] - 1][inputArray[1] - 1] > inputArray[2]:
      adjMat[inputArray[0] - 1][inputArray[1] - 1] = inputArray[2]

  distances = [INF for i in range(n)]
  distances[0] = 0
  queue = [0]
  route = [-1 for i in range(n)]

  while len(queue) > 0:
    actual = queue[0]
    for i in range(1, len(queue)):
      if distances[actual] > distances[queue[i]]:
        actual = queue[i]
    queue.remove(actual)

    i = 0
    for edge in adjMat[actual]:
      if edge != INF and edge + distances[actual] < distances[i]:
        distances[i] = edge + distances[actual]
        queue.append(i)
        route[i] = actual

      i += 1

  res = f'{distances[0]}'
  for i in range(1, n):
    res = f'{res} {distances[i]}'
  print(res)

shortestRoutes1()