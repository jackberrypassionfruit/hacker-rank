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
    
order = 
[1, 2, 5, 3, 7, 8, 6, 4]

[1, 2, 3, 5, 7, 8, 6, 4]
[1, 2, 3, 5, 7, 6, 8, 4]
[1, 2, 3, 5, 6, 7, 8, 4]
[1, 2, 3, 5, 6, 7, 4, 8]
[1, 2, 3, 5, 6, 4, 7, 8]
[1, 2, 3, 5, 4, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
