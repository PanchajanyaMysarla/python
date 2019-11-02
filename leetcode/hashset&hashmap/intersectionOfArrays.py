"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
"""

n1 = [1,2,2,1]
n2 = [2,2]

n3 = [4,9,5]
n4 = [9,4,9,8,4]

def intersection( nums1, nums2):
    return list(set(nums1) & set(nums2))

def intersect(nums1,nums2):
    
    n1 = set(nums1)
    n2 = set(nums2)
    
    if len(n1) > len(n2):
        shorter = n2
        longer = n1
        #return [i for i in n1 if i in n2]
    else:
        shorter = n1
        longer =n2
        #return [i for i in n2 if i in n1]
    result =[]
    hashTable = {}
    for i in shorter:
        hashTable[i] =1
    for j in longer:
        if j in hashTable and hashTable[j] ==1:
            result.append(j)
    return result
            
        
print(intersect(n3,n4))