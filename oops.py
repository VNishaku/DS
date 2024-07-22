class Employee:
    N0_of_Employ=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@commpany.com'

        Employee.N0_of_Employ+=1
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    
emp1=Employee('spliz','man','1300')
emp2=Employee('Dorota','wyon',1900)
emp3=Employee('Cactus','tanwar',9999)
print(emp1.email)
print(Employee.N0_of_Employ)