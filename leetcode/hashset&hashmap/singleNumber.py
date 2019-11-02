"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
n1 = [2,2,1]
n2= [4,1,2,1,2]

def singleNumber(nums):
    
    hashMap = {}
    
    for i in nums:
        hashMap.setdefault(i,0)
        hashMap[i]+=1
    
    print(hashMap)
    for k,v in hashMap.items():
        if v ==1:
            return k
        
def singleNumberList(nums):
    non_dups = []
    
    for i in nums:
        if i not in non_dups:
            non_dups.append(i)
        else:
            non_dups.remove(i)
    return non_dups.pop()

def singleNumberHashTable(nums):
    hashMap =  {}
    for i in nums:
        try:
            hashMap.pop(i)
        except:
            hashMap[i]=1
    return hashMap.popitem()[0]


def singleNumberMath(nums):
    
    return 2 * sum(set(nums)) - sum(nums)

def singleNumberBitManipulation(nums):
    
    a = 0
    for i in nums:
        a^=i
        print(a)
    return a
    
print(singleNumberBitManipulation(n2))