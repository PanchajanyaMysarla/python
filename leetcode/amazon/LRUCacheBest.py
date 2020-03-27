class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None
        self.prev = None
    def __str__(self):
        return "Key : {}, Value: {}".format(self.key,self.value)
        
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insert_after_head(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_tail(self):
        node = self.tail.prev
        self.remove(node)
        return node.key
    
    def move_to_head(self,node):
        self.remove(node)
        self.insert_after_head(node)
    
        

class LRUCache():
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.dll = DLL()
    
    def get(self,key):
        
        if key not in self.cache:
            print('get',-1)
            return -1
        self.dll.move_to_head(self.cache[key])
        print('get',self.cache[key].value)
        return self.cache[key].value
       
    
    def put(self,key,value):
        node = self.cache.get(key)

        if not node:
            newNode = Node()
            newNode.key = key
            newNode.value = value
    
            self.cache[key] = newNode
            self.dll.insert_after_head(newNode)
            
            if len(self.cache) > self.capacity:
                removedkey = self.dll.remove_tail()
                del self.cache[removedkey]
        else:        
            node.value = value
            self.dll.move_to_head(node)        
            self.cache[key] = node
        print(self.cache[key])

cache = LRUCache(2)
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)
cache.get(3);       # returns 3
cache.get(4);       # returns 4
                