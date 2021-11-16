# 3. What is the time complexity in terms of O()
# Su complejidad es O(n^2), porque tiene for anidado.
def twoSum(array):
  # Este algoritmo retorna verdadero si existen dos números diferentes cuya
  # suma es 10
  for i in array:
    for j in array:
      if(i != j and i + j == 10):
        return True
  
  return False

a = [2, 6, 3, 8, 1]
print(twoSum(a))
a = [5, 2, 5, 8, 1]
print(twoSum(a))
a = [3, 6, 5, 14, 8]
print(twoSum(a))