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

