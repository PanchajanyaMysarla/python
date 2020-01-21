n = [5,2,3,99,4,1,100]

def maxSeqBruteForce(nums):
    
    nums_set = set(nums)
    
    longest_streak = 0
    
    for n in nums:
        curr = n
        current_streak =1
        
        while curr+1 in nums_set:
            current_streak+=1
            curr+=1
        
        longest_streak = max(longest_streak,current_streak)
    
    return longest_streak
 
        
def maxSeqSort(nums):
    nums.sort()
    longest_streak = 1
    current_streak = 1
    
    for n in range(1,len(nums)):
        if nums[n] - nums[n-1] == 1:
            current_streak+=1
        else:
            longest_streak = max(longest_streak,current_streak)
            current_streak = 1
    return max(longest_streak,current_streak)

def maxSeqHashSet(nums):
    nums_set = set(nums)
    longest_streak = 1
    
    for n in nums:
        
        if n -1 not in nums_set:
            curr = n
            curr_streak = 1

            while curr+1 in nums_set:
                curr+=1
                curr_streak+=1
                
            longest_streak = max(longest_streak,curr_streak)
    return longest_streak
print(maxSeqHashSet(n))