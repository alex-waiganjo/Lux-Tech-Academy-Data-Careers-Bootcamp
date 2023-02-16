#Types of Operators

            #1. Arithmetic Operators
            #2. Assignment  ``
            #3. Comparison ``
            #4. Logical ``
            #5. Identity ``
            #6. Membership ``
            #7.  BitWise ``


# 1. Arithmetic ``
x =20
y =90
z=3
add= x+y
subtract = y-x
divide = y/x
multiply = x*y
modulus = y%x
exponential = x**z
floor_division = y//x

print(add) #110
print(subtract) #70
print(divide) #4.5
print(multiply) #1800
print(modulus) #10
print(exponential) #8000
print(floor_division) #4


#2. Assignment ``
a=30  # =
b=100 # =
c=30  # =

b+=20 # +=
c+=b  # +=
a+=c  # +=
print("(b+=20) ={}".format(a)) #180
print("(c+=b) ={}".format(b)) #120
print("(a+=c) ={}".format(c)) #150

c-=b  # -=
b-=10 # -=
a-=10 # -=
print("(c-=b) ={}".format(c)) #30
print("(b-=10) ={}".format(b)) #110
print("(a-=10) ={}".format(a)) #170

a*=10 # *=
b*=2  # *=
c*=5  # *=
print("(a*=10) ={}".format(a)) #1700
print("(b*=2) ={}".format(b)) #220
print("(c*=5)  ={}".format(c)) #150

a%=b # %=
b%=23 # %=
c%=20 # %=
print(a) #160
print(b) #13
print(c) #10

a|=b # |=
b|=c # |=
c|=a # |=
print(a) #173
print(b) #15
print(c) #175


#3. Comparison ``
u=30
v=50
w=90
m=30
print(u==m) #True
print(u!=m) #False
print(u!=w) #True
print(w>v) #True
print(w<m) #False
print(u>=m) #True
print(w>=v) #True
print(v<=u) #False
print(u<w) #True
print(m>(90-80)) #True


#4. Logical ``
   #(a) Not
   #(b) And
   #(c) Or

   #  Parameter1 + Parameter2 = Value
      #AND Operator
      #False + False = False
      #True + True = True
      #True + False = False
      #False + True = False

      #OR Operator
      #False + False = False
      #True + True = True
      #True + False =True
      #False + True = True

      #NOT Operator
      # Not(True) =False
      # Not(False) =True


name='alex'
day = 'thursday'
code= True

print(name=='alex' and day=='thursday') #True
print(name=='alexis' and day=='thursday') #False since one parameter is incorrect
print(name=='alex' or day=='Monday') #True since one of the parameters is True
print(name=='jane' or day=='sunday') #False
print(name=='james' and day=='thursday' and code==True) #False
print(name=='james' or day=='thursday' or code==True) #True
print(name=='james' and day=='thursday' or code==True) #True
print(name=='james' and day=='thursday' and code==False) #False
print(name=='alex' and day=='thursday' and code==True) #True

print(not(name=='alexf') and   code==True) #True
print(not(name=='alex') and   code==True) #False
print(not(name=='alexf')) #True
print(f" End of Logical Operators, {not(name=='alex')}") #False


#5. Identity Operators
   # -> Used to compare objects (same object with same memory location)
user_is_authenticated = True
logged_in = True 
user_registered = False
print(user_is_authenticated is logged_in) #True
print(user_is_authenticated is not logged_in) #False  
print(user_registered is logged_in) #False
print(f'End of Identity Operators {user_registered is not logged_in}') #True


#6. Membership ``
   #(a). in
   #(b).  not in 
   
   # -> Used to test if a sequence is present in an object

users = ['Alex','Rose','Andrew','Esther','Abby','Kelvin','Charity','Ken','Jason']
print('Alex' in users)#True
print('Jimmy' in users)#False
print('Jimmy' not in users)#True

if 'Risper' in users:
    print('Risper is Present in the Users list')
else:
    print("Risper is not present in the Users list") #Result   

if 'Paul' not in users:
    print("Paul is not present in the Users list")#Result
else:
    print('Paul is present')  

if 'Abby' not in users:
    print("Abby is not presnt in the Users list")
else:
    print('Abby is present in the Users list')#Result



 #7. BitWise Operators     
     #(a). AND [ & ]
     #(b). OR  [ | ]
     #(c). XOR [ ^ ]
     #(d). NOT [ ! ] 

     # -> Used to compare (binary) numbers