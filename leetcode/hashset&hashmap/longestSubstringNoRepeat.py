"""
Longest Substring Without Repeating Characters
Solution
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             """
import collections

a ="abcabcbb"
def lengthOfLongestSubstring(s: str):
    sett = set(s)
    maxSize = 0
    maxi=None
    
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if len(s[i:j]) == len(set(s[i:j])):
                if maxSize < len(s[i:j]):
                    maxSize = len(s[i:j])
                    maxi = s[i:j]
        print(maxSize,maxi)      


def slidingWindow(s):
    i = 0
    j = 0
    
    sett = set()
    maxer = 0
    while i < len(s) and j < len(s):
        if s[j] not in sett:
            sett.add(s[j])
            j+=1
            maxer = max(maxer,j-i)
        else:
            sett.remove(s[i])
            i+=1
    return maxer
        
                            
                
            
print(slidingWindow(a))
        