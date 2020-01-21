n  = [5,4,1,8,7,2,6,3,9,10]

def ithSmallestNum(nums):
    
    return helper(nums,0,len(nums)-1)

def helper(n,start,end):
    
    if start < end:
        p = partition(n,start,end)
        helper(n,start,p-1)
        helper(n,p+1,end)
    
def partition(n,start,end):
    pivot = n[start]
    left = start +1
    right = end
    done = False
    
    while not done:
        while left<=right and n[left]<=pivot:
            left+=1
        while left<=right and n[right]>= pivot:
            right-=1
        if left > right:
            done = True
        else:
            n[left],n[right] = n[right],n[left]
    
    n[start],n[right] = n[right],n[start]
    
    return right
    

ithSmallestNum(n)
print(n)