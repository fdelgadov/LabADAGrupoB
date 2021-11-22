from collections import deque

def capsLock(str: str):
  # Este programa interpreta metaracteres de una cadena para escribir mayúsculas
  # en un teclado simulado que solo permite letras minúsculas
  # Metacaracteres:
  # @ -> Alterna entre minúscula y mayúscula los caracteres del buffer
  # $ -> Vacea el buffer

  buffer = deque([])
  res = ""
  upper = False

  for i in str:
    if i == '$':
      aux = ""
      while len(buffer) > 0:
        aux += buffer.popleft()
      if upper:
        res += aux.upper()
      else:
        res += aux
    elif i == '@':
      upper = not upper
    else:
      buffer.append(i)
  
  return res

# Test
str = "abc$d@ef$@g$"
print(f'{str}\n{capsLock(str)}')

str = "@f$@ranco $@d$@el@gado @$v@$@alencia$@tonto"
print(f'{str}\n{capsLock(str)}')