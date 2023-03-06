class Users:
    # Constructor
    def __init__(self, name, email, pwd) -> None:
        self.name = name
        self.email = email
        self.pwd = pwd

    def user_info(self):
        return  f'{self.name} ,{self.email} , {self.pwd}'   


# Instances of the class Users
user_1 = Users('alex', 'alex44@gmail.com', 'll')
user_2 = Users('kimmy', 'kimm77@gmail.com', 'passwaaad')

#Method 1
print(user_1.user_info())
print(user_2.user_info())

#Method 2
print('Method 2')
print(Users.user_info(user_1))

#Memory Location
print(user_1)
print(user_2)

#Print Each User info without the user_info function
# print(f'{user_1.name} ,{user_1.email} , {user_1.pwd}')
# print(f'{user_2.name} ,{user_2.email} , {user_2.pwd}')



class Employee:

    no_of_employees = 0
    raise_amount= 1.04
    def __init__(self,fname,lname,pay) -> None:
        self.fname = fname
        self.lname = lname
        self.pay = pay

        Employee.no_of_employees += 1

    def fullname(self):
        return '{} ,{}'.format(self.fname,self.lname) 
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount =amount  

    @classmethod
    def from_string(cls,emp_str):
        fname,lname,pay = emp_str.split('-') 
        return cls(fname,lname,pay) 
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    

import datetime
my_date = datetime.date(2023,3,7) 
print(Employee.is_workday(my_date))

#Initial no of Employees is 0
print(Employee.no_of_employees)

#Instantiate the Class
emp1=Employee('Rose','Williams',90000)
emp2=Employee('Jimmy','Howdy',80000)

#Get the No of Employees
print(Employee.no_of_employees)

#Print the fullname
print(emp1.fullname())

#Increase pay
print(emp1.apply_raise())

#Attributes
print(Employee.__dict__)
print(emp1.__dict__)

print(Employee.raise_amount)
Employee.set_raise_amt(1.06)
print(Employee.raise_amount)
print(emp1.raise_amount)


#Passing strings
emp_str1 =  'ken-james-30000'
emp3 = Employee.from_string(emp_str1)
print(emp3.fname)
print(emp3.pay)
print(emp3.lname)