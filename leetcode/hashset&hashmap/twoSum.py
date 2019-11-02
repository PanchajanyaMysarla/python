"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
n1 = [2, 7, 11, 15]
target = 9

def twoSum(nums,target):
    compliments = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in compliments:
            return [compliments[comp],i]
        compliments[nums[i]]= i

print(twoSum(n1,9))
        