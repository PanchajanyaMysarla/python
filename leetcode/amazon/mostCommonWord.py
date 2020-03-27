import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if not paragraph:
            return
        
        ans = ''
        l = re.split('\W',paragraph)
        l = [i.lower() for i in l if i]
        c = Counter(l)
        banned = set(banned)
        sortedwords = sorted(c,key= lambda x: (-c[x],x))
        if not banned:
            return sortedwords[0]
        
        for word in sortedwords:
            if word not in banned:
                ans = word
                break
        return ans
                