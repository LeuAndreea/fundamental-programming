from DOMAIN.department import Department
from DOMAIN.patient import Patient

class UI():
    def __init__(self,pcontroller,dcontroller):
        self.__pcontroller=pcontroller
        self.__dcontroller=dcontroller
        
    @staticmethod
    def Menu():
        s="1-Add a new department" +'\n'
        s+="2-Add a new patient" +'\n'
        s+="3-Assign department to patient" +'\n'
        s+="4-Sort the patients in a department by their pnc" + '\n'
        s+="5-Sort all departments by nb of patients" + '\n'
        s+="6-Sort departments by the number of patients having the age above a given limit"
        s+="7-Sort departments by the number of patients and the patients in a department alphabetically"
        s+="8-Identify departments where there are patients under a given age"
        s+="9-Identify patients from a given department for which the first name or last name contain a given string"
        s+="10-Identify department/departments where there are patients with a given first name"
        return s

    @staticmethod
    def readPositiveInteger(msg):
        n=-1
        while(n<0):
            n=int(input(msg))
        return n
    
    @staticmethod
    def readDepartment():
        id_d=input("Introduce the id of the department:")
        name=input("Intoduce the name of the department:")
        num_of_beds=input("Introduce the number of beds:")
        return Department(id_d,name,num_of_beds,[  ])
    
    @staticmethod
    def readPatient():
        first_name=input("Introduce the first name")
        last_name=input("Introduce last name of patient")
        code=input("Intoduce the code:")
        disease=input("Introduce disease:")
        return Patient(first_name,last_name,code,disease)
    
    
    ###needs testing!!
    def addPatientToDepartment(self,id_d):
        index=self.__dcontroller.get_index(id_d)
        if (index==-1):
            raise ValueError("Department not existent!")
        
        ans="y"
        while (ans=="y"):
            pnc=input("Introduce code of patient:")
            i=self.__pcontroller.get_index(pnc)
            if i == -1:
                print("Code not in the records")
                ans=input( "Create new entry for patient?Y/n")
                if ans=="y":
                    p=UI.readPatient()
                    self.__pcontroller.add_patient(p)
                    self.__dcontroller.add_patient_to_department(index,p)
            else:
                p=self.__pcontroller.get_patient_by_index(i)
                self.__dcontroller.add_patient_to_department(index,p)        
            ans=input("Do you wish to add another patient?Y/n")           
                    
    
    def mainMenu(self):
        while True:
            print(UI.Menu())
            try:
                option=UI.readPositiveInteger("Choose a valid option:")
                if option==0:
                    return
                if option==1:
                    d=UI.readDepartment()
                    self.__dcontroller.add_department(d)
                    try:
                        self.__dcontroller.add_department(d)
                        print("Department succesfully added! \n")
                        answer=input("Do you wish to add patients to the department now? Y/n")
                        if answer=="y":
                            UI.addPatientsToDepartment(d)
                    except Exception as ex:
                        print("Department already existent!")
                    
                        
                if option==2:
                    p=UI.readPatient()
                    try:
                        self.__pcontroller.add_patient(p)
                    except Exception as ex:
                        print("Patient already existent!")
                if option==3:
                    id_d=input("Introduce the id of the department: ")
                    self.addPatientToDepartment(id_d)
                if option==4:
                    id_d=input("Introduce the id of the department: ")
                    self.__dcontroller.sort_by_patient_pnc()
                if option==5:
                    self.__dcontroller.sort_departments_by_nb_of_patients()
                if option==6:
                    limit=int(input("Intorduce the age:"))
                    self.__dcontroller.sort_by_patients_above_age(limit)
                if option==7:
                    self.__dcontroller.sort_by_nb_of_patients_and_patients_alphabetically()
                if option==8:
                    limit=int(input("Intorduce the age:"))
                    self.__dcontroller.search_departments_with_age_below(limit)
                if option==9:
                    id_d=input("Introduce the id of the department: ")
                    substr=input("Introduce the string: ")
                    self.__dcontroller.find_patients_containing_string(id_d,substr)
                if option==10:
                    name=("Introduce the name: ")
                    self.__dcontroller.find_departmentes_patient_given_first_name(name)
                    
            except Exception as ex:
                print("An error occured" + str(ex))
                
            