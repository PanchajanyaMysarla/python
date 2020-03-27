"""
Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

a= 'race a car'
b = 'A man, a plan, a canal: Panama'

# from collections import deque
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         
#         a = deque([x.lower() for x in s if x.isalnum()])
#         
#         print(a)
#         
#         while len(a) > 1:
#             if a.pop() != a.popleft():
#                 return False
#         return True
#                 
#             
#         

class Solution:
    
    
    def isPalindrome(self, s):
        x = [i for i in s if i.isalnum()]
        print(x)
        l = 0
        r = len(x)-1
        while l < r:  
            if x[l].lower() != x[r].lower():
                return False
            l+=1
            r-=1
        return True
        
s = Solution()
print(s.isPalindrome(b))
      