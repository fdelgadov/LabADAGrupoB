# Number of longest increasing subsequence

def lengthOfLIS(nums):
  """
  Este programa resuelve el siguiente ejercicio: Longest Increasing Subsequence
  Link: https://leetcode.com/problems/longest-increasing-subsequence/

  Este programa retorna el tamaño de la subsecuencia ascendente de mayor tamaño
  Una subsecuencia de un arreglo A es un arreglo formado por algunos elementos
  de A sin alterar el orden.
  """
  LISArr = [nums[-1]]
  for num in nums[-2::-1]:
    update = False

    i = len(LISArr)
    for LIS in LISArr[::-1]:
      if num < LIS:
        length = i + 1
        if len(LISArr) < length:
          LISArr.append(num)
        elif num > LISArr[length - 1]:
          LISArr[length - 1] = num
        update = True
        break
      i -= 1

    if not update:
      if LISArr[0] < num:
        LISArr[0] = num

  return len(LISArr)

# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f'{nums}\n{lengthOfLIS(nums)}')

nums = [0,1,0,3,2,3]
print(f'{nums}\n{lengthOfLIS(nums)}')

nums = [7,7,7,7,7,7,7]
print(f'{nums}\n{lengthOfLIS(nums)}')