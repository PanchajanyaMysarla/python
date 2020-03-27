import heapq

class Solution:
    def mergeKSortedArrays(self,lists):
        q = []
        
        for l in lists:
            for i in l:
                heapq.heappush(q,i)
        
        print(q)
    def mergeKArrays
        
lists =[ [5,6,7],[1,2,3], [9,7,8]]
s= Solution()
s.mergeKSortedArrays(lists)
        
        
        