"""
Top K Frequent Elements
Solution
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import collections

nums = [1,1,1,2,2,3]
k = 2

def topKFrequent(nums, k):
    c = collections.Counter(nums)
    print(c)
    
    s =sorted(c.items(),key = lambda x : x[1],reverse=True)
    print(s)
    res = []
    for i in range(k):
        res.append(s[i][0])
        
    print(res)
    
print(topKFrequent(nums,k))