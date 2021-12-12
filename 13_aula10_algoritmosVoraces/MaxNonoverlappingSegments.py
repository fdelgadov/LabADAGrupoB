# MaxNonoverlappingSegments

def solution(A, B):
  """
  Este algoritmo resuelve el problema MaxNonoverlappingSegments:
  Link: https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/

  Este programa retorna el número máximo de segmentos no superpuestos. Los 
  segmentos están denotados por las listas A y B, donde A contiene el punto 
  origen de cada segmento y B contiene el puno final de cada segmento.

  Solución:
  Deben contarse los segmentos de modo que cada segmeneto no contenga más de un segmento superpuesto.
  De lo contrario dicho segmento evitará que se cuenten 2 o más segmentos. Una vez seleccionado un 
  segemento para contar, si hubiese un segmento superpuesto, debe ser eliminado de la lista, porque
  el problema no permite que sea tomado en cuenta.
  """
  N = len(A)
  maxSegments = 0
  segments = [x for x in range(N)]
  deletes = 0

  for i in segments:
    overlapping = 0

    for j in segments[i + 1 - deletes:]:
      if A[j] <= B[i] and overlapping < 2:
        overlapping += 1
      else:
        break

    print(f'{i} {overlapping}')
    if overlapping == 0:
      maxSegments += 1
    elif overlapping == 1:
      maxSegments += 1
      segments.remove(i + 1)
      deletes += 1

  return maxSegments

# main
A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]
print(f'solution: {solution(A, B)}')

A = [1, 3, 4, 5]
B = [5, 3, 4, 5]
print(f'solution: {solution(A, B)}')

A = [1, 4, 5, 1]
B = [2, 4, 5, 6]
print(f'solution: {solution(A, B)}')

A = [1, 2, 5, 1]
B = [2, 2, 5, 6]
print(f'solution: {solution(A, B)}')

A = [2, 1, 5, 1]
B = [2, 2, 5, 6]
print(f'solution: {solution(A, B)}')