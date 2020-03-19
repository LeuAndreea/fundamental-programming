import unittest
from DOMAIN.department import Department
class DepartmentTest(unittest.TestCase):
    def test_create(self):
        d1=Department(1,"Contagious diseases",12)
        self.assertEqual(d1.get_id_d(),1)
        self.assertEqual(d1.get_name(),"Contagious diseases")
        self.assertEqual(d1.get_num_of_beds(),12)

if __name__=="__main__":
    unittest.main()