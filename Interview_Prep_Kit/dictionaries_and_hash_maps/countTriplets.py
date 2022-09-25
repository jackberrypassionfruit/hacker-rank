"""Improvement Ideas
  
  Take advantage of repeated numbers and dictionaries to do math instead of more iterations
  ex. when I have two 2's in arr, I know that I'll have two different chances to make that triplet sum
"""

def countTriplets(arr, r):
  triplets = 0

  num_dict = {}
  for i in arr:
      num_dict[i] = 0
  for i in arr:
      num_dict[i] += 1

  arr = list(set(arr))
  arr.sort()
  print("arr: ", arr)
  for i in range(len(arr) - 2):
    j = i + 1
    k = i + 2
    while k < len(arr):
      first_ratio = arr[j] / arr[i]
      second_ratio = arr[k] / arr[j]
      # print(f'i: {i} | j: {j} | k: {k} | first_ratio: {first_ratio} | second_ratio: {second_ratio}')
      if first_ratio < second_ratio:
        j += 1
      elif first_ratio > second_ratio:
        k += 1
      else: 
        if first_ratio == r and second_ratio == r:
          triplets += (num_dict[arr[i]] * num_dict[arr[j]] * num_dict[arr[k]])
          # print('good')
        j += 1
      
      if j >= k:
          j -= 1
          k += 1
  return triplets
          
          
print(countTriplets([1, 3, 9, 9, 27, 81], 3)) 