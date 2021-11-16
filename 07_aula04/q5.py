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

# Algoritmo
# for (i = 0; i < n; i++) {
#     for (j = 0; j < i; j++) {
#         statement;
#     }
# }

n = 5
for i in range(n):
  for j in range(i):
    print(f'{i}, {j}')