# Convert from O(n^2) to O(n)
def greatestNumber(array):
  # Este algoritmo retorna el mayor número de un arreglo
  for i in array:
    isIValTheGreatest = True
    for j in array:
      if j > i:
        isIValTheGreatest = False
      if isIValTheGreatest:
        return i

# What is the time complexity of this code?
# La comlejidad es O(n^2)
def every_other(array):
  # Este algoritmo imprime en consola los números del arreglo aumentados en m,
  # tal que m es un número del arrelgo en una posición impar.
  for i in range(len(array)):
    if i % 2 == 0:
      for j in range(len(array)):
        print(array[i] + array[j])
      print()

# What is the time complexity in terms of O()
# Su complejidad es O(n^2)
def twoSum(array):
  # Este algoritmo retorna verdadero si existen dos números diferentes cuya
  # suma es 10
  for i in array:
    for j in array:
      if(i != j and i + j == 10):
        return True

a = [4, 1, 7, 3, 12]
print(a)
every_other(a)
print(a)
print(twoSum(a))