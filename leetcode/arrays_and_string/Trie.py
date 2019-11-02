class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        
    def containsKey(self,id):
        
        return self.children[id] 
    
    def getV(self,id):
        return self.children[id] 
    
    def put(self,id,node):
        self.children[id]  =  node
        
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def charToIndex(self,ch):
        return ord(ch) - ord('a')
    
    def insert(self,key):
        crawl = self.root
        for letter in range(len(key)):
            id = self.charToIndex(key[letter])
            print('crawl',crawl)
            if crawl == None or not crawl.children[id]:
                crawl.children[id] = TrieNode()
            crawl = crawl.children[id]
                
        crawl.isEndOfWord = True
        
    def search(self,key):
        crawl = self.root
        for letter in range(len(key)):
            id =self.charToIndex(key[letter])
            if not crawl.children[id]:
                return False
            crawl = crawl.children[id]
        return crawl != None and crawl.isEndOfWord
    
    
    
keys = ['the','that','this']

trie= Trie()

trie.insert(keys[0])
print(trie.root.children)

print(trie.search('thee'))