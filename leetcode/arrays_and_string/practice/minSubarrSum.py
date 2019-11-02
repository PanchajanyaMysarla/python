s, nums = 4, [2,3,1,2,4,3]
n2=[1,4,4]
n3 = [1,1]


def minSub(nums,s):
    left = 0
    total = 0
    ans = float('inf')
    for i in range(len(nums)):
        total+=nums[i]
        while total >= s:
            ans = min(ans,i+1-left)
            left+=1
            total-=nums[left]
    return ans
            
    
def minSubArr(nums,s):
    if len(nums) == 0: return 0
    if sum(nums) < s: return 0
    minSubArr = []
    count = float('inf')
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            print(i,j,nums[i:j+1],sum(nums[i:j+1]))
            subset = nums[i:j+1]
            
            if sum(subset) >= s:
                print(i,j,subset,sum(subset))
                if count > len(subset):
                    count = len(subset)
                    minSubArr = subset
                    print(count,minSubArr)
                
       
    return count
#print('minSubArr',minSubArr(n3,3))
print('minSub',minSubArr(nums,7))