"""
Intersection of Two Arrays II
Solution
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
import collections

nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]


def intersect( nums1, nums2) :
    
    l = []
    if len(nums1) > len(nums2):
        longer = nums1
        shorter = nums2
    else:
        longer = nums2
        shorter = nums1
        
    
    for i in shorter:
        if i in longer:
            l.append(i)
            longer.remove(i)
    return l   
    
def intersectHashMap(nums1,nums2):
    d = collections.Counter(nums1)
    print(d)
    f = []
    for i in nums2:
        if i in d and d[i] > 0:
            f.append(i)
            d[i]-=1
            
    print(f)    
    
def intersectSorted(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    ans = list()
    i1 = 0
    i2 = 0
    while i1 < len(nums1) and i2 < len(nums2):
        n1 = nums1[i1]
        n2 = nums2[i2]
        if n1 == n2:
            ans.append(n1)
            i1 += 1
            i2 += 1
        elif n1 > n2:
            i2 += 1
        else:
            i1 += 1
            
    return ans
    
print(intersectSorted(nums3,nums4))
    
        