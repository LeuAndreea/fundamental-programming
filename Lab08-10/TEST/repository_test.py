
from DOMAIN.business import MyVector
from INFRASTRUCTURE.repository import VectorRepository
import unittest

class RepositoryTest(unittest.TestCase):
    def test_create(self):
        v=MyVector(2,"r",1,[2,40,44,55])
        repo=VectorRepository([])
        self.assertEqual(repo.getSize(),0)
        repo.addVector(v)
        self.assertEqual(repo.getSize(),1)

    def test_getVectorAtIndex(self):
        v=MyVector(21,"r",1,[2,40,44,55])
        u=MyVector(2,"y",2,[1,2])
        repo=VectorRepository([])
        repo.addVector(v)
        repo.addVector(u)
        self.assertEqual(repo.getVectorAtIndex(1),u)

    def test_getIndex(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        self.assertEqual(repo.getIndex(33),2)

    def test_updateVectorByIndex(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        v4=MyVector(54,"g",6,[11,12])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        repo.updateVectorByIndex(1,v4)
        self.assertEqual(repo.listOfVectors[1].get_name_id(), 54 )
        self.assertEqual(repo.listOfVectors[1].get_colour(), "g" )
        self.assertEqual(repo.listOfVectors[1].get_typev(), 6 )
        self.assertEqual(repo.listOfVectors[1].get_values(), [11,12] )
    
    def test_updateVectorById(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        v4=MyVector(54,"g",6,[11,12])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        repo.updateVectorById(33,v4)
        self.assertEqual(repo.listOfVectors[2].get_name_id(), 54 )
        self.assertEqual(repo.listOfVectors[2].get_colour(), "g" )
        self.assertEqual(repo.listOfVectors[2].get_typev(), 6 )
        self.assertEqual(repo.listOfVectors[2].get_values(), [11,12] )
        
    def test_deleteByIndex(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        v4=MyVector(54,"g",6,[11,12])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        repo.addVector(v4)
        repo.deleteByIndex(2)
        self.assertEqual(repo.getSize() ,3 )
        self.assertEqual(repo.listOfVectors[2].get_name_id(), 54 )
        self.assertEqual(repo.listOfVectors[2].get_colour(), "g" )
        self.assertEqual(repo.listOfVectors[2].get_typev(), 6 )
        self.assertEqual(repo.listOfVectors[2].get_values(), [11,12] )
        
    def test_deleteByName(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        v4=MyVector(54,"g",6,[11,12])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        repo.addVector(v4)
        repo.deleteByName(33)
        self.assertEqual(repo.getSize() ,3 )
        self.assertEqual(repo.listOfVectors[2].get_name_id(), 54 )
        self.assertEqual(repo.listOfVectors[2].get_colour(), "g" )
        self.assertEqual(repo.listOfVectors[2].get_typev(), 6 )
        self.assertEqual(repo.listOfVectors[2].get_values(), [11,12] )
        
    def test_getSumOfAll(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        v4=MyVector(54,"g",6,[11,12])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        repo.addVector(v4)
        self.assertEqual(repo.getSumOfAll(),278)
        
    def test_vectorOfSums(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        v4=MyVector(54,"g",6,[11,12])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        repo.addVector(v4)
        self.assertEqual(repo.vectorOfSums(),[59 ,120,44,55 ])
        
    '''def test_draw(self):
        v1=MyVector(21,"r",1,[2,40,44,55])
        v2=MyVector(2,"y",2,[1,2])
        v3=MyVector(33,"b",4,[45,66])
        v4=MyVector(54,"g",6,[11,12])
        repo=VectorRepository([])
        repo.addVector(v1)
        repo.addVector(v2)
        repo.addVector(v3)
        repo.addVector(v4)
        repo.draw() '''

if __name__=="__main__":
    unittest.main()