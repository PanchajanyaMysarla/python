"""
 Find Minimum in Rotated Sorted Array
Solution
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
nums = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
n3= [2,3,4,5,1]

class Solution2(object):
    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high-low)/2
            if nums[mid] > nums[high]:
                low = mid+1
            elif nums[mid] < nums[high]:
                high = mid
        return nums[low]
    
    
class Solution(object):
    def findMin(self, nums):
        if len(nums) ==1:
            return nums[0]
        l = 0
        r = len(nums)-1
        
        if nums[r] > nums[0]:
            return nums[0]
        
        while l <= r:
            mid = l +(r-l) //2
            print(l,mid,r)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l =mid +1
            else:
                r = mid -1
             
s = Solution()
x = s.findMin(n3)
print(x)