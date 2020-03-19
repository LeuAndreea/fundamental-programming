'''
Created on Nov 26, 2018

@author: Leut
'''
import matplotlib.pyplot as plt
###from DOMAIN.business import MyVector
class VectorRepository(object):


    def __init__(self,vectors):
        self.listOfVectors= []
        
    def addVector(self,v):
        for el in self.listOfVectors:
            if (el==v):
                raise ValueError("Vector already existent")
        self.listOfVectors.append(v)
        
    def getVectors(self):
        return self.listOfVectors
    
    def getSize(self):
        return len(self.listOfVectors)
    
    def getVectorAtIndex(self,index):
        if index>0 and index<len(self.listOfVectors): 
            return self.listOfVectors[index]
        else:
            raise ValueError("Index out of range.")
    
    def getIndex(self,name):
        for i in range(len(self.listOfVectors)):
            if self.listOfVectors[i].get_name_id()==name:
                return i
        return -1
    
    def updateVectorById(self,name,v):
        i=self.getIndex(name)
        if i==-1:
            raise ValueError("Id does not exist")
        else:
            self.listOfVectors[i].set_name_id(v.get_name_id())
            self.listOfVectors[i].set_colour(v.get_colour())
            self.listOfVectors[i].set_typev(v.get_typev())
            self.listOfVectors[i].set_values(v.get_values())
    
    def updateVectorByIndex(self,i,v):
        if i>0 and i<len(self.listOfVectors):
            self.listOfVectors[i].set_name_id(v.get_name_id())
            self.listOfVectors[i].set_colour(v.get_colour())
            self.listOfVectors[i].set_typev(v.get_typev())
            self.listOfVectors[i].set_values(v.get_values())
        else:
            raise ValueError("Index out of range.")
    
    
            
    def deleteByIndex(self,index):
        if index>0 and index<len(self.listOfVectors):
            del (self.listOfVectors[index])
        else:
            raise ValueError("Index out of range.")
        
    def deleteByName(self,name):
        i=self.getIndex(name)
        if i==-1:
            raise ValueError ("Id not existent")
        else:
            del (self.listOfVectors[i])
            
    def getSumOfAll(self):
        s=0
        for el in self.listOfVectors:
            s+=el.getSum()
        return s
    
    def vectorOfSums(self):
        res=self.listOfVectors[0]
        for i in range(1,len(self.listOfVectors)):
            if len(self.listOfVectors[i].get_values())>len(res.get_values()):
                v=res.getValues()
                res.set_values(self.listOfVectors[i].get_values())
                res.add_Vectors(v)
            else:
                v=self.listOfVectors[i].get_values()
                res.add_Vectors(v)
        return res.get_values()
    
    def draw(self):
        for el in self.listOfVectors:
            s=el.get_colour()
            if el.get_typev()==1:
                s+="o"
            if el.get_typev()==2:
                s+="^"
            if el.get_typev()==3:
                s+="s"
            if el.get_typev()>=3:
                s+="D"
            plt.plot(el.get_values(),s)
        plt.show()