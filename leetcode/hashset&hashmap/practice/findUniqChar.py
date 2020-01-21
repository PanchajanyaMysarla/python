# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.

s = "leetcode"
s1 = "loveleetcode"

import collections

def firstUniqChar(s):
    c = collections.Counter(s)
    print(c)
    
    for idx,v in enumerate(s):
        if v in c and c[v] ==1:
            return idx
                       
print(firstUniqChar(s1))