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

# Test
a = [4, 1, 7, 3, 12]
print(a)
every_other(a)
print(a)
print(twoSum(a))

## Review of Time Complexity
## Q1: What is the time complexity of
## O(n), es un for de i=0 hasta i=n
for (i = 0; i < n; i++) {   # n*1 = n = O(n)
    statement;              # 1
}

## Q2: What is the time complexity of
## O(n), porque es un for de i=n hasta i=1
for (i = n; i > 0; i--) { # n
    statement;            # 1
}

## Q3: What is the time complexity of
# i = 0, 2, 4, 6, ...
# O(n)
for (i = 0; i < n; i=i+2) { # n/2*1 = n/2 = O(n)
    statement;              # 1
}

# Q4: What is the time complexity of
# O(n^2), porque tiene for anidado
for (i = 0; i < n; i++) {       # n*n = n^2 = O(n^2)
    for (j = 0; j < n; j++) {   # n*1 = n
        statement;              # 1
    }
}

# Q5: What is the time complexity of
# i   j                           iteraciones
# 0   -                             0
# 1   0                             1
# 2   0, 1                          2
# 3   0, 1, 2                       3
# ...
# n   0, ..., (n - 2), (n - 1)      n
#
# 0 + 1 + 2 + 3 + ... + n = n*(n + 1) / 2
# = O(n^2)
for (i = 0; i < n; i++) {
    for (j = 0; j < i; j++) {
        statement;
    }
}

# Q6: What is the time complexity of
# i   p
# -   0
# 1   0 + 1
# 2   0 + 1 + 2
# 3   0 + 1 + 2 + 3
# k   0 + 1 + 2 + ... + k = k * (k+1) / 2
# El bucle termina cuando: p > n
# k*(k+1)/2 > n
# k^2 > n
# k > n^(1/2)
# O(n^(1/2))
p = 0
for (i = 1; p <= n; i++) {
    p = p + i;
}

# Q7: What is the time complexity of
# i = 1, 2, 4, 8, 16, ..., 2^k
# El bucle termina para: i >= n
# 2^k = n
# k = log_2(n)
# O(log_2(n))
for (i = 1; i < n; i = i*2) {
    statement;
}

# Q8: What is the time complexity of
# i = n, n/(2^1), n/(2^2), n/(2^3), ..., n/(2^k)
# El bucle termina para i < 1
# n/(2^k) = 1
# n = 2^k
# log_2(n) = k
# O(log_2(n))
for (i = n; i >= 1; i = i/2) {
    statement;
}

# Q9: What is the time complexity of
# i = 0^2, 1^2, 2^2, 3^3, ..., k^2
# El bucle termina para i >= n
# k^2 = n
# k = n^(1/2)
# O(n^(1/2))
for (i = 0; i * i < n; i++) {
    statement;
}

# Q10: What is the time complexity of
# n + n = 2n
# O(2n) = O(n)
for (i = 0; i < n; i++) { # n*1=n
    statement;            # 1
}

for (j = 0; j < n; j++) { # n*1=n
    statement;            # 1
}
                          # n + n = 2n

# Q11: What is the time complexity of
# O(log_2(log_2(n)))
p = 0
for (i = 1; i < n; i = i * 2) { # O(log_2(n))
    p++;                        # p = log_2(n)
}

for (j = 1; j < p; j = j * 2) { # log_2(p) = log_2(log_2(n))
    statement;
}

# Q12: What is the time complexity of
# O(n*log(n))
for (i = 0; i < n; i++) {           # n*log_2(n) = O(n*log(n))
    for (j = 1; j < n; j = j * 2) { # log_2(n)*1
        statement;                  # 1
    }
}