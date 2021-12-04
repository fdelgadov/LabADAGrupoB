def rectangleCutting():
  inputArray = [int(x) for x in input().split()]

  # Rectángulo
  a = inputArray[0]
  b = inputArray[1]

  print(recRectCutting(a, b))

def recRectCutting(a, b):
  print(f'{a} {b}')
  res = 0
  if a == b:
    return res

  if a < b:
    aux = a
    a = b
    b = aux

  n = mcd(a, b)
  a = a / n
  b = b / n
  
  if a - b == 1:
    if a == 2:
      return 1
    elif a % 2 != 0:
      res = 1 + recRectCutting(a // 2, b) + recRectCutting((a // 2) + 1, b)
    else:
      res = 1 + recRectCutting(b // 2, a) + recRectCutting((b // 2) + 1, a)
  else:
    m = a - b
    n = b
    res = 1 + recRectCutting(m, n)

  return res

def mcd(a, b):
  if b == 0:
    return a
  else:
    return mcd(b, a % b)

# Test
rectangleCutting()