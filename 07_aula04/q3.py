# Q3: What is the time complexity of
# i = 0, 2, 4, 6, ...
# O(n)

# Algoritmo
# for (i = 0; i < n; i=i+2) { # n/2*1 = n/2 = O(n)
#     statement;              # 1
# }

n = 5
for i in range(0, n, 2): # n/2*1 = n/2 = O(n)
  print(i);              # 1