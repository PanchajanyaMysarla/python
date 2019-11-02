"""
First Unique Character in a String
Solution
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""
import collections
s = "leetcode"
s2 = "loveleetcode"
def firstUniqChar(s):
    d = {}
    for i in s:
        d.setdefault(i,0)
        d[i]+=1
    print(d)
#     for k,v in d.items():
#         if v ==1:
#             return s.find(k)
#     return -1

    for i,v in enumerate(s):
        if d[v] ==1:
            return i
    return -1

def firstUniqCharCollections(s):
    c = collections.Counter(s)
    print(c)
    for i,v in enumerate(s):
        if c[v] ==1:
            return i
    return -1
    
    
print(firstUniqCharCollections(s2))