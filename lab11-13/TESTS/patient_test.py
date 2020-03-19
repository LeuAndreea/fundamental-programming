from DOMAIN.patient import Patient
import unittest

class PatientTest(unittest.TestCase):
    def test_create(self):
        p1=Patient(1, "Andreea","Leu",2704,"cold")
        self.assertEqual(p1.get_id_d(),1)
        self.assertEqual(p1.get_first_name(),"Andreea")
        self.assertEqual(p1.get_last_name(),"Leu")
        self.assertEqual(p1.get_pnc(),2704)
        self.assertEqual(p1.get_disease(),"cold")
        

if __name__=="__main__":
    unittest.main()