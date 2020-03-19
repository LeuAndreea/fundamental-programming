class Patient():
    def __init__(self,first_name,last_name,pnc,disease):
        self.__first_name=first_name
        self.__last_name=last_name
        self.__pnc=pnc
        self.__disease=disease
        
    def __str__(self):
        s="PNC: " + self.__pnc + '\n'
        s+="First name: " + self.__first_name + '\n'
        s+="Last name: " + self.__last_name + '\n'
        s+="Disease: " + self.__disease + '\n'
        return s
    
    def set_first_name(self, first_name):
        self.__first_name=first_name
    def get_first_name(self):
        return self.__first_name
    
    def set_last_name(self, last_name):
        self.__last_name=last_name
    def get_last_name(self):
        return self.__last_name
    
    def set_pnc(self, pnc):
        self.__pnc=pnc
    def get_pnc(self):
        return self.__pnc
    
    def set_disease(self, disease):
        self.__disease=disease
    def get_disease(self):
        return self.__disease
    
    def update_disease(self,disease):
        self.set_disease(disease)
    
    
        
    
    
    
    