n = [0,1,0,0,3,0,13]

def moveZeroes(n):
    i = 0
    for j in range(len(n)):
        if n[j] != 0:
            n[i],n[j] = n[j],n[i]
            i+=1
    return n
      
n1 = [0,0,1,1,1,2,2,3,3,4]

def remDups(n):
    
    i = 0
    
    for j in range(1,len(n)):
        if n[i] != n[j]:
            i+=1
            n[i] = n[j]
    print(n,i,n[:i+1])
        
n2 = [-9,-4,-1,0,1,2,3]

def squardSort(n):
    res= [None] * len(n)
    
    l = 0
    r = len(n) -1
    
    while l <= r:
        if abs(n[l]) > abs(n[r]):
            res[r-l] = n[l] ** 2
            l+=1
        else:
            res[r-l] =n[r] ** 2
            r-=1
    return res
        
n3 = [5,2,3,99,4,1,100]

def maxSeqBruteForce(n):
    
    longest = 0
    n_set = set(n)
    
    for i in range(len(n)):
        curr = n[i]
        length = 1
        
        while curr+1 in n_set:
            length+=1
            curr+=1
        print(longest,length)   
        longest = max(longest,length)
    return longest

def maxSeqBruteForce2(n):
    n.sort()
    longest = 1
    length = 1
    n_set= set(n)

    for i in range(1,len(n)):
        
        if n[i] - n[i-1] == 1:
            length+=1
        else:
            longest = max(longest,length)
            length = 1
    longest = max(longest,length)
    
    return longest
            
def maxSeq3(n):
    longest = 1
    n_set = set(n)
    
    for i in range(len(n)):
        if n[i] -1 not in n_set:
            length =1
            
            while n[i]+1 in n_set:
                length+=1
                n[i]+=1
                
            longest= max(longest,length)
    return longest

s ="abcabcbb"
def longSub(s):
    longest = 0
    
    for i in range(len(s)):
        longest = max(longest,helper(i,s))
    return longest

def helper(start,s):
    seen = set()
    
    for j in range(start,len(s)):
        if s[j] not in seen:
            seen.add(s[j])
        else:
            return j - start
    return len(s) - start
            
    
    
def longSubSlidng(s):
    longest = 0
    start = 0
    seen = {}
    for end in range(len(s)):
        if s[end] in seen:
            start = max(start,seen[s[end]]+1)
            
        seen[s[end]] = end
        longest = max(longest,end - start +1)
     
    return longest
    
print(longSubSlidng(s))