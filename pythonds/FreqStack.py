import collections

class FreqStack:
    
    def __init__(self):
        self.freq = collections.Counter()
        self.maxfreq = 0
        self.group = collections.defaultdict(list)

    def push(self,item):
        self.freq[item] += 1
        self.maxfreq = max(self.maxfreq,self.freq[item])
        self.group[self.freq[item]].append(item)
        
    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x]-=1
        if not self.group[self.maxfreq]:
            self.maxfreq -=1
        return x
        
                 
    def printall(self):
        print([i for i in self.freq.items()], [j for j in self.group.items()], self.maxfreq)
        
fs =  FreqStack()
fs.push(1)
fs.push(1)
fs.push(2)
fs.push(3)
fs.printall()
fs.pop()
fs.printall()
fs.pop()
fs.printall()

