import unittest
from DOMAIN.patient import Patient
from INFRASTRUCTURE.patient_repository import PatientRepository


class DepartmentRepositoryTest(unittest.TestCase):
    def test_create(self):
        p1=Patient("Andreea","Leu",2704,"cold")
        repo=PatientRepository()
        self.assertEqual(repo.get_size(), 0)
        repo.add_patient(p1)
        self.assertEqual(repo.get_size(), 1)


if __name__=="__main__":
    unittest.main()