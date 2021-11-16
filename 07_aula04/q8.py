# Q8: What is the time complexity of
# i = n, n/(2^1), n/(2^2), n/(2^3), ..., n/(2^k)
# El bucle termina para i < 1
# n/(2^k) = 1
# n = 2^k
# log_2(n) = k
# O(log_2(n))

# Algoritmo
# for (i = n; i >= 1; i = i/2) {
#     statement;
# }

n = 10
i = n
while i >= 1:
  print(i)
  i = i / 2