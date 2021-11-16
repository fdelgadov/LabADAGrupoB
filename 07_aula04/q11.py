# Q11: What is the time complexity of
# O(log_2(log_2(n)))

# Algoritmo
# p = 0
# for (i = 1; i < n; i = i * 2) { # O(log_2(n)) -> p = log_2(n)
#     p++;
# }

# for (j = 1; j < p; j = j * 2) { # log_2(p) = log_2(log_2(n))
#     statement;
# }

n = 10
p = 0
i = 1
while i < n: # O(log_2(n)) -> p = log_2(n)
  p += 1
  print(p)
  i = i * 2
print()
j = 1
while j < p: # log_2(p) = log_2(log_2(n))
  print(j)
  j = j * 2