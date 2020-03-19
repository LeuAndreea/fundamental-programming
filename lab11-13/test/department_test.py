from DOMAIN.deaprtment import Department
from DOMAIN.patient import Patient
import unittest
class RepositoryTest(unittest.TestCase):
    def testCreate(self):
        p1=Patient()