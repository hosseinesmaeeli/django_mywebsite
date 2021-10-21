class  employee:
    def __init__(self, f_name,l_name):  
        self.f_name = f_name 
        self.l_name = l_name 
        self.salary= "3000$"
      
  
    def print_salary(self):  
        print('first name : ', self.f_name) 
        print('last name : ', self.l_name)   
        print("salary : ",self.salary)    
      
p = employee('hossein','esmaeeli12')  
p.print_salary()        