import unittest
from DOMAIN.business import MyVector

class MyVectorTest(unittest.TestCase):
    def test_create(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        self.assertEqual(v.get_name_id(),21)
        self.assertEqual(v.get_colour(),"r")
        self.assertEqual(v.get_typev(),1)
        self.assertEqual(v.get_values(),[2,40,44,55])
        v.set_name_id(2)
        v.set_colour("y")
        v.set_typev(2)
        v.set_values([40,50,30])
        self.assertEqual(v.get_name_id(),2)
        self.assertEqual(v.get_colour(),"y")
        self.assertEqual(v.get_typev(),2)
        self.assertEqual(v.get_values(),[40,50,30])
   
    def test_add_Scalar(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        v.add_Scalar(5)
        self.assertEqual(v.get_values(),[7,45,49,60])

    def test_add_Vectors(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        v.add_Vectors([1,1])
        self.assertEqual(v.get_values(),[3,41,44,55])

    def test_substract_Vectors(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        v.substract_Vectors([1,1])
        self.assertEqual(v.get_values(),[1,39,44,55])

    def test_multiplicate_Vectors(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        v.multiplicate_Vectors([2,2,2])
        self.assertEqual(v.get_values(),[4,80,88,55])
    
    def test_getSum(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        self.assertEqual(v.getSum(),141)    
    
    def test_getProduct(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        self.assertEqual(v.getProduct(),193600)
    
    def test_getAverage(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        self.assertEqual(v.getAverage(),35)
    
    def test_getMinimum(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        self.assertEqual(v.getMinimum(),2) 
    
    def test_getMaximum(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        self.assertEqual(v.getMaximum(),55)

if __name__=="__main__":
    unittest.main()
    