def rotLeft(a, d):
    print('d: ', d)
    rot = d % len(a)
    print('rot: ', rot)
    tmp = a[:rot]
    a = a[rot:] + tmp
    return a
    
    
    
    
# a = [1,2,3,4,5]
# tmp = a[:3]
# a = a[3:]
# a += tmp
# print('a: ', a)

print(rotLeft([1,2,3,4,5], 8))