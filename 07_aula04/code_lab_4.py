# 1. Convert from O(n^2) to O(n)
def greatestNumber(array):
  # Este algoritmo retorna el mayor número de un arreglo
  for i in array:
    isIValTheGreatest = True
    for j in array:
      if j > i:
        isIValTheGreatest = False
      if isIValTheGreatest:
        return i

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

# 3. What is the time complexity in terms of O()
# Su complejidad es O(n^2), porque tiene for anidado.
def twoSum(array):
  # Este algoritmo retorna verdadero si existen dos números diferentes cuya
  # suma es 10
  for i in array:
    for j in array:
      if(i != j and i + j == 10):
        return True

# 4. What is the time complexity in terms of O()?
# Para:
# n = haystack.length
# m = needle.length
# O(n*m), porque tenemos un while dentro de un while; es decir, anidado.
def find_needle(needle, haystack)
    needle_index = 0
    haystack_index = 0
    
    while haystack_index < haystack.length
        if needle[needle_index] == haystack[haystack_index]
            found_needle = true
            while needle_index < needle.length
                if needle[needle_index] != haystack[haystack_index + needle_index]
                    found_needle = false
                break
            end
            needle_index += 1
            end
        return true if found_needle
        needle_index = 0
        end
        haystack_index += 1
    end
    return false
end

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
    eliminate = "top"
    
    while resumes.length > 1:
        if eliminate == "top":
            resumes = resumes[resumes.length / 2, resumes.length - 1]
            eliminate = "bottom"
        elif eliminate == "bottom":
            resumes = resumes[0, resumes.length / 2]
            eliminate = "top"
        end
    end
    return resumes[0]
end

a = [4, 1, 7, 3, 12]
print(a)
every_other(a)
print(a)
print(twoSum(a))