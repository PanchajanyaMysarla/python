"""
Group Anagrams
Solution
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
import collections

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def groupAnagrams(strs):
    d = {}
    
    for s in strs:
        seq = ''.join(sorted(s))
        #print('seq',seq)
        if seq in d:
            d[seq].append(s)
        else:
            d[seq] = [s]
    return list(d.values())


def groupAnagrams2(strs):
        mapping = collections.defaultdict(list)
        print(mapping)
        for s in strs:
            mapping[tuple(sorted(s))].append(s)
        return mapping.values()

print(groupAnagrams2(strs))