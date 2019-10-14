"""
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
"""

nums = [3,2,2,3]
val = 3

def removeElement(nums, val):
    final =[]
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k+=1
    return k
            
    
print(removeElement(nums,val))