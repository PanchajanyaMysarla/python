"""
 Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

s = "egg"
t = "add"

s1 = "paper"
t1 = "title"

s2 = "ab"
t2 = "aa"

def isIsomorphic(s, t):
    
    i = [ s.index(i) for i in s]
    j = [t.index(j) for j in t]
    print(i,j)
   
def isIsomorphicZip(s,t):
    
    d = {}
    for i, j in zip(s,t):
        if i not in d:
            if j in d.values():
                return False
            d[i]= j
        elif d[i] != j:
            return False
    return True
    
print(isIsomorphicZip(s2,t2))