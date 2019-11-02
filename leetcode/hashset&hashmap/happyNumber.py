"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

n1 = 19


"""
class Solution:
    def isHappy(self, n: int) -> bool:
        occr = set()
        while n != 1:
            n = sum(map(lambda x: x**2, [int(i) for i in str(n)]))
            if n in occr:
                return False
            occr.add(n)
        
        return True
"""

def isHappy(n: int):
    hashSet = set()
    while n != 1:
        if n in hashSet:
            return False
        hashSet.add(n)
        n = helper(n)
        print(n)
    return True
    

def helper(n):
    sumOfSquares = 0
    for digit in str(n):
        sumOfSquares += int(digit) ** 2
    return sumOfSquares
        
print(isHappy(19))
        