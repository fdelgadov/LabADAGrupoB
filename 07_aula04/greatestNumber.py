# Este algoritmo retorna el mayor número de un arreglo
# Fue implemetando para que sea O(n)
def greatestNumber(array):
  greatestNumber = array[0]
  for i in array[1:]:
    if(i > greatestNumber):
      greatestNumber = i

  return greatestNumber

# Test
a = [43, 81, 21, 42, 13, 25]
print(greatestNumber(a))
a = [24, 6, 19, 67, 24, 8]
print(greatestNumber(a))
a = [31, 36, 94, 2, 76]
print(greatestNumber(a))
a = [6, 87, 35, 1, 785]
print(greatestNumber(a))