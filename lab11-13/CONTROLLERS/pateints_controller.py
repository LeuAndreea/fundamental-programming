class PatientRepositoryController():
    def __init__(self,repo):
        self.__repo=repo
        
    def add_patient(self,p):
        self.__repo.add_patient(p)
        
    def get_index(self,code):
        return self.__repo.get_index(code)
    
    def get_patient_by_index(self,i):
        return self.__repo.get_patient_by_index(i)
    
    