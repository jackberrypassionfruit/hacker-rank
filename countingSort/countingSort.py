def sortArr(self, arr, n): 
    freqArr = [0] * (max(arr) + 1)
    sortedArr = []
    for x in arr:
        freqArr[x] += 1
    for i, x in enumerate(freqArr):
        sortedArr = sortedArr + [i] * x
    return sortedArr
  
""" 
1 -> arr = [1, 4, 1, 2, 7, 5, 2]

2 -> freqArr = [0, 0, 0, 0, 0, 0, 0, 0]
    arr = [1, 4, 1, 2, 7, 5, 2]

3 -> sortedArr = []
    freqArr = [0, 0, 0, 0, 0, 0, 0, 0]
    arr = [1, 4, 1, 2, 7, 5, 2]

4 -> sortedArr = []
    arr = [1, 4, 1, 2, 7, 5, 2]
    freqArr = [0, 2, 2, 0, 1, 1, 0, 1]
    
5 -> arr = [1, 4, 1, 2, 7, 5, 2]
    freqArr = [0, 2, 2, 0, 1, 1, 0, 1]
    sortedArr = []

"""