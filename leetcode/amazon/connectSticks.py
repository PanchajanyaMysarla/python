from collections import deque
import heapq

class Solution(object):
    def connectSticks(self, sticks):

        # Binary search insert function
        def insert(l,item):
            start=0
            end = len(l)-1
            while start<=end:
                mid = (start+end)//2
                if item > l[mid]:
                    start=mid+1
                else:
                    end=mid-1
            l.insert(start,item)

        if sticks==[]:
            return 0
        sticks.sort()
        result = 0
        while len(sticks)>1:
            s0=sticks.pop(0)
            s1=sticks.pop(0)
            result+=s0+s1
            insert(sticks,s0+s1)
        return result

    def connectSticksHeaping(self,sticks):
        heapq.heapify(sticks)
        total = 0
        while len(sticks) > 1:
            s = heapq.heappop(sticks) + heapq.heappop(sticks)
            total+=s
            heapq.heappush(sticks,s)
        return total

    def connectSticksHeap(self,sticks):
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) >= 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            ans+=a+b
            heapq.heappush(sticks,a+b)
        return ans
