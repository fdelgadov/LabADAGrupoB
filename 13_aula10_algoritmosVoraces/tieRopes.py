# Tie Ropes

def tieRopes(K, A: list):
  """
  Este programa resuele el ejercicio Tie Ropes
  Link: https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/

  Dado una lista de cuerdas A y un entero K, el programa retonar el mayor 
  número de cuerdas de tamaño >= K. Las cuerdas adyacientes pueden unirse 
  en una nueva cuerda.
  """

  # Número de cuerdas >= K
  ropes = 0

  # Se evalúan todas las cuerdas, menos la última
  while len(A) > 1:
    # Se saca la primera cuerda
    actual = A.pop(0)

    # Se compara la longitud de la cuerda con K
    if actual < K:
      # Se une la cuerda sacada con la siguiente; forman una nueva cuerda
      A.insert(0, actual + A.pop(0))
    else:
      # La cuerda es >= K, entonces aumenta el contador
      ropes += 1
  
  # Se evalúa la última cuerda
  if A[0] >= K:
    ropes += 1

  # Retorna la respuesta
  return ropes

A = [1, 2, 3, 4, 1, 1, 3]
print(f'tieRopes: {tieRopes(4, A)}')

A = [1]
print(f'tieRopes: {tieRopes(2, A)}')