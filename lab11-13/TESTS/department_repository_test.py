import unittest
from DOMAIN.department import Department
from DOMAIN.patient import Patient
from INFRASTRUCTURE.department_repository import DepartmentRepository


class DepartmentRepositoryTest(unittest.TestCase):
    
        
    def test_sort_by_patient_pnc(self):
        p1=Patient("Andreea","leu","299897","Appendicitis")
        p2=Patient("Alina","Mirela","298568","sore throat")
        p3=Patient("Z ","edf ","176668"   ,"  grg ")
        p4=Patient(" Dfedf"," H"," 100876 "  ,"  reg ")
        
        
        d1=Department("1","Contagious diseases","12",[p1,p2,p3,p4])
        repo=DepartmentRepository()
        repo.add_department(d1)
        repo.sort_by_patient_pnc_r(0)
        
        try:
            l=d1.get_patients()
            if l[0]==p4 and l[1]==p3 and l[2]==p2 and l[3]==p1:
                assert True
        except Exception:
            assert False
        
        ###print(d1)
        
    def test_sort_departments_by_nb_of_patients(self):
        
        p1=Patient("Andreea","leu","299897","Appendicitis")
        p2=Patient("Alina","Mirela","2","sore throat")
        p3=Patient("Z ","edf ","176668"   ,"   ")
        p4=Patient(" Dfedf"," H"," 100876 "  ,"   ")
        p5=Patient("Fredff "," I ","203456"  ,"   ")
        p6=Patient(" Alina","F ","274567   "  ,"   ")
        p7=Patient("N ","P ","208556  "  ,"   ")
        p8=Patient("Alina ","Dedfg ", "29667  "  ,"   ")
        p9=Patient("Y ","T ","18578  "  ,"   ")
        p10=Patient("V ","C  ", "17367  "  ,"   ")
        
        d1=Department("1","Contagious diseases","12",[p1,p2,p3,p4,p5])
        d2=Department("2","fff","14",[p6,p7])    
        d3=Department("3","yyy","4",[p8])
        d4=Department("4","aaa","20",[p9,p10])
        
        repo=DepartmentRepository()
        repo.add_department(d1)
        repo.add_department(d2)
        repo.add_department(d3)
        repo.add_department(d4)
        
        repo.sort_departments_by_nb_of_patients()
        try:
            l=repo.get_all()
            if l[0]==d3 and l[1]==d2 and l[2]==d4 and l[3]==d1:
                assert True
        except Exception:
            assert False
    
    def test_sort_departments_by_above_age(self):
        p1=Patient("Andreea","leu","299897","Appendicitis")
        p2=Patient("Alina","Mirela","28567","sore throat")
        p3=Patient("Z ","edf ","176668"   ,"   ")
        p4=Patient(" Dfedf"," H"," 100876 "  ,"   ")
        p5=Patient("Fredff "," I ","255456"  ,"   ")
        p6=Patient(" Alina","F ","274567   "  ,"   ")
        p7=Patient("N ","P ","208556  "  ,"   ")
        p8=Patient("Alina ","Dedfg ", "29667  "  ,"   ")
        p9=Patient("Y ","T ","18578  "  ,"   ")
        p10=Patient("V ","C  ", "17367  "  ,"   ")
        
        d1=Department("1","Contagious diseases","12",[p1,p2,p3,p4,p5])
        d2=Department("2","fff","14",[p6,p7])    
        d3=Department("3","yyy","4",[p8])
        d4=Department("4","aaa","20",[p9,p10])
            
        repo=DepartmentRepository()
        repo.add_department(d1)
        repo.add_department(d2)
        repo.add_department(d3)
        repo.add_department(d4)
        repo.sort_by_patients_above_age(25)
        
        try:
            l=repo.get_all()
            if l[0]==d3 and l[1]==d2 and l[2]==d4 and l[3]==d1:
                assert True
        except Exception:
            assert False
            
    def test_find_patients_containing_string(self):
        p1=Patient("Andreea","leu","299897","Appendicitis")
        p2=Patient("Alina","Mirela","28567","sore throat")
        p3=Patient("Z ","edf ","176668"   ,"   ")
        p4=Patient(" Dfedf"," H"," 100876 "  ,"   ")
        p5=Patient("Fredff "," I ","255456"  ,"   ")
        p6=Patient(" Alina","F ","274567   "  ,"   ")
        p7=Patient("N ","P ","208556  "  ,"   ")
        p8=Patient("Alina ","Dedfg ", "29667  "  ,"   ")
        p9=Patient("Y ","T ","18578  "  ,"   ")
        p10=Patient("V ","C  ", "17367  "  ,"   ")
        
        d1=Department("1","Contagious diseases","12",[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10])
        
        
            
        
            
        
        
        
if __name__=="__main__":
    unittest.main()