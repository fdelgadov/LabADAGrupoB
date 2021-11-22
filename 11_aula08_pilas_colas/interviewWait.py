from collections import deque

def interviewWait(arr):
  # Este programa simula la cola de espera para una entrevista.
  # Las personas son atendidades de modo que el siguiente será alguno de los
  # que están más a la izquierda o derecha. Además, el que será atentido es
  # el que menor tiempo de entrevistar tomará de ambos.
  # Usted será entrevistado y está denotado por '-1'.
  # El programa retorna el tiempo transcurrido hasta que sea su turno.

  queue = deque(arr)
  wait = 0

  for i in range(len(queue)):
    if queue[0] == -1 or queue[-1] == -1:
      return wait
    if queue[0] < queue[-1]:
      wait += queue.popleft()
    else:
      wait += queue.pop()

# Test
arr = [4, -1, 5, 2 , 3]
print(f'{arr}\n{interviewWait(arr)}')

arr = [5, 2, 8, 4, 3, -1, 7, 9, 11, 6]
print(f'{arr}\n{interviewWait(arr)}')

arr = [-1, 4, 2, 7]
print(f'{arr}\n{interviewWait(arr)}')