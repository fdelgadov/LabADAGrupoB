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

# Algoritmo
# p = 0
# for (i = 1; p <= n; i++) {
#     p = p + i;
# }

p = 0
n = 5
i = 1
while p <= n:
  p = p + i
  print(p)
  i += 1