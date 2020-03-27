class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = collections.defaultdict(list)
        
        for s in range(len(strs)):
            hash[tuple(sorted(strs[s]))].append(strs[s])
        
        return hash.values()
        
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c)-ord('a')]+=1
            
            ans[tuple(count)].append(s)
        return ans.values()
                

            
            
        
