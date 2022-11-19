import math

def counterGame(n):
    # Write your code here
    turns = 0
    while n > 1:
      turns += 1
      log2_result = math.log(n, 2)
      print(f'n: {n}, log2_result: {log2_result}')
      if log2_result % 1 == 0:
        n /= 2
      else:
        next_lowest_power_of_2 = int(log2_result)
        n -= 2**next_lowest_power_of_2
    if turns % 2 == 0:
      return "Richard"
    else:
      return "Louise"

print(counterGame(390024124134132343))