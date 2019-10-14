"""
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

a= ["h","e","l","l","o"]

l = 0
r = len(a) - 1

while l < r:
    a[l], a[r] = a[r], a[l]
#     temp = a[l]
#     a[l] = a[r]
#     a[r] = temp
    
    l+=1
    r-=1
   
    
print(a)



"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        for i in range(int(l/2)):
            s[i], s[l-i-1] = s[l-i-1], s[i]

"""


