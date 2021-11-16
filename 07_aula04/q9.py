# Q9: What is the time complexity of
# i = 0^2, 1^2, 2^2, 3^3, ..., k^2
# El bucle termina para i >= n
# k^2 = n
# k = n^(1/2)
# O(n^(1/2))

# Algoritmo
# for (i = 0; i * i < n; i++) {
#     statement;
# }

n = 10
i = 0
while i * i < n:
  print(i*i)
  i += 1