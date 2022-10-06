def findZigZagSequence(a, n):
    a.sort()
    reversed = a[(n//2):]
    reversed.reverse()
    res = a[:(n//2)] + reversed
    for num in res:
        print(num, end=" ")
    
    # asc = []
    # desc = []
    # while a:
    #     if a:
    #         asc.append(a.pop(0))
    #     if a:
    #         desc.insert(0, a.pop(0))
    # # print(f"asc: {asc}, desc: {desc}")
    # print(asc + desc)
            


findZigZagSequence([1,2,3,4,5,6,7], 7)
