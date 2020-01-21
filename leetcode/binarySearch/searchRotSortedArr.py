"""
Search in Rotated Sorted Array
Solution
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""



nums = [4,5,6,7,0,1,2]
target = 0

def search(nums, target):
    
    l = 0
    h = len(nums) - 1
    
    while l <= h:
        mid =  l+(h-l)//2
        print(l,mid,h,nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[l] <= target < nums[mid] or target < nums[mid] < nums[l] or nums[mid] < nums[l] <= target:
            h = mid -1
        else:
            l = mid + 1
    return -1
    

def search2(nums,target):
    low =0
    high = len(nums) -1
    
    while low <=high:
        mid = low+(high-low) //2
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low]<= target < nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid +1
            else:
                high = mid -1
    return -1
                
print(search2(nums,0))