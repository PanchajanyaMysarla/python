import collections

def sqrt_x(n):
    
    root = n//2
    
    for i in range(20):
        root = (1/2) * (root + ( n/root))
        
    return root


#print(sqrt_x(25))
    
    
def gcd(a,b):
    
    while a%b !=0:
        old_a = a
        old_b = b
        
        a = old_b
        b = old_a%old_b
    return b
    
    
#print(gcd(2,5))


def fib(n):
    ans = 0
    for i in range(n+1):
        ans+=i
    return ans

#print(fib(10))



def anagram(a,b):
    
    x = {}
    y  = {}
    
    for i in a:
        x.setdefault(i,0)
        x[i]+=1
    
    for i in b:
        y.setdefault(i,0)
        y[i]+=1
    print(x,y, x == y)

def anagram_sort(a,b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    
    pos =0
    matches = True
    
    while pos < len(a) and matches:
        if a[pos] == b[pos]:
            matches = True
            pos+=1
        else:
            matches = False
            
    print(matches)
#anagram_sort('heart','earth')

def balanced_pars(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) ==0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

#print(balanced_pars('(()'))

def balanced_pars2(s):
    p = {
        ')':'(',
        '}':'{',
        ']':'['
        }
    stack = []
    
    for a in s:
        if a in '{[(':
            stack.append(a)
        elif stack[len(stack)-1] == p[a]:
            stack.pop()
    return len(stack) == 0

#print(balanced_pars2('{[('))
        
def divideBy2(n):
    stack = []
    
    while n > 0:
        stack.append(n%2)
        n = n //2
    return stack[::-1]
#print(divideBy2(42))

def infixToPostfix(s):
    prec= {}
    prec['/'] = 3
    prec['*'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    opStack = []
    postFixList =[]
    for a in s:
        if a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            postFixList.append(a)
        elif a == '(':
            opStack.append(a)
        elif a == ')':
            toptoken = opStack.pop()
            while toptoken != '(':
                postFixList.append(toptoken)
                toptoken = opStack.pop()
        else:
            while len(opStack) !=0 and prec[opStack[len(opStack)-1]] >= prec[a]:
                postFixList.append(opStack.pop())
            opStack.append(a)
    while len(opStack) !=0:
        postFixList.append(opStack.pop())
    return postFixList
    #print(opStack,postFixList)
            
#print(infixToPostfix('A*B+C*D'))

def postFixEval(s):
    res = 0
    stack = []
    
    for a in s:
        if a in '0123456789':
            stack.append(a)
        else:
            x = stack.pop()
            y = stack.pop()
            #res = x a y
            stack.append(res)
            
#print(postFixEval('78+32+/'))


def baseNConvertor(n,base):
    s = ''
    stack = []
    c = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            stack.append(c[n])
        else:
            stack.append(c[n%base])
        n = n // base
    while len(stack) != 0:
        s +=str(stack.pop())
    return s
#print(baseNConvertor(1453,16))


def binarySearch(alist,item):
    low = 0
    high = len(alist) -1
    found = False
    
    while low <= high and not found:
        mid = (low + high) //2
        if alist[mid] == item:
            found = True
        elif item > mid:
            low = mid+1
        else:
            high = mid - 1
    return found
            
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
#print(binarySearch(testlist, 3))
#print(binarySearch(testlist, 13))
    
     
def pivotIndex(nums):
        
    total = sum(nums)
    left = 0
        
    for i in range(len(nums)-1):
        if left == total-left- nums:
            return nums[i]
        left += nums[i]
    return -1

#print(pivotIndex([1,7,3,6,5,6]))



def rotate(nums,k):
    previous = 0
    for i in range(k):
        previous = nums[len(nums)-1]
        for j in range(len(nums)):
            nums[j],previous = previous,nums[j]
    print( nums)
#rotate([1,2,3,4,5,6,7],3)
    
n = [1,1,2]
n2 = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates( nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                i = i+1
                nums[i] = nums[j]
        return i+1
        
#removeDuplicates(n2)
#print(n2)
    
def moveZeroes(nums):
    slow = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[slow],nums[i] = nums[i],nums[slow]
            slow+=1
    return nums   
    
#print(moveZeroes([0,1,0,3,12]))



def twoSum(nums, target):
    hash = {}
    for x in range(len(nums)):
        diff = abs(target - nums[x])
        
        if nums[x] in hash:
            return [hash[nums[x]],x]
        hash[diff] = x
                
#print(twoSum([2, 7, 11, 15], 9,))

def firstUniqChar(s: str):
    
    c = collections.Counter(s)
    
    for i in s:
        if i in c and c[i] == 1:
            return i
            
    
    
#print(firstUniqChar('loveleetcode'))
    
def helper(start,s):
    seen = set()
    for i in range(start,len(s)):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            return i- start
    return len(s) - start

def lengthOfLongestSubstring(s):
    
    maxer = 0

    for i in range(len(s)):
        maxer = max(maxer,helper(i,s))
    
    return maxer   
print(lengthOfLongestSubstring('abcabcbb'))

