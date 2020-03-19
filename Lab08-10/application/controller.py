
class VectorController():
    def __init__(self,repo):
        self.__repo=repo
        
    def addVector(self,v):
        self.__repo.store(v)
    
    def getVectors(self):
        self.__repo.getVectors(self)
    def getVectorAtIndex(self,index):
        self.__repo.getVectorAtIndex(index)
        
    def updateVectorById(self,name,v):
        self.__repo.updateVectorById(self,name,v)
        
    def updateVectorByIndex(self,i,v):
        self.__updateVectorByIndex(self,i,v)
        
    def deleteByIndex(self,index):
        self.__repo.deleteByIndex(self,index)
        
    def deleteByName(self,name):
        self.__repo.deleteByName(self,name)
        
    def draw(self):
        self.__repo.draw()
