"""
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:

k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.


Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
"""
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]


k2 = 2
keywords2 = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews2 = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

from collections import Counter
import heapq
from functools import cmp_to_key

class Solution:
    
    
    
    def freq(self,k,keywords,reviews):
      
        ans = []
        keywords = set(keywords)
        count = Counter()

        for review in reviews:
            seen = set()
            strs = review.split(' ')
            for s in strs:
                s = s.lower()
                if s in keywords and s not in seen:
                    count[s]+=1
            
        print(count)
                    
        #print(sorted(count,key = lambda x: (-count[x],x)))
        
        heap = [(key,value) for key,value in count.items()]
        
        print('nsmallest',heapq.nsmallest(k,heap))
        print(heap)



s = Solution()
print(s.freq(k2,keywords2,reviews2))