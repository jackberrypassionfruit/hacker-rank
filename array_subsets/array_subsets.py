def subsetA(arr):
  arr.sort()
  tups = []
  count = 0
  cur = None
  for i, n in enumerate(arr):
    if n is cur:
      count += 1
    else:
      if cur is not None:
        tups.append((cur, count))
      cur = n
      count = 1
  tups.append((cur, count))
  print("tups: ", tups)  
  
  a = []
  maxSum = None
  minCount = None
  
  tot = 0
  for tup in tups:
    tot += tup[0] * tup[1]
  thresh = tot // 2
  print(thresh)
  
  result = None
  Asum = 0
  count = 0
  # iterating over every combination of two subarrays in the array
  for i in range(1, len(tups)): # 1 -> 3 length
    for j in range(len(tups) - i + 1): # 4 -> 2 # of iterations
      print('')
      # print('i: ', i, 'j: ', j)
      a = tups[j:j+i]
      print(a)
      for tup in a:
        count += tup[1]
        Asum += tup[0] * tup[1]
      print('Asum: ', Asum)
      print('count: ', count)
      if Asum > thresh:
        if maxSum is None or Asum >= maxSum:
          if minCount is None or count <= minCount:
            maxSum = Asum
            minCount = count
            result = a
        
      count = 0
      Asum = 0
  return result
  
# arr = [7,7,8,8,8,8,8,9,9,10]
arr = [6,5,3,2,4,1,2]
print(subsetA(arr))