def diagonalDifference(arr):
  lr_diag = 0
  rl_diag = 0
  
  for i, row in enumerate(arr):
      lr_diag += arr[i][i]
      rl_diag += arr[i][len(arr) - 1 - i]
      
  return abs(lr_diag- rl_diag)
       
# a = [[1,2,3], [4,5,6], [9,8,9]]
a = [[11,2,4], [4,5,6], [10,8,-12]]
print(diagonalDifference(a))