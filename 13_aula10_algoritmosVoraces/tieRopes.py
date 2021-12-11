# Tie Ropes

def tieRopes(K, A: list):
  """
  Este programa resuele el ejercicio Tie Ropes
  Link: https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/

  Dado una lista de cuerdas A y un entero K, el programa retonar el mayor 
  número de cuerdas de tamaño >= K. Las cuerdas adyacientes pueden unirse 
  en una nueva cuerda.

  Solucion:
  El objetivo es hallar el mayor número de cuerdas >= K, teniendo en cuenta que
  es posible unir cuerdas adyacentes. Para ello, es suficiente con sacar y unir
  las cuerdas con tamaño < K según el orden en el que estan dispuestas en la
  lista A, ya que solo pueden ser unidas si son adyacentes. Cada vez que es
  sacada una cuerda >= K, es contada para el total de la respuesta final.
  """
  # Numero de cuerdas
  length = len(A)

  # Número de cuerdas >= K
  ropes = 0

  #Tamaño de cuerda atada
  tiedRope = 0 # Cuerda atada vacía

  # Se evalúan todas las cuerdas, menos la última
  for i in range(length):
    # Se une a cuerda atada
    tiedRope += A[i]

    # Se compara la longitud de la cuerda atada con K
    if tiedRope >= K:
      ropes += 1
      tiedRope = 0
  
  # Retorna la respuesta
  return ropes

A = [1, 2, 3, 4, 1, 1, 3]
print(f'tieRopes: {tieRopes(4, A)}')

A = [1]
print(f'tieRopes: {tieRopes(2, A)}')