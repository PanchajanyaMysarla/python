def split(nums):
    mid = len(nums)//2
    return nums[:mid], nums[mid:]

def helper(left,li,right,ri):
    merged= []
    i = 0
    j = 0
    inversions = 0 +li + ri
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
            inversions+= (len(left)- i)
    merged += left[i:]
    merged += right[j:]
    return merged,inversions
            
    
def countInversions(nums):
    
    if len(nums) == 1:
        return nums,0
    
    left,right =  split(nums)
    
    l,li = countInversions(left)
    r,ri = countInversions(right)
    
    return helper(l,li,r,ri)

def mergeSortInversions(nums):
    if len(nums) ==1 :
        return nums,0
    
    left,right = split(nums)
    
    l,li = mergeSortInversions(left)
    r,ri = mergeSortInversions(right)
    
    i = 0
    j = 0
    c = []
    inversions = 0 + li +ri
    
    while i <len(l) and j < len(r):
        if l[i]<=r[j]:
            c.append(l[i])
            i+=1
        else:
            c.append(r[j])
            j+=1
            inversions+=len(l) -i
    c +=l[i:]
    c +=r[j:]
    return c,inversions
    
n  = [5,4,1,8,7,2,6,3,10]
n2 = [1,2,4,3]
print(countInversions(n))
print(mergeSortInversions(n2))