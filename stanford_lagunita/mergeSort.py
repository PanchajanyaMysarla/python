
n  = [5,4,1,8,7,2,6,3,10]

def mergeSort(nums):
    
    if len(nums) <= 1:
        return nums
    
    left,right = split(nums)
    print(left,right,'mergeSort')
    
    return merge_helper(mergeSort(left),mergeSort(right))

def split(nums):
    mid = len(nums)//2
    return nums[:mid],nums[mid:]
    

def merge_helper(left,right):
    
    print(left,right,'mergehelper')
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    i = 0
    j = 0
    
    merged = []
    
    total = len(left)+ len(right)
    
    while len(merged) < total:
        if left[i] > right[j]:
            merged.append(right[j])
            j+=1
        else:
            merged.append(left[i])
            i+=1
        
        if i == len(left):
            merged+=right[j:]
            break
        if j == len(right):
            merged+=left[i:]
            break
        
    return merged
            
    
print(mergeSort(n))  
    
    