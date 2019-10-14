"""
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

nums = [2,7,11,15]
target = 9

def twoSumBruteForce(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i+1,j+1]

#print(twoSumBruteForce(nums))
            
def twoSumTwoPointer(nums):
    r = 0
    l = len(nums) -1
    
    while r < l:
        if nums[r] + nums[l] == target:
            return [r+1,l+1]
        elif nums[r] + nums[l] > target:
            l-=1
        else:
            r+=1
    
#print(twoSumTwoPointer(nums))
            
def twoSum( numbers, target: int):
        search = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] not in search:
                search[numbers[i]] = i
            else:
                return [search[target-numbers[i]]+1,i+1]
            
print(twoSum(nums,target))          
