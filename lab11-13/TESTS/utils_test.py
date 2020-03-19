'''
Created on Dec 18, 2018

@author: Leut
'''
import unittest
from DOMAIN.utils import *

class Test(unittest.TestCase):


    def test_mysort(self):
        self.assertEqual(MySort(f,[2,1,10,10,20,3,8,4]),[1,2,3,4,8,10,10,20])


if __name__=="__main__":
    unittest.main()