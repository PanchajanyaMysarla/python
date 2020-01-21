"""
Find Peak Element
Solution
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""
nums = [1,2,3,1]
nums2 = [1,2,1,3,5,6,4]

# O(n) time
def findPeakElement1(self, nums):
    i = 0
    while i <= len(nums)-1:
        while i < len(nums)-1 and nums[i] < nums[i+1]:
            i += 1
        return i 

# Recursively
def findPeakElement2(nums):
    return helper(nums, 0, len(nums)-1)

def helper(nums, l, r):
    if l == r:
        return l
    mid = l + (r-l)//2
    if nums[mid] > nums[mid+1]:
        return helper(nums, l, mid)
    else:
        return helper(nums, mid+1, r)

    
def findPeakElement(nums):
    
    l =0
    r = len(nums)
    
    while l < r:
        mid = l +(r-l) //2
        if nums[mid] > nums[mid+1]:
            r =mid
        else:
            l =  mid+1
    return l
        
print(findPeakElement2(nums2))