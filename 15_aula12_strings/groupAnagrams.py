# groupAnagrams

def groupAnagrams(strs):
  anagrams = []

  for word in strs:
    add = True
    for ana in anagrams:
      if len(ana[0]) != len(word):
        continue

      group = True
      aux = word
      for ch in ana[0]:
        if ch in aux:
          aux = aux.replace(ch, "", 1)
        else:
          group = False
          break

      if group:
        ana.append(word)
        add = False
        break

    if add:
      anagrams.append([word])
  
  return anagrams

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

strs = [""]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))

strs = ["ddddddddddg","dgggggggggg"]
print(groupAnagrams(strs))