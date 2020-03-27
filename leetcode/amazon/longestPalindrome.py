from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(s):
            q = deque(list(s))
            
            while len(q) > 1:
                front = q.popleft()
                end = q.pop() if q else ''
                if front != end:
                    return ''
            return s
        
        ans = ''
        maxlength = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print(i,j,s[i:j+1])
                curr_pal = helper(s[i:j+1])
                print(curr_pal,'curr')
                ans = curr_pal if len(ans) < len(curr_pal) else ans
                print(ans,'ans')
        return ans
            
s = Solution()
print(s.longestPalindrome('aba'))