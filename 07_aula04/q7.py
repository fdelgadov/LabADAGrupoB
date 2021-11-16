# Q7: What is the time complexity of
# i = 1, 2, 4, 8, 16, ..., 2^k
# El bucle termina para: i >= n
# 2^k = n
# k = log_2(n)
# O(log_2(n))

# Algoritmo
# for (i = 1; i < n; i = i*2) {
#     statement;
# }

i = 1
n = 10
while i < n:
  print(i)
  i = i*2