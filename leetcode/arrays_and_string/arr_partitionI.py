"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).


"""
n = [1,4,3,2]

def arrayPairSum(nums):
    sortedn = sorted(nums)
    print(sortedn)
    sum = 0
    for i in range(0,len(sortedn),2):
        print(i)
        sum+=sortedn[i]
    return sum

print(arrayPairSum(n))