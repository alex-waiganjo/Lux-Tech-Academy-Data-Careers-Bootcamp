class Users:
    # Constructor
    def __init__(self, name, email, pwd):
        self.name = name
        self.email = email
        self.pwd = pwd


# Instances of the class Users
user_1 = Users('alex', 'alex44@gmail.com', 'll')
user_2 = Users('kimmy', 'kimm77@gmail.com', 'passwaaad')

#Memory Location
print(user_1)
print(user_2)

#Each User info
print(f'{user_1.name} ,{user_1.email} , {user_1.pwd}')
print(f'{user_2.name} ,{user_2.email} , {user_2.pwd}')
