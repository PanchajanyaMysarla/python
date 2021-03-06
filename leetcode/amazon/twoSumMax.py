"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
"""


def findSum(nums, target):
    target -= 30
    map = {}
    maximum = -1
    ans = [-1,-1]
    for i in range(len(nums)):
        if nums[i] not in map:
            map[target - nums[i]] = i
        else:
            if nums[i] > maximum or target - nums[i] > maximum:
                ans[0] = map[nums[i]]
                ans[1] = i
                maximum = max(nums[i],target - nums[i])
    if ans != [-1,-1]:
        return ans
    else:
        return []

# [20, 50, 40, 25, 30, 10],90 | [1, 5]
# [1, 10, 25, 35, 60], 90 | [2, 3]
# [50, 20, 10, 40, 25, 30], 90 | [0, 2]
print (findSum([50, 20, 10, 40, 25, 30], 90))
