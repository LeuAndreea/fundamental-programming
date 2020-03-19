from DOMAIN.patient import *
from utils import *

class Department():
    
    def __init__(self,id_d,name,num_of_beds,patients):
        self.__id_d=id_d
        self.__name=name
        self.__num_of_beds=num_of_beds
        self.__patients=patients
    
    def __str__(self):
        s="ID: " + self.__id_d + '\n'
        s+="NAME: " + self.__name + '\n'
        s+="NUMBER OF BEDS: " + self.__num_of_beds + '\n' 
        s+="PATIENTS: " + '\n'   
        for el in self.__patients:
            s+= str(el)
        return s
        
    def set_id_d(self,id_d):
        self.__id_d=id_d
    def get_id_d(self):
        return self.__id_d
    
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    
    def set_num_of_beds(self,num_of_beds):
        self.__num_of_beds=num_of_beds
    def get_num_of_beds(self):
        return self.__num_of_beds
    
    def set_patients(self,patients):
        self.__patients=patients
    def get_patients(self):
        return self.__patients
    
    def update_num_of_beds(self,num_of_beds):
        self.set_num_of_beds(num_of_beds)
        
    def add_patient(self,patient):
        self.__patients.append(patient)
        
    def get_patient_at_index(self,index):
        return self.__patients[index]
    
    
    
    
    def sort_by_patient_pnc(self):
        def ascending_pnc(p1,p2):
            if p1.get_pnc() < p2.get_pnc():
                return True
            return False
        
        self.set_patients(MySort(ascending_pnc,self.get_patients()))

    def sort_patients_alphabetically(self):
        def check_alphabetical_order(p1,p2):
            if(p1.get_last_name() < p2.get_last_name()):
                return True
            return False
        
        newl=self.patients
        newl=MySort(check_alphabetical_order,self.patients)
    
    def find_patients_containing_string(self,substr):
        def check_substr(p):
            if substr in p.get_first_name() or substr in p.get_last_name():
                return True
            return False
        
        return MySearch(check_substr,self.__patients)
    
    
    
            
            