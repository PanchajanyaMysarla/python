"""
692. Top K Frequent Words
Medium

1357

116

Add to List

Share
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
    """

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        print(c)
        print(sorted(c,key=lambda x:(-c[x],x)))
        
        
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        memo = collections.defaultdict(int)
        for word in words:
            memo[word] -= 1
            
        heap = []
        for word, negCnt in memo.items():
            heapq.heappush(heap, (negCnt, word))
            
        res = []
        for i in range(k):
            top = heapq.heappop(heap)
            res.append(top[1])
            
        return res
        
        