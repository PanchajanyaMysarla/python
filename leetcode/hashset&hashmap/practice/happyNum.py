def isHappy(n):
    
    seen = set()
    
    while n != 1 and n not in seen:
        print('n',n)
        seen.add(n)
        n = getNext(n)
    return n ==1

def getNext(n):
    total = 0
    while n > 0:
        n,digit = divmod(n,10)
        print(n,digit)
        total+=digit **2
    return total
    
    
    
def isHappyFloyd(n):
    slow = n
    fast = getNext(n)
    
    while fast != 1 and slow != fast:
        slow = getNext(slow)
        fast = getNext(getNext(fast))
    return fast == 1
print(isHappyFloyd(19))