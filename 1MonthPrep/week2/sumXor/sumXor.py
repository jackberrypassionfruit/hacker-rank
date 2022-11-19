import math

def sumXor(n):
  if n == 0:
    return 1
  pow2 = int(math.log(n, 2))
  bin = ''
  wiggle = 0
  while pow2 >= 0:
    # print(f'n: {n}, pow2: {pow2}')
    if n >= 2**pow2:
      bin += '1'
      n -= 2**pow2
    else:
      bin += '0'
      wiggle += 1
    pow2 -= 1
  
  combos = 2 ** wiggle
  return combos
  
  
# print(sumXor(11))