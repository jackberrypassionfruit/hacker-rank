def makeAnagram(a, b):
  char_dictA = {}
  char_dictB = {}
  for char_index in range(97,123):
    char_dictA[chr(char_index)] = 0
    char_dictB[chr(char_index)] = 0

  for char in a:
    char_dictA[char] += 1

  for char in b:
    char_dictB[char] += 1  

  deletions = 0

  for key in char_dictA.keys():
    deletions += (char_dictB[key] - char_dictA[key]) * (char_dictB[key] > char_dictA[key])
  # print(char_dictA.keys())

  print('deletions: ', deletions)

makeAnagram('fart', 'jump')

# letter97 = chr(97)
# letter122 = chr(122)