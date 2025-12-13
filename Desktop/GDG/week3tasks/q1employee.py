class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    
def annual_salary(employee):
    return employee.salary*12
emp1=Employee("Aderajew",5000)
print("Employee Name:",emp1.name)
print("Annual Salary:",annual_salary(emp1))