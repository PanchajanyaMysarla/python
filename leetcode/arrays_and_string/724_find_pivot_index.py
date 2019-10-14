def pivotIndex(nums) -> int:
    if len(nums) <= 0: return -1
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:len(nums)]):
            return i
    return -1
    
def pivot_index2(nums) -> int:
    leftsum = 0
    
    if len(nums) <= 0: return -1
    
    total_sum = sum(nums)

    for i in range(len(nums)):
        
        right = total_sum - leftsum - nums[i]
        
        if leftsum == right:
            return i
        leftsum+=nums[i]
        
    return -1

def pivot_index3(nums) -> int:
    leftsum = 0

    if len(nums) <= 0: return -1
    
    total_sum = sum(nums)

    for i,el in enumerate(nums):
        
        right = total_sum - leftsum - el
        
        if leftsum == right:
            return i
        leftsum+=nums[i]
        
    return -1
        
#print(pivotIndex([1, 7, 3, 6, 5, 6]))
            
#print(pivot_index2([1, 7, 3, 6, 5, 6]))

print(pivot_index3([1, 7, 3, 6, 5, 6]))