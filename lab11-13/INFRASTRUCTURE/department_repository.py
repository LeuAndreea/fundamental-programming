from utils import *

class DepartmentRepository():
    def __init__(self):
        self.__listOfDepartments= [ ]
        
    def get_all(self):
        return self.__listOfDepartments
    
    def get_index(self,id_d):
        for i in range(len(self.__listOfDepartments)):
            if self.__listOfDepartments[i].get_id_d()==id_d:
                return i
        return -1
    
    def get_size(self):
        return len(self.__listOfDepartments)
    
    def add_department(self,depart):
        i=self.get_index(depart.get_id_d())
        if i==-1:
            self.__listOfDepartments.append(depart)
        else:
            raise ValueError("Department already added")
    
    def add_patient_to_department(self,index,p):
        self.__listOfDepartments[index].add_patient(p)
                
    def find_by_id_d(self,id_d):
        i=self.get_index(id_d)
        print(i)
        if (i==-1):
            raise ValueError("Department doesn't exist")
        return self.__listOfDepartments[i]
            
    def get_department_at_index(self,index):
        return self.__listOfDepartments[index]
    
    def sort_by_patient_pnc_r(self,index):
        d=self.get_department_at_index(index)
        d.sort_by_patient_pnc()
        
    def sort_departments_by_nb_of_patients(self):
        def check_nb_of_patients(d1,d2):
            if len(d1.get_patients())<= len(d2.get_patients()):
                return True
            return False
        
        newl=MySort(check_nb_of_patients,self.__listOfDepartments)
        newl=self.__listOfDepartments
        
    def sort_by_patients_above_age(self,limit):
        def check_above(p):
            year_limit=str(2019-limit)
            year_limit=year_limit[2:]
            
            year_patient=p.get_pnc()
            year_patient=year_patient[1:3]
            
            if year_patient<year_limit:
                return True
            return False
        
        def check_nb_of_patients(d1,d2):
            if len(MySearch(check_above,d1.get_patients()))<= len(MySearch(check_above,d2.get_patients())):
                return True
            return False
        
        newl=MySort(check_nb_of_patients,self.__listOfDepartments)
        newl=self.__listOfDepartments
        
    def sort_by_nb_of_patients_and_patients_alphabetically(self):
        self.sort_departments_by_nb_of_patients()
        
        for el in self.__listOfDepartments:
            el.sort_patients_alphabetically()
            
    def search_departments_with_age_below(self,limit):
        def check_above(p):
            year_limit=str(2019-limit)
            year_limit=year_limit[2:]
            
            year_patient=p.get_pnc()
            year_patient=year_patient[1:3]
            
            if year_patient<year_limit:
                return True
            return False
        
        def check_above_d(d):
            if len(MySearch(check_above,self.__patients))>0:
                return True
            return False
        return MySearch(check_above_d,self.__listOfDepartments)
    
    def find_patients_containing_string(self,id_d,substr):
        index=self.get_index(id_d)
        return self.__listOfDepartments[index].find_patients_containing_string(substr)
    
    def find_departmentes_patient_given_first_name(self,name):
        def check_name(p):
            if p.get_first_name()==name:
                return True
            return False
        
        def check_name_d(d):
            if len(MySearch(check_name,self.__patients))>0:
                return True
            return False
        
        return MySearch(check_name_d,self.__listOfDepartments)