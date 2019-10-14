import Graph
import Queue

def build_graph():
    words = wordsFromFile('words.txt')

    d= {}
    g = Graph.Graph()
    
    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    print(d)
    
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
        
        
def wordsFromFile(wordFile):
    words = []
    wordfile = open(wordFile,'r')
    for line in wordfile:
        words.append(line[:-1])
    return words


def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() =='white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() +1)
                nbr.setPred(currrentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
        

g = build_graph()

for v in g:
    for w in v.getConnections():
        print(str(v.getId()) + ',' + str(w.getId()))
        
        
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(g.getVertex('sage'))