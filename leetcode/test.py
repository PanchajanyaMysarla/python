a = [1,2,3,4,5]
s = 'hello world'

def rev(s):
    stack = []  
    revStr = ''
    l = list(s)
    while l:
        p = l.pop()
        stack.append(p)
        revStr+=p   
    return stack,revStr
    
print(rev('hello'))

def revLoop(a):
    f = []
    g = []
    for i in range(len(a)):
        f.append(a[len(a)-i-1])
     
    for i in range(len(s)):
        g.append(s[len(s)-i-1])
    
    
def revTwoPointer(a):
    l =0
    r =len(a)-1   
    while l <r:
        a[l],a[r] = a[r],a[l]
        l+=1
        r-=1
    print(a)

nums =  [0,1,0,3,12]

def moveZeroes(n):
    
    zero = 0
    non_zero = 0
    
    for i in range(len(n)):
        if n[i] != 0:
            n[non_zero], n[i] = n[i],n[non_zero]
            non_zero+=1
            print(n)
    return n
    
#print(moveZeroes(nums))

def remDups(n):
    
    i = 0
    for j in range(1,len(n)):
        if n[i] != n[j]:
            i+=1
            n[i]= n[j]
        print(n,i)
    print('aftr',n[:1+1],i)   
    
n2 = [1,1,2]
n3 = [0,0,1,1,1,2,2,3,3,4]

#print(remDups(n3))