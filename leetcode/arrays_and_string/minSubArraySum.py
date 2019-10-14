"""
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

"""
s = 7
nums = [2,3,1,2,4,3]
def minSubArrayLen(s, nums):
    ans = 0
    left =0
    summ = 0
    
    for i in range(len(nums)):
        summ+=nums[i]
        while summ >= s:
            ans = min(ans,i+1-left)
            left+=1
            summ-=nums[left]
    return ans


print(minSubArrayLen(s,nums))
            
    