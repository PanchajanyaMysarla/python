class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 100000
        self.capacity = 100000
        
    def hash(self,key):
        return key % self.capacity
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashId = self.hash(key)
        self.table[hashId]= value
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashId = self.hash(key)
        
        if self.table[hashId] == None:
            return -1
        return self.table[hashId]
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
         hashId = self.hash(key)
         self.table[hashId] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_buckets = 1000
        self.buckets = [-1] * self.num_buckets

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.num_buckets
        
        if self.buckets[index] == -1:
            self.buckets[index] = []
            
        for i, kv_pair in enumerate(self.buckets[index]):
            if kv_pair[0] == key:
                self.buckets[index][i] = (key, value)  # tuples don't support assignment
                return
            
        self.buckets[index].append((key, value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.num_buckets
        
        if self.buckets[index] == -1:
            return -1
        
        for kv_pair in self.buckets[index]:
            if kv_pair[0] == key:
                return kv_pair[1]
            
        return -1
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.num_buckets
        
        index_to_remove = -1
        
        if self.buckets[index] == -1:
            return
        
        for i, kv_pair in enumerate(self.buckets[index]):
            if kv_pair[0] == key:
                index_to_remove = i
                break
        
        if index_to_remove == -1:
            return
        else:
            del self.buckets[index][index_to_remove]


"""