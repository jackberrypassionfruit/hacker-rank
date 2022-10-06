def lonelyinteger(a):
  a.sort()
  for i in range(0, len(a) -1, 2):
    if a[i] != a[i + 1]:
      return a[i]
  return a[-1]


arr = [1,2,3,4,3,2,1]
print(lonelyinteger(arr))