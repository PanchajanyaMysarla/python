"""
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""
nums= [1,1,0,1,1,1,0]
n2 = [1,0,1,1,0,1]

def findMaxConsecutiveOnes(nums):
    maxOnes = 0
    k = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            k+=1
            if maxOnes < k:
                maxOnes = k
            
        else:
            k = 0
        
    return maxOnes
    
def findMaxConsecutiveOnes2(nums):
    max_ones, k = 0, 0
    for i in nums:
        if i == 1:
            k+=1
        else:
            max_ones = max(k,max_ones)
            k= 0
    
    return max(max_ones,k)

print(findMaxConsecutiveOnes2(n2))