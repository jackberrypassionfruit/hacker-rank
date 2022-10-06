def nums():
  i = 0
  j = 1
  
  while j < 10:
    k = i+j
    yield k
    
    i = j
    j = k  
    
for n in nums():
  print(n)