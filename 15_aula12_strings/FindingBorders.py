# Finding Borders

def findingBorders():
  string = input()
  res = ""
  for i in range(1, len(string)):
    if string[:i] == string[-i:]:
      res = f'{res} {i}'

  print(res.strip())

findingBorders()