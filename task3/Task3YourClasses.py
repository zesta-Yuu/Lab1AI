from thingClass import Thing

class OfficeManager(Thing):
    def __init__(self, location=None):
      
        super().__init__(location) 
    
    def get_package(self):
        #"daily mail"
        return "Office manager"

class ITStaff(Thing):
    def __init__(self, location=None):
      
        super().__init__(location) 
        
    def get_package(self):
       #"donuts from Tim Hortons"
       return "IT"

class Student(Thing):
    def __init__(self, location=None):
      
        super().__init__(location) 
        
    def get_package(self):
        # "pizza from Domino Pizza"
        return "Student"