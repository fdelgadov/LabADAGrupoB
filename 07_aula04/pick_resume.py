# 5. What is the time complexity in terms of O()?
# n = tamaño del arreglo
# 0   n
# 1   n/2
# 2   n/4
# ...
# k   n/(2^k)
# Termina cuando: n/(2^k) <= 1
# n/(2^k) = 1
# n = 2^k
# log_2(n) = k
# O(log_2(n)), porque en cada iteración el valor de n se reduce a la mitad.
# resumes is an array
def pick_resume(resumes):
  # Este algoritmo elije un elemento del arreglo eliminando alternativante la
  # primera y la segunda mitad del arreglo hasta que queda el elemento elegido
  # Retorna el elemento que no fue eliminidado; es decir, el elegido
  eliminate = "top"
  length = len(resumes)

  while length > 1:
    if eliminate == "top":
      resumes = resumes[int(length / 2):]
      eliminate = "bottom"
    elif eliminate == "bottom":
      resumes = resumes[:int(length / 2)]
      eliminate = "top"
    length = len(resumes)
  return resumes[0]

# Test
a = [3, 7, 1, 2, 5, 8, 4, 9]
print(f'a: {a}\npick_resume(a): {pick_resume(a)}')
a = [3, 7, 1, 2]
print(f'a: {a}\npick_resume(a): {pick_resume(a)}')
a = [3, 7, 8, 4, 9]
print(f'a: {a}\npick_resume(a): {pick_resume(a)}')
a = [3, 8, 4, 9]
print(f'a: {a}\npick_resume(a): {pick_resume(a)}')