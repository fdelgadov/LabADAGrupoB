# 4. What is the time complexity in terms of O()?
# Para:
# n = haystack.length
# m = needle.length
# O(n*m), porque tenemos un while dentro de un while; es decir, anidado.
def find_needle(needle, haystack):
  # Este algoritmo veirica si un patrón se encuentra en otra cadena.
  # Retorna True si un patrón está en otra cadena.
  # False de lo contrario.

  needle_index = 0
  haystack_index = 0
    
  while haystack_index < len(haystack):
    found_needle = False
    if needle[needle_index] == haystack[haystack_index]:
      found_needle = True
      while needle_index < len(needle):
        if needle[needle_index] != haystack[haystack_index + needle_index]:
          found_needle = False
          break
        needle_index += 1
    if found_needle:
      return True
    needle_index = 0
    haystack_index += 1
  return False

# Test
str1 = "fgh"
str2 = "abcdefghi"
print(f'find_needle({str1}, {str2}): {find_needle(str1, str2)}')

str1 = "franco"
str2 = "francoDelgado"
print(f'find_needle({str1}, {str2}): {find_needle(str1, str2)}')

str1 = "marco"
str2 = "asdawmarCoasd"
print(f'find_needle({str1}, {str2}): {find_needle(str1, str2)}')

str1 = "end"
str2 = "startenxend"
print(f'find_needle({str1}, {str2}): {find_needle(str1, str2)}')

str1 = "end"
str2 = "startenxena"
print(f'find_needle({str1}, {str2}): {find_needle(str1, str2)}')