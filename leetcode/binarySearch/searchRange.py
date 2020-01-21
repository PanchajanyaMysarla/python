"""
Search for a Range
Solution
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

nums = [5,7,7,8,8,10]
target = 8

nums2 = [5,7,7,8,8,10]
target2 = 6

class Solution(object):
    def searchRangeLinear(self,nums,target):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] == target:
                return [i,i+1]
        return [-1,-1]
    
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) -1
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return [mid,l]
            elif nums[mid] > target:
                r = mid
            else:
                l = mid
        return [-1,-1]
        
s = Solution()
x = s.searchRange(nums,target)
y = s.searchRangeLinear(nums2,target2)
print(y)