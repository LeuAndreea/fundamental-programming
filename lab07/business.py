'''
Created on Jan 13, 2019

@author: Leut
'''

class MyPoint():
    def __init__(self,coord_x,coord_y,colour):
        self.__coord_x=coord_x
        self.__coord_y=coord_y
        self.__colour=colour
        
        
    def get_coord_x(self):
        return self.__coord_x
    def set_coord_x(self,coord_x):
        self.__coord_x=coord_x
        
    def get_coord_y(self):
        return self.__coord_y
    def set_coord_y(self,coord_y):
        self.__coord_y=coord_y
        
    def get_colour(self):
        return self.__colour
    def set_colour(self,colour):
        self.__colour=colour
        
    def check_square(self,x,y,length):
        if self.get_coord_x()>=x and self.get_coord_x()<=x+length and self.get_coord_y()<=y and self.get_coord_y()>=y-length:
            return True
        return False
    
    def check_rectangle(self,x,y,length,width):
        if self.get_coord_x()>=x and self.get_coord_x()<=x+length and self.get_coord_y()<=y and self.get_coord_y()>=y-width:
            return True
        return False
    def check_circle(self,x,y,):
        
    
    def __str__(self):
        s="Point(" + str(self.__coord_x)+ "," + str(self.__coord_y) + "of colour" + self.__colour 
        return s
    

def test_create():
    p=MyPoint(5,6,"red")
    assert p.get_coord_x()==5
    assert p.get_coord_y()==6
    assert p.get_colour()=="red"
    
    p.set_coord_x(7)
    p.set_coord_y(8)
    p.set_colour("green")
    
    assert p.get_coord_x()==7
    assert p.get_coord_y()==8
    assert p.get_colour()=="green"
    
def test_check_square():
    p1=MyPoint( 7,7 , "red")
    p2=MyPoint( 8,-1 , "red")
    p3=MyPoint( 13,4 , "red")
    p4=MyPoint( 5,-3 , "red")
    p5=MyPoint( 4,9 , "red")
    
    assert p1.check_square(5, 4, 7)==False
    assert p2.check_square(5, 4, 7)==True
    assert p3.check_square(5, 4, 7)==False
    assert p4.check_square(5, 4, 7)==True
    assert p5.check_square(5, 4, 7)==False
    
def test_check_rectangle():
    p1=MyPoint( 7,7 , "red")
    p2=MyPoint( 8,-1 , "red")
    p3=MyPoint( 13,4 , "red")
    p4=MyPoint( 5,-3 , "red")
    p5=MyPoint( 4,9 , "red")
    
    assert p1.check_square(5, 4, 7)==False
    assert p2.check_square(5, 4, 7)==True
    assert p3.check_square(5, 4, 7)==False
    assert p4.check_square(5, 4, 7)==True
    assert p5.check_square(5, 4, 7)==False
    
test_create()
test_check_square()
    