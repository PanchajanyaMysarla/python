import collections

a = [-9,-4,-1,0,1,2,3]


def sqrdSorted(n):
    res = collections.deque()
    l = 0
    r = len(n) - 1
    
    while l < r:
        left,right = abs(n[l]) , abs(n[r])
        print(left,right)
        
        if left > right:
            res.appendleft(left**2)
            l+=1
        else:
            res.appendleft(right**2)
            r-=1
    print(res)

def sqrdSorted2(n):
    res = []
    l = 0
    r = len(n) - 1
    
    while l <= r:
        left,right = abs(n[l]) , abs(n[r])
        print(left,right)
        
        if left > right:
            res.append(left**2)
            l+=1
        else:
            res.append(right**2)
            r-=1
    print(res)
    

def sqrdSorted3(n):
    res = [None] * len(n)
    l = 0
    r = len(n) - 1
    
    while l <= r:
        left,right = abs(n[l]) , abs(n[r])
        print(left,right)
        
        if left > right:
            res[r-l] = left**2
            l+=1
        else:
            res[r-l] = right**2
            r-=1
    print(res)
print(sqrdSorted3(a))