def salesByMatch(ar):
  socks = {}
  count = 0
  for sock in ar:
      if sock not in socks:
        socks[sock] = 1
      else:
        socks[sock] += 1
        
  for sock in socks:
    count += socks[sock] // 2
        
  for sock in socks:
    socks[sock] = socks[sock] // 2
    
  return count
          
print(salesByMatch([1,2,1,2,1,3,2]))