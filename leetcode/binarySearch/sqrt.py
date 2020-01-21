"""
Sqrt(x)
Solution
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
   
   """

"""
class Solution(object):
    def mySqrt(self, x):
       
        if x == 1 or x == 0:
            return x

        left = 1
        right = x // 2
        
        while left <= right:
            pivot = left + (right -left) // 2
            num = pivot **2
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right
        """

def mySqrt(x):
    if x == 1: return x
    l = 0
    r = x
    while l <= r: 
        pivot = l +(r-l) // 2
        print(l,r,pivot,pivot**2)
        if pivot ** 2 <= x < (pivot+1) * (pivot+1):
            return pivot
        elif pivot**2 < x:
            l =pivot+1
        else:
            print('r')
            r = pivot-1
     
    
print('ans',mySqrt(2))