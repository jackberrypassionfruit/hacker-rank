# def activityNotifications(expenditure, d):
#   # if len(expenditure) <= d:
#   #   return 0
  
#   # def myMedian(arr):
#   #   arr.sort()
#   #   mid = len(arr) // 2
#   #   if len(arr) % 2 == 1:
#   #     return arr[mid]
#   #   else:
#   #     return (arr[mid - 1] + arr[mid]) / 2

#   # notifications = 0
  
#   # trailing_days = expenditure[:d]
#   # trailing_days.sort()
#   # print("trailing_days: ",trailing_days)
  
  
      
#   # sorted = expenditure.copy()
#   # sorted.sort()
#   # print('sorted: ', sorted)
#   # print(expenditure)
  
#   # for i in range(d, len(expenditure)):
#   #   median = myMedian(expenditure[i-d : i])
#   #   print('median: ', median, ' | next: ', expenditure[i])
#   #   if median * 2 <= expenditure[i]:
#   #     print('yes')
#   #     notifications += 1

#   return notifications 

# print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)) # output -> 2

"""brain
there are 5 end conditions for the binary search:
  1 - One number, n is smaller
  2 - One number, n is bigger
    these are both easy
  3 - Two numbers, n is smaller
  4 - Two numbers, n is in the middle
  5 - Two numbers, n is bigger
"""
from collections import deque   
import timeit
def arrayBisection(arr, n, insert):
  
    # if type(arr) != deque:
      # arr = deque(arr)
      
    # deq = deque(arr)
    i = 0
    j = len(arr) - 1
    mid = len(arr) // 2
    while arr[mid] != n and j - i > 1:
      mid = (i + j) // 2
      if n > arr[mid]:
        i = mid
      elif n < arr[mid]:
        j = mid
      # print(f'arr[i : j+1]: {arr[i : j+1]} | i: {i} | mid: {mid} | j: {j}')
    if arr[mid] == n:
      if insert:
        arr.insert(mid, n)
      else:
        arr.pop(mid)
    else:
      if insert:
        if n < arr[i]:
          arr.insert(i, n)
        elif n > arr[j]:
          arr.insert(j + 1, n)
        else:
          arr.insert(j, n)
      else:
        if arr[i] == n:
          arr.pop(i)
        elif arr[j] == n:
          arr.pop(j)
          
    return arr

arr = list(range(100000))

arr = deque(arr)
starttime = timeit.default_timer()
print("The start time is :",starttime)
for _ in range(1000):
  arr = arrayBisection(arr, 9, True) 
print("The time difference is :", timeit.default_timer() - starttime)
# print(arr)