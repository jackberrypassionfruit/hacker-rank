def balancedSums(arr):
  i = len(arr) // 2
  left = sum(arr[:i])
  right = sum(arr[i+1:])
  print(f'left: {left}, right: {right}')
  if left < right:
    while left < right:
      left += arr[i]
      i += 1
      right -= arr[i] 
      print(f'left: {left}, right: {right}')
      if left == right:
        return "YES"
      elif i == len(arr):
        if sum(arr[:len(arr) -1]) == 0:
          return "YES"
        else:
          return "NO"
    
  elif left > right:
    while left > right:
      right += arr[i] 
      i -= 1
      left -= arr[i]
      if left == right:
        return "YES"
      elif i == 0:
        if sum(arr[1:]) == 0:
          return "YES"
        else:
          return "NO"
  elif left == right:
    return "YES"
  return "NO"

a = [4,1,1,3,6]
print(balancedSums(a)) 