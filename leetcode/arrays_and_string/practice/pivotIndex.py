nums = [1, 7, 3, 6, 5, 6]



def pivotIndex(nums):
    total_sum = sum(nums)
    left = 0
    for i in range(len(nums)):
        if left == total_sum - left - nums[i]:
            return nums[i]
        else:
            left+=nums[i]
    
print(pivotIndex(nums))