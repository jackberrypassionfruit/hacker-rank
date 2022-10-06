def minimumSwaps(arr):
  count = 0
  for i in range(len(arr) - 1):
    max_index = 0
    for j in range(1, len(arr) - i):
      # current_max = max(arr[max_index], arr[j])
      if arr[j] > arr[max_index]:
        max_index = j
    if arr[max_index] != arr[len(arr) - i - 1]:
      count += 1
      arr[max_index], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[max_index]
      
  # return arr
  return count
      
    
  
# ---------
print(minimumSwaps([4, 3, 1, 2]))
# 2 3 1 _4
# 2 1 _3 4
# 1 _2 3 4

# -------
# [2, 3, 4, 1, 5]

# ---------
# [1, 3, 5, 2, 4, 6, 7]