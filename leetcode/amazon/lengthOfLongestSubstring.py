class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def allUniq(s,start,end):
            hashset = set()
            for i in range(start,end):
                if s[i] in hashset:
                    return False
                else:
                    hashset.add(s[i])
            return True
        
        ans = 0
        
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print(i,j)
                if allUniq(s,i,j):
                    ans = max(ans,j-i)
                    
        return ans
                
        
    def slidingSet(self,s):
        ans = 0
        hashset = set()
        i = 0
        j = 0
        
        while i < len(s) and j < len(s):
            if s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            else:
                hashset.add(s[j])
                j+=1
                ans = max(ans,j-i)
        return ans
    
    def slidingMap(self,s):
        hash = {}
        start =  ans = 0
        for end in range(len(s)):
            if s[end] in hash:
                start = max(start,hash[end]+1)
            hash[s[end]] = end
            ans = max(ans,end-start+1)
              
        return ans
                

a = 'abcdabca'
s= Solution()
print(s.lengthOfLongestSubstring(a))
print(s.sliding(a))