# Q4: What is the time complexity of
# O(n^2), porque tiene for anidado

# Algoritmo
# for (i = 0; i < n; i++) {       # n*n = n^2 = O(n^2)
#     for (j = 0; j < n; j++) {   # n*1 = n
#         statement;              # 1
#     }
# }

n = 5
for i in range(n):     # n*n = n^2 = O(n^2)
  for j in range(n):   # n*1 = n
    print(f'{i}, {j}') # 1