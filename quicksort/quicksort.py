def sort(arr, lo, hi):
  if lo < hi:
    pivot = arr[hi]
    big = None
    for i in range(lo, hi):
      if big is None and arr[i] > pivot:
        big = i
      ## swap arr[i] with arr[big] if we find a smaller num
      elif big is not None and arr[i] < pivot:
        print(big)
        arr[big], arr[i] = arr[i], arr[big]
        big += 1
    if big is not None:
      arr[hi], arr[big] = arr[big], arr[hi]
    else:
      big = 0
    
    print(arr[lo:big])
    sort(arr, lo, big)
    sort(arr, big, hi)

def quickSort(arr):
  sort(arr, 0, len(arr) - 1)
  
arr = [8, 7, 6, 1, 0 ,9 ,2]
quickSort(arr)
print(arr)