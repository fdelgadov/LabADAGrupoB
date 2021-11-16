# Q12: What is the time complexity of
# O(n*log(n))

# Algoritmo
# for (i = 0; i < n; i++) {           # n*log_2(n) = O(n*log(n))
#     for (j = 1; j < n; j = j * 2) { # log_2(n)*1
#         statement;                  # 1
#     }
# }

n = 5
for i in range(n):      # n*log_2(n) = O(n*log(n))
  j = 1
  while j < n:          # log_2(n)*1
    print(f'{i}, {j}')  # 1
    j = j * 2