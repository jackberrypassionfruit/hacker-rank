def twoArrays(k, A, B):
  A.sort()
  B.sort()
  B.reverse()
  print(f'A: {A}, B: {B}')
  for i in range(len(A)):
    if A[i] + B[i] < k:
      return "NO"
  return "YES"
      
    
print(twoArrays(5, [1,2,2,1], [3,3,3,4]))