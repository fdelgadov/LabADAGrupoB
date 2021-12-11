# Tie Ropes

def tieRopes(K, A: list):
  ropes = 0

  while len(A) > 1:
    actual = A.pop(0)
    if actual < K:
      A.insert(0, actual + A.pop(0))
    else:
      ropes += 1
  
  if A[0] >= K:
    ropes += 1

  return ropes

A = [1, 2, 3, 4, 1, 1, 3]
print(f'tieRopes: {tieRopes(4, A)}')

A = [1]
print(f'tieRopes: {tieRopes(2, A)}')