'''
Created on Jan 13, 2019

@author: Leut
'''
from business import MyPoint


class PointRepository():
    def __init__(self):
        self.lst= [ ]
        
    def getall(self):
        return self.lst
    def get_size(self):
        return len(self.lst)
    
    def add_point(self,point):
        self.lst.append(point)
    def get_point_at_index(self,index):
        if (index<0 or index>self.get_size()-1):
            raise ValueError("Index out of range!")
        else:
            return self.lst[index]
    def get_points_of_colour(self,colour):
        lst2=[ ]
        for el in self.lst:
            if el.get_colour()==colour:
                lst2.append(el)
        return lst2
    
    
    def get_points_inside_sqaure(self,x,y,length):
        lst2=[ ]
        for el in self.lst:
            if el.check_square(x,y,length):
                lst2.append(el)
        return lst2
    def get_points_inside_rectangle(self,x,y,length,width):
        lst2=[ ]
        for el in self.lst:
            if el.check_rectangle(x,y,length,width):
                lst2.append(el)
        return lst2
    

def test_add_point():
    repo=PointRepository()
    assert repo.get_size()==0
    
    p=MyPoint(2,4,"yellow")
    repo.add_point(p)
    assert repo.get_size()==1
    
def test_get_point_at_index():
    repo=PointRepository()
    p1=MyPoint(2,4,"yellow")
    p2=MyPoint(5,6,"red")
    repo.add_point(p1)
    repo.add_point(p2)
    assert repo.get_point_at_index(1)==p2 
    
def test_get_points_of_colour():
    repo=PointRepository()
    p1=MyPoint(2,4,"yellow")
    p2=MyPoint(5,6,"red")
    p3=MyPoint(9,1,"yellow")
    
    repo.add_point(p1)
    repo.add_point(p2)
    repo.add_point(p3)
    
    lst=repo.get_points_of_colour("yellow")
    assert len(lst)==2
    
test_add_point()
test_get_point_at_index()  
test_get_points_of_colour()