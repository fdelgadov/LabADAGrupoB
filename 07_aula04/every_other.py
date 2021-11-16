# 2. What is the time complexity of this code?
# La comlejidad es O(n^2), porque tiene for anidado.
def every_other(array):
  # Este algoritmo imprime en consola los números del arreglo aumentados en m,
  # tal que m es un número del arrelgo en una posición impar.
  for i in range(len(array)):
    if i % 2 == 0:
      for j in range(len(array)):
        print(array[i] + array[j])
      print()

# Test
a = [2, 6, 3, 7, 4]
every_other(a)
a = [5, 2, 8, 4, 2]
every_other(a)
a = [10, 45, 21, 5, 31]
every_other(a)