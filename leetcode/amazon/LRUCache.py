from collections import OrderedDict

class LRUCache(OrderedDict):
    
    def __init__(self,capacity):
        self.capacity = capacity
    
    def get(self,key):
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1
    
    def put(self,key,value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
         
class DLinkedNode():
    def __init__(self):
        self.val =0
        self.key =0
        self.prev= None
        self.next =None
            
class LRUCache2():
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = self.tail = DLinkedNode()
        self.head.next =self.tail
        self.tail.prev = self.head
        
    def _add_node(self,node):
        
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_node(node)
    def _poptail(self):
        
        res = self.tail.prev
        self._remove_node(res)
        return res
    def get(self,key):
        node = self.cache.get(key,None)
        if node:
            self._move_to_head(node)
            return node.val
        return -1
    def put(self,key,value):
        
        node = self.cache.get(key,None)
        
        if node:
            self.cache[key] = value
            self._move_to_head(node)
    
        