def matchingStrings(strings, queries):
  results = [0 for num in queries]
  for i, query in enumerate(queries):
    for string in strings:
      if query == string:
        results[i] += 1
  return results
  
s = ['ab', 'ab', 'abc']
q = ['ab', 'bc', 'abc']
print(matchingStrings(s, q))