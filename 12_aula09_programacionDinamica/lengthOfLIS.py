# Number of longest increasing subsequence

def lengthOfLIS(nums):
  LISArr = [[1, nums[-1]]]
  for num in nums[-2::-1]:
    update = False

    for LIS in LISArr[::-1]:
      if num < LIS[1]:
        length = LIS[0] + 1
        if len(LISArr) < length:
          LISArr.append([length, num])
        elif num > LISArr[length - 1][1]:
          LISArr[length - 1][0] = length
          LISArr[length - 1][1] = num
        update = True
        break

    if not update:
      if LISArr[0][1] < num:
        LISArr[0][1] = num

  return LISArr[-1][0]
      
    


# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f'{nums}\n{lengthOfLIS(nums)}')

nums = [0,1,0,3,2,3]
print(f'{nums}\n{lengthOfLIS(nums)}')

nums = [7,7,7,7,7,7,7]
print(f'{nums}\n{lengthOfLIS(nums)}')