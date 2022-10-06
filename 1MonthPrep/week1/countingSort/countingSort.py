def countingSort(arr): 
    freqArr = [0] * (max(arr) + 1)
    sortedArr = []
    for x in arr:
        freqArr[x] += 1
    for i, x in enumerate(freqArr):
        sortedArr = sortedArr + [i] * x
    return sortedArr

def countArray(arr):
    freqArr = [0] * 100
    for i in arr:
        freqArr[i] += 1
    print(f'len(freqArr): {len(freqArr)}')
    return freqArr

a = [1,1,3,2,1]
s = "63 54 17 78 43 70 32 97 16 94 74 18 60 61 35 83 13 56 75 52 70 12 24 37 17 0 16 64 34 81 82 24 69 2 30 61 83 37 97 16 70 53 0 61 12 17 97 67 33 30 49 70 11 40 67 94 84 60 35 58 19 81 16 14 68 46 42 81 75 87 13 84 33 34 14 96 7 59 17 98 79 47 71 75 8 27 73 66 64 12 29 35 80 78 80 6 5 24 49 82"

s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
# print(countingSort(a))
# print(len(countArray(a)))
print(countArray(s))

  
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