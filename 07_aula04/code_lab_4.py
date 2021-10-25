# Convert from O(n^2) to O(n)
def greatestNumber(array):
  for i in array:
    isIValTheGreatest = True
    for j in array:
      if j > i:
        isIValTheGreatest = False
      if isIValTheGreatest:
        return i

# What is the time complexity of this code?
def every_other(array):
  for i in range(len(array)):
    if i % 2 == 0:
      for j in range(len(array)):
        print(array[i] + array[j])
      print()

# What is the time complexity in terms of O()
def twoSum(array):
  for i in array:
    for j in array:
      if(i != j and i + j == 10):
        return True

a = [4, 1, 7, 3, 12]
print(every_other(a))
print(twoSum(a))