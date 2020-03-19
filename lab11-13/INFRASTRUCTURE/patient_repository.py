class PatientRepository():
    def __init__(self):
        self.__listOfPatients=[ ]

        
    def get_all(self):
        return self.__listOfPatients
    
    def get_index(self,pnc):
        for i in range(len(self.__listOfPatients)):
            if self.__listOfPatients[i].get_pnc()==pnc:
                return i
        return -1
    
    def get_size(self):
        return len(self.__listOfPatients)
    
    def add_patient(self,patient):
        i=self.get_index(patient.get_pnc())
        if i==-1:
            self.__listOfPatients.append(patient)
        else:
            raise ValueError("Patient already existent")
        
    def delete_by_code(self,code):
        i=self.get_index(code)
        if i==-1:
            raise ValueError("Patient already existent")
        else:
            del (self.__listOfPatients[i])
            
    def get_patient_by_index(self,index):
        return self.__listOfPatients[index]
    
    def update_patient_at_index(self,index,first_name):
        self.__listOfPatients[index].set_first_name(first_name)
        
        
            
        
        