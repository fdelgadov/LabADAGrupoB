from collections import deque

def backspace(str: str):
  # Este programa interpreta metacaracteres de una cadena ingresada para poder
  # borrar caracteres ingresados por error por medio de un teclado especial
  # El teclado solo acepta letras minúsculas y el metacaracter
  # Metacaracteres
  # # -> Borra la última letra ingresada
  
  queue = deque([])
  
  for ch in str:
    if ch == '#':
      queue.pop()
    else:
      queue.append(ch)

  res = ""
  for i in range(len(queue)):
    res += queue.popleft()
  
  return res

# Test
str = "abc#de##f#ghi#jklmn#op#"
print(f'{str}\n{backspace(str)}')

str = "franasd###codl#elgadod#niw###vol##an#e#lencia"
print(f'{str}\n{backspace(str)}')

str = "loren#mipso#um"
print(f'{str}\n{backspace(str)}')