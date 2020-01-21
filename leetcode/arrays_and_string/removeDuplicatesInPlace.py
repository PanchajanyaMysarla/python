"""
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""


nums = [0,0,1,1,1,2,2,3,3,4]
n2=[1,1,2]

def removeDupsInPlace(nums):
    c=1
    for i in range(1,len(nums)):
        if nums[i-1]!=nums[i]:
            nums[c]=nums[i]
            c+=1
    print(nums)
    return c
            

def countUniq(nums):
    count = 0
    seen = None
    for i in nums:
        if i != seen:
            seen = i
            count+=1
           
    return count

print(removeDupsInPlace(n2))