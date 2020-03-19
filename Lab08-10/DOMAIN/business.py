'''
Created on Nov 26, 2018

@author: Leut
'''
class MyVector():
    
    def __init__(self,name=1,c="r",typev=2,values=[1]):
        self.__name_id=name
        self.__colour=c
        self.__typev=typev
        self.__values= values
    
    
    
    def get_name_id(self):
        return self.__name_id
    def set_name_id(self,name):
        self.__name_id=name
        
    def get_colour(self):
            return self.__colour
    def set_colour(self,c):
        if c in ["r", "g", "b", "y","m" ]:
            self.__colour=c
        else:
            raise ValueError("You can't assign that colour")
        
    def get_typev(self):
        return self.__typev
    def set_typev(self,typev):
        if int(typev) > 0:
            self.__typev=typev
        else:
            raise ValueError("Type must be integer greater than 0")
    
    def get_values(self):
        return self.__values
    def set_values(self,values):
        self.__values=values
        
    def add_Scalar(self,scalar):
        for i in range(len(self.__values)):
            self.__values[i]+=scalar
            
    
    def add_Vectors(self,v):
        i = 0
        while i < len(self.__values) and i < len(v):
            self.__values[i]+=v[i]
            i+=1
    
    def substract_Vectors(self,v):
        i = 0
        while i < len(self.__values) and i < len(v):
            self.__values[i]-=v[i]
            i+=1
            
    
    def multiplicate_Vectors(self,v):
        i=0
        res=0
        while i<len(self.__values) and i<len(v):
            res+=self.__values[i]*v[i]
            i+=1
        while i<len(self.__values):
            res+=self.__values[i]
            i+=1
        while i<len(v):
            res+=self.v[i]
            i+=1
        return res
    
    
    def getSum(self):
        s=0
        for el in self.__values:
            s+=el
        return s
    
    def getProduct(self):
        p=1
        for el in self.__values:
            p*=el
        return p
    
    def getAverage(self):
        return self.getSum()//len(self.__values)
    
    def getMinimum(self):
        min_v=self.__values[0]
        for el in self.__values:
            if min_v>el:
                min_v=el
        return min_v
    
    def getMaximum(self):
        max_v=self.__values[0]
        for el in self.__values:
            if max_v<el:
                max_v=el
        return max_v
    
   
    
    def __eq__(self,other):
        if self.__name_id==other.get_name_id():
            return True
        else:
            return False
    def __str__(self):
        s = "Id: " + self.get_name_id() +'\n'
        s+= "Colour: " + self.get_colour() +'\n'
        s+="Type: " + self.get_typev() +'\n'
        s+="Values: "
        for el in self.__values:
            s+= str(el) + " "
        return s
    
    