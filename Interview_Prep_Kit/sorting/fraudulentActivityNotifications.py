def activityNotifications(expenditure, d):
  if len(expenditure) <= d:
    return 0
  
  def myMedian(arr):
    arr.sort()
    mid = len(arr) // 2
    if len(arr) % 2 == 1:
      return arr[mid]
    else:
      return (arr[mid - 1] + arr[mid]) / 2

  notifications = 0
  
  trailing_days = expenditure[:d]
  trailing_days.sort()
  print("trailing_days: ",trailing_days)
  
  
      
  # sorted = expenditure.copy()
  # sorted.sort()
  # print('sorted: ', sorted)
  # print(expenditure)
  
  # for i in range(d, len(expenditure)):
  #   median = myMedian(expenditure[i-d : i])
  #   print('median: ', median, ' | next: ', expenditure[i])
  #   if median * 2 <= expenditure[i]:
  #     print('yes')
  #     notifications += 1

  return notifications 

# print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)) # output -> 2
    
def arrayBisection(arr, n, insert):
    i = 0
    j = len(arr)
    mid = len(arr) // 2
    while arr[mid] != n and j > i:
      print(f'arr[i : j+1]: {arr[i : j+1]} | i: {i} | mid: {mid} | j: {j}')
      mid = len(arr) // 2
      if n > arr[mid]:
        i = mid
      elif n < arr[mid]:
        j = mid
    ## either found n in array, or down to last value    
    if arr[mid] == n:
      if insert:
        arr.insert(mid, n)
      else:
        arr.pop(mid)
    else:
      if insert:
        arr.insert(mid + (arr[mid] < n), n)
        # if arr[mid] > n:
        #   arr.insert(mid, n)
        # else:
        #   arr.insert(mid + 1, n)
        


# a = ['a', 'b','c','d']
# a.insert(2, 'fart')

# a = 3
# b = (a is 3) + 5

arr = [1,2,4]
arr.sort()
arrayBisection(arr, 3, True)