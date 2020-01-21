nums = [2, 7, 11, 15]
target = 9



def twoSum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in seen:
            return [seen[comp], i]
        else:
            seen[nums[i]] = i
            
    
print(twoSum(nums,target))