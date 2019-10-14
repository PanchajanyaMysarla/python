"""
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
nums=[1,2,3,4,5,6,7]
k = 3


def rotateArrSlicing(nums,k):
    left = nums[:k+1]
    right = nums[k+1:]
    return right+left


def rotateArrInPlace(nums,k):
    
    for i in range(k):
        previous =  nums[len(nums)-1]
        
        for j in range(len(nums)):
            previous, nums[j] =  nums[j],previous
            
            
        print(i,nums)
        
        
def rotateArrReverse(nums,k):
    reverseArr(nums,0,len(nums)-1)
    reverseArr(nums,0,k-1)
    reverseArr(nums,k,len(nums)-1)
    
def reverseArr(nums,start,end):
    while start < end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1
    
def rotateArrNewArr(nums,k):
    final = [None] * len(nums)
    for i in range(len(nums)):
        index = (i + k) % len(nums)
        final[index] = nums[i]
    return final

def rotateSlicing(nums, k):

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
        

print(rotateSlicing(nums,k))
