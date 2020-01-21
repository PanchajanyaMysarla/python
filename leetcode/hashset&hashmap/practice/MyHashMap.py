class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 10000
        self.buckets = [[] for i in range(self.capacity)]
        
    def hash(self,key):
        return key% self.capacity
        
    def index(self,key):
        slot = self.hash(key)
        buck = self.buckets[slot]
        for i,v in enumerate(buck):
            if v and v[0] == key:
                return buck, i
        return buck, -1
            
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        buck, idx = self.index(key)
        print(buck,idx )
        if idx >=0 :
            buck[idx] =  key,value
        else:
            buck.append((key,value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        buck,idx = self.index(key)
      
        if idx >=0:
            return buck[idx][1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        buck,idx = self.index(key)
        if idx >= 0:
            buck.remove(buck[idx])
        return


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
print(obj.get(3))
obj.put(2,1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))



# obj.remove(key)