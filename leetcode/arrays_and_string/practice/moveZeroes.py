n1 = [0,1,0,3,12]

def moveZeroes(nums):
    lastNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[lastNonZero] = nums[lastNonZero],nums[i]
            lastNonZero+=1
    return nums
    
print(moveZeroes(n1))