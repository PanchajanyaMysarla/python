class Vertex:
    def __init__(self,key,distance = 0, predecessor = None, color = None):
        self.id = key
        self.distance = distance
        self.predecessor = predecessor
        self.color = color
        self.connectedTo = {}
        
    def setDistance(self,dis):
        self.distance = dis
        
    def setColor(self,color):
        self.color = color
        
    def getDistance(self):
        return self.distance
    
    def setPred(self,pred):
        self.predecessor = pred
        
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + ' connectedTo: '+ str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self):
        return self.weight