n  = [5,4,1,8,7,2,6,3,9,10]

def quickSort(nums):
    return helper(nums,0,len(nums)-1)

def helper(nums,start,end):
    if start < end:
        pp =  partition(nums,start,end)
        
        helper(nums,start,pp-1)
        helper(nums,pp+1,end)
           
def partition(nums,start,end):
    
    pivot = nums[start]
    
    left = start+1
    right = end
    done =False
    
    while not done:
        
        while left <= right and nums[left] <= pivot:
            left+=1
        while right >=left and nums[right] >= pivot:
            right-=1
        
        if left > right:
            done = True
        else:
            nums[left],nums[right] = nums[right],nums[left]
    
    nums[start],nums[right] = nums[right],nums[start]
    
    return right
    
quickSort(n)
print(n)
    
    
    
    