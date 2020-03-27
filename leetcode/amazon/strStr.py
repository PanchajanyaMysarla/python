class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1
    def strStr2(self, haystack: str, needle: str) -> int:
        L,n = len(needle),len(haystack)
        pn = 0
        
        while pn < n - L + 1:
            
            while pn <n-L+1 and haystack[pn] != needle[0]:
                pn+=1
            
            
            curr_len, pL = 0,0
            
            while pn < n and pL < L and haystack[pn] == needle[pL]:
                pL+=1
                curr_len+=1
                pn+=1
                
            if curr_len == len(needle):
                return pn-L
        
            pn = pn - curr_len + 1
        return -1
            
        
a = 'hello'
b = 'll'


s = Solution()
print(s.strStr('',''))