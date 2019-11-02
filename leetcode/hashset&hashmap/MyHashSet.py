"""
class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)

    def remove(self, key):
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)

    def contains(self, key):
        _, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 10
        self.capacity = 10000
        
    def add(self, key: int) -> None:
        hashId = self.hash(key)
        print(hashId)
        
        self.table[hashId] = key
        
        

    def remove(self, key: int) -> None:
        hashId = self.hash(key)
        print(hashId)
        if hashId in self.table:
            del self.table[hashId]
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashId = self.hash(key)
        print(hashId)
        return hashId in self.table
    
    def hash(self,key):
        return key % self.capacity
    
    def printAll(self):
        print(self.table)

# Your MyHashSet object will be instantiated and called as such:
hashSet = MyHashSet()
hashSet.add(1);         
hashSet.add(2);          
hashSet.remove(2);
hashSet.printAll()
