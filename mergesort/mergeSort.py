def mergeSort(arr):
  # Divide
  # Conquer
  # Combine
  
  
  if len(arr) > 1:
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    
    mergeSort(L)
    mergeSort(R)
    
    i = 0
    j = 0
    k = 0
    
    print("arrBefore: ", arr)
  
    while i < len(L) and j < len(R):
      if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
      elif L[i] > R[j]:
        arr[k] = R[j]
        j += 1
      k += 1
      
    print("arrAfter: ", arr)
    
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
    


arr = [4,3,5,1,73,5,2,2,1,4,6]
mergeSort(arr)
print(arr)