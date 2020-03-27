from collections import deque;

class Solution:
    def firstNonRepeatChar(self,s):
        seen = set()
        ans = ''
        q = deque()
        for i in s:
            if i not in seen:
                seen.add(i)
                if i not in q:
                    q.append(i)
            else:
                if i in q:
                    q.remove(i)
            print('else',q,seen)

        return q.popleft()
                
        
s = Solution()
print(s.firstNonRepeatChar('geeksofrgeeks'))