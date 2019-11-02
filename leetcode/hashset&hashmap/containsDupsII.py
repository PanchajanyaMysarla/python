"""
Contains Duplicate II
Solution
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
nums = [1,2,3,1]
k = 3

nums2 = [1,0,1,1]
k2 = 1

nums3 = [1,2,3,1,2,3,1]
k3 = 2


"""
brute force: O(n) * O(k) = O(nk) time
    for i=0 to n:
        for j=i+1 to i+1+k
            if nums[i] == nums[j]: return True
    return False
    
    
     # one pass
        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = [i]
            elif i - d[nums[i]][-1] <= k:
                return True
            else:
                d[nums[i]].append(i)
                
        return False
            
"""
def containsNearByDuplicateHash(nums,k):
    d ={}
    
#     for i in range(len(nums)):
#         if nums[i] in d:
#             if i - d[nums[i]] > k:
#                 d[nums[i]] = i
#                 continue
#             else:
#                 return True
#         else:
#             d[nums[i]] = i
        
    e ={}
    
    for i in range(len(nums)):
        if nums[i] in e and i - e[nums[i]] <= k:
            return True
        e[nums[i]] = i
    return False



def containsNearbyDuplicate( nums, k):
    
    for i in range(len(nums)):
        print('i',i)
        try :
            temp = nums[i+1:].index(nums[i])
        except:
            continue
        j = temp +i+1
        print('j',j)
        if j != -1 and  j-i  <= k:
            return True
    return False
print(containsNearByDuplicateHash(nums3,k3))
        