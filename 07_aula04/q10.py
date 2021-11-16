# Q10: What is the time complexity of
# n + n = 2n
# O(2n) = O(n)

# Algoritmo
# for (i = 0; i < n; i++) { # n*1=n
#     statement;            # 1
# }

# for (j = 0; j < n; j++) { # n*1=n
#     statement;            # 1
# }
                            # n + n = 2n

n = 10
for i in range(n): # n*1 = n
  print(i)         # 1
print()
for j in range(n): # n*1 = n
  print(j)         # 1
                   # n + n = 2n