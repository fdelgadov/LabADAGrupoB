# Este programa resuelve el siguiente problema:
# Link: https://www.spoj.com/problems/INTEST/
# Input:
# La entrada comienza con dos números enteros positivos n k (n, k<=10^7). Las siguientes n líneas de
# entrada contienen un entero positivo t, no mayor de 10^9, cada uno

# Output:
# Escriba un solo entero a la salida, denotando cuántos enteros t, son divisibles por k

def exercise01():
  n = int(input("> "))
  k = int(input("> "))
  count = 0
  for i in range(n):
    t = int(input("> "))
    if(t % k == 0):
      count += 1
  print(count)

exercise01()