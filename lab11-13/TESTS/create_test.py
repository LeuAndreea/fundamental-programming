from DOMAIN.patient import Patient
from DOMAIN.department import Department 
from INFRASTRUCTURE.patient_repository import PatientRepository
import unittest


class CreateTest(unittest.TestCase):


    def testCreate(self):
        p1=Patient("Andreea","Leu",2704,"cold")
        self.assertEqual(p1.get_first_name(),"Andreea")
        self.assertEqual(p1.get_last_name(),"Leu")
        self.assertEqual(p1.get_pnc(),2704)
        self.assertEqual(p1.get_disease(),"cold")
        
        p2=Patient("Alina","Mirela",222,"sore throat")
        
        d1=Department(1,"Contagious diseases",12,[p1,p2])
        self.assertEqual(d1.get_id_d(),1)
        self.assertEqual(d1.get_name(),"Contagious diseases")
        self.assertEqual(d1.get_num_of_beds(),12)
        
        repo=PatientRepository()
        self.assertEqual(repo.get_size(), 0)
        repo.add_patient(p1)
        self.assertEqual(repo.get_size(), 1)
        repo.add_patient(p2)
        self.assertEqual(repo.get_size(), 2)
        
        repo.update_patient_at_index(0,"Andrada")
        self.assertEqual(repo.get_patient_by_index(0).get_first_name(), "Andrada")
        self.assertEqual(d1.get_patient_at_index(0).get_first_name(),"Andrada")

if __name__ == "__main__":
    unittest.main()