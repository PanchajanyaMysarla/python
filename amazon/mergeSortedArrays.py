"""
88. Merge Sorted Array
Easy

1360

3182

Favorite

Share
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

n3 = [2,0]
n4 = [1]



def mergeSortedArrays(nums1,m,nums2,n):
    
    a = len(nums1) -1
    b = len(nums2) -1
    m = m-1
    n = n-1

    while nums2:
        if m >= 0 and nums1[m] > nums2[n]:
            nums1[a] = nums1[m]
            m-=1
        else:
            nums1[a] = nums2.pop()
            n-=1
        a-=1
  
    print(nums1)          
                   
mergeSortedArrays(n3,1,n4,1)