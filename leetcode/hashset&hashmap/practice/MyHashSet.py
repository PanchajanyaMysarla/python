class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.size = 1000
        
        self.buckets = [ [] for _ in range(self.size) ]
        
        print(self.buckets)
        
        
    def hash(self,key):
        
        return key % self.size
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
       buck, idx =  self.index(key)
       
       if idx >=0:
           return
        buck.append(key)
       
            
        
        
    def index(self,key):
        slot = self.hash(key)
        buck = self.buckets[slot]
        
        for i,v in enumerate(self.buckets[slot]):
            if v == key:
                return buck, i
        return buck, -1
                

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        buck, idx = seld.index(key)
        if idx < 0:
            return
        buck.remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        buck,idx = self.index(key)
        return idx >= 0

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)