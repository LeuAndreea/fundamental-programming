class DepartmentRepositoryController():
    def __init__(self,repo):
        self.__repo=repo
        
    def add_department(self,d):
        self.__repo.add_department(d)
        
    def get_index(self,d):
        return self.__repo.get_index(d)
    
    def find_by_id_d(self,id_d):
        return self.__repo.find_by_id_d(id_d)
    
    def add_patient_to_department(self,index,p):
        self.__repo.add_patient_to_department(index,p)
        
    def sort_by_patient_pnc(self,index):
        self.__repo.sort_by_patient_pnc(index)
        
    def sort_departments_by_nb_of_patients(self):
        self.__repo.sort_departments_by_nb_of_patients()
        
    def sort_by_patients_above_age(self,limit):
        self.__repo.sort_by_patients_above_age(limit)
        
    def sort_by_nb_of_patients_and_patients_alphabetically(self):
        self.__repo.sort_by_nb_of_patients_and_patients_alphabetically()
    
    def search_departments_with_age_below(self,limit):
        self.__repo.search_departments_with_age_below(limit)
        
    def find_patients_containing_string(self,id_d,substr):
        self.__repo.find_patients_containing_string(id_d,substr)
        
    def find_departmentes_patient_given_first_name(self,name):
        self.__repo.find_departmentes_patient_given_first_name(name)
        