class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee{0} :".format(Employee.empCount))
    def displayEmployee(self):
        print("Name :",self.name,",salary:",self.salary)
emp1=Employee("Likhi",9999)
emp1.displayEmployee()
emp1.salary=17000
emp1.experience=3
emp1.displayEmployee()
emp1.name='manoj'
emp1.displayEmployee()
print(emp1.experience)
##del emp1.salary
emp1.displayEmployee()
