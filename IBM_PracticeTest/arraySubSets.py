def arraySubsets(arr):
  arr.sort()
  
  i = len(arr) - 1
  j = i - 1
  while 
  

[2, 3, 5, 6, 7]
          j  i
        
6 7 -> 10 < 13
5 7 -> 11 < 12 ***
5 6 -> 12 > 11


[5,3,2,4,1,2]
[1,2,2,3,4,5]
         i j
4 5 -> 8 < 9 ***
3 5 -> 9 > 8


[4,2,5,1,6]
[1,2,4,5,6]
       i j
       
5 6 -> 7 < 11
4 6 -> 8 < 10 ***
4 5 -> 9 == 9 


