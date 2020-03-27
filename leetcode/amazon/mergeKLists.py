from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        
        head = point = ListNode(0)
        
        for l in lists:
            if l:
                q.put((l.val,l))
        
        while q:
            val,node = q.get()
            
            point.next = ListNode(val)
            point = point.next
            node =node.next
            if node:
                q.put((node.val,node))
        return head.next
   
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        head = ListNode(0)
        curr = head
        [heapq.heappush(heap,(l.val,i)) for i,l in enumerate(lists) if l]
        while heap:
            pop = heapq.heappop(heap)
            ind = pop[1]
            curr.next = lists[ind]
            curr= curr.next
            if lists[ind].next:
                lists[ind] = lists[ind].next
                heapq.heappush(heap,(lists[ind].val,ind))
        return head.next
    
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        class NodeCompare:
            def __init__(self,node):
                self.node = node
            def __lt__(self,other):
                return self.node.val < other.node.val
        
        head = point = ListNode(0)
        
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put(NodeCompare(l))
        
        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(NodeCompare(node))
            
        return head.next    
            