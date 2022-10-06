def miniMaxSum(arr):
  res = sum(arr)
  
  min = res - arr[0]
  max = res - arr[-1]
  return min, max
  
a = [1,2,3,4,5]
print(miniMaxSum(a))