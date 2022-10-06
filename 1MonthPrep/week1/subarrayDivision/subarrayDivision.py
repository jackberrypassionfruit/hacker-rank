def birthday(s, d, m):
  count = 0
  for i in range(len(s) - m + 1):
    segment = s[i:i+m]
    print(segment)
    if sum(segment) == d:
      count += 1
  return count
    
  
  
s = [2,2,1,3,2]
e = [4]
print(birthday(e, 4, 1))