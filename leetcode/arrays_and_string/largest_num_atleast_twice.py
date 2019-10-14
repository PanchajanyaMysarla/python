nums1 = [1, 2, 3, 4]
nums2 = [3, 6, 1, 0]
def dominantIndex(nums) -> int:

    twice_sum = [x*2 for x in nums]
    
    print(twice_sum)
    for i in range(len(nums)):
        check = twice_sum[:i] + twice_sum[i+1:]
        print(check,i)
        
        if nums[i] >= max(check):
            return i
    return -1
            
print(dominantIndex(nums2))