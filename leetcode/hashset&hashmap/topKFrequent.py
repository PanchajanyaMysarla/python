"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import collections,heapq

n1 = [1,1,1,2,2,3]
n2 = [1,2]
k = 2
def topKFrequent(nums, k):
    c = collections.Counter(nums)
    print(c)
    
    ans = heapq.nlargest(k,c.keys(),key = lambda num: c[num])
    print(ans)
    
#     for k,v in c.items():
#         deque.appendleft(k)
    

print(topKFrequent(n1,k))
        