"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
n1 = [0,1,0,3,12]


def moveZeroes(nums):
    left = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left],nums[i] = nums[i],nums[left]
            left+=1
    return nums
            
print(moveZeroes(n1))

def bruteforce(nums):
    for i in range(len(nums)-1):
        if nums[i]==0:
            for j in range(i+1,len(nums)):
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    break

#bruteforce(nums)

def method2(nums):
    ans=[0]*len(nums)
    i=0
    for n in nums:
        if n!=0:
            ans[i]=n
            i+=1
            
    for i in range(len(ans)):
        nums[i]=ans[i]
    
#method2(nums)
def moveZeroesBruteForce(nums):
    
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            print('before',i,j,nums[i],nums[j])
            if nums[i] == 0:
                nums[i],nums[j] = nums[j],nums[i]
            print(i,j,nums[i],nums[j])
    print(nums)
        

#print(moveZeroes(n1))