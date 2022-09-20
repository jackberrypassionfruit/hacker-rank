def dynamicArray(n, queries):
    # Write your code here
    ans = []
    lastAnswer = 0
    arr = []
    for i in range(n):
        arr.append([])
    
    
    for query in queries:
        x = query[1]
        y = query[2]
        idx = (x ^ lastAnswer) % n
        if query[0] == 1:
            # do 1
            arr[idx].append(y)
        elif query[0] == 2:
            # do 2
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)
        else:
            print(f"mistakes where made here: {query}")
            
    return ans

print(dynamicArray(2, [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]))