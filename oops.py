class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@commpany.com'
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    
emp1=Employee('spliz','man','1300')
print(emp1.email)
print(emp1.fullname())