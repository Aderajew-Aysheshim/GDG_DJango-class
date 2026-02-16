from abc import ABC, abstractmethod

class Employee(ABC): 
    @abstractmethod 
    def calculate_salary(self):
        pass 

class FullTimeEmployee(Employee):
    def calculate_salary(self): 
        return "Full time salary calculated"
    

fte = FullTimeEmployee()
print(f"FullTimeEmployee salary: {fte.calculate_salary()}")
