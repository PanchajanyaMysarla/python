"""

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""
import collections

nums1 = [1,2,2,1]
nums2 = [2,2]

def intersect(nums1, nums2):
    res = []
    if len(nums1) > len(nums2):
        l = nums1
        s = nums2
    else:
        l = nums2
        s = nums1
    a = collections.Counter(l)
    print(a)
    
    for i in nums2:
        if i in a and a[i] > 0:
            res.append(i)
            a[i]-=1
    print(res)
    
def intersectColl(n1,n2):
    a = collections.Counter(n1)
    b = collections.Counter(n2)
    print(a,b, list((a&b).elements()))
    
print(intersectColl(nums1,nums2))