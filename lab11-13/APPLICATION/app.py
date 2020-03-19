from DOMAIN.department import Department
from DOMAIN.patient import Patient
from INFRASTRUCTURE.department_repository import DepartmentRepository
from INFRASTRUCTURE.patient_repository import PatientRepository
from CONTROLLERS.departments_controller import DepartmentRepositoryController
from CONTROLLERS.pateints_controller import PatientRepositoryController
from APPLICATION.console import UI

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



d1=Department("1e","Intensive Recovery","12",[p1])

p_repo=PatientRepository()
d_repo=DepartmentRepository()

p_repo.add_patient(p1)
d_repo.add_department(d1)

p_controller=PatientRepositoryController(p_repo)
d_controller=DepartmentRepositoryController(d_repo)

ui=UI(p_controller,d_controller)


ui.mainMenu()

