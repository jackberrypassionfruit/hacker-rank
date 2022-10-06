def checkMagazine(magazine, note):
  magazine = magazine.split()
  note = note.split()
  
  hash_table = {}
  for word in magazine:
    if word in hash_table:
      hash_table[word] += 1
    else:
      hash_table[word] = 1
  
  # print(hash_table)
  
  for word in note:
    if word in magazine and hash_table[word] > 0:
      hash_table[word] -= 1
    else:
      print('No')
      return
  print("Yes")
  
checkMagazine("two times three is not four", "two times two is four")