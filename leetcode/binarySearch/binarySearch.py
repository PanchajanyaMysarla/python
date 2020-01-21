"""
Binary Search
Solution
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

"""
nums = [-1,0,3,5,9,12]
target = 9

def search(nums, target):
    l = 0
    r = len(nums) -1
    
    while l < r:
        mid = (l + r) // 2
        print(mid,nums[mid])
        if nums[mid] == target:
            return mid, nums[mid] 
        elif nums[mid] < target:
            l = mid
        else:
            r = mid
def search2(nums,target):
    l = 0
    r = len(nums) -1
    while l <= r:
        pivot = l + (r -l) //2
        print(pivot,nums[pivot])
        if nums[pivot] == target:
            return pivot
        elif target > nums[pivot]:
            l = pivot + 1
        else:
            r = pivot -1
            
print(search2(nums,target))
    
    