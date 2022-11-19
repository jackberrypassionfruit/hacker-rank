def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i in range(len(q) - 1):
        diff = q[i] - q[i+1]
        if diff > 2:
            print("Too chaotic")
            return
        elif diff > 0:
            bribes += diff
    print(bribes)
    
    """self_demo
[1, 2, 5, 3, 7, 8, 6, 4]    3-5
      +2 -1 +2 +2 -1 -4
      
[1, 2, 3, 5, 7, 8, 6, 4]    6-8
         +1 +2 +2 -1 -4
         
[1, 2, 3, 5, 7, 6, 8, 4]    6-7
         +1 +2    +1 -4
         
[1, 2, 3, 5, 6, 7, 8, 4]    4-8
         +1 +1 +1 +1 -4
         
[1, 2, 3, 5, 6, 7, 4, 8]    4-7
         +1 +1 +1 -3
         
[1, 2, 3, 5, 6, 4, 7, 8]    4-6
         +1 +1 -2 
         
[1, 2, 3, 5, 4, 6, 7, 8]    4-5
         +1 -1
         
[1, 2, 3, 4, 5, 6, 7, 8] 
    """

arr = [1,2,5,3,7,8,6,4]
minimumBribes(arr)