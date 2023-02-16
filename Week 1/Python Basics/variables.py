#Global Variables
lang = 'python'
def show_lang():
    return f'I love {lang}'
print(show_lang()) #Global Variable

print(f'I love coding in {lang}') #Global variable since it is accessible from anywhere

#Using the Global Keyword
def day():
    global fav_day
    fav_day = 'Monday'
    return f'{fav_day} is my Favorite Day of the Week'
print(day())
print(f'I hate all {fav_day}`s')


#Local Variables
def show_name():
    my_name= 'Alex'
    return f'{my_name} is a Coder'

print(show_name())
#print(f'{my_name} is a Programmer') # Unable to print my_name variable since it cannot be accessed outside the function hence it is a local variable


#Variables and DataTypes

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

#Numeric DataTypes
'''
Int,Float,Complex
'''
salary = 100000    # int
price = 289.0  # float
z = 1j   # complex


# print(salary)
print(type(salary))
print(type(price))
print(type(z))

#Conversions
#From int to float
print(salary) #Int
decimal = float(salary) + float(salary)
print(decimal) #Float

reverse = int(decimal)
print(reverse) #Int



x=90
y=30
name='Alex'
age=None
is_single =True

add =x+y
print(add) #120
conv  = str(add) #'120'
print(conv)
# added = add+conv
#print(added) #Prints a TypeError since int and str are not of the same type

#Get type of variable
print(type(add))  # <class 'int'>
print(type(is_single)) # <class 'bool'>
print(type(age))  # <class 'NoneType'>
print(type(name)) # <class 'str'>


#Techniques of naming Variables

#Snake case
first_name = 'Alex'
last_name ='Waiganjo'

#Pascal Case
FirstName = 'John'
LastName = 'Kamau'

#Camel Case
firstName = 'Joel'
lastName = 'Edwin'


#Assigning many values to variables
day_1,day_2,day_3,day_4,day_5,day_6,day_7 = 'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'
print(day_7,day_6,day_5,day_4,day_3,day_2,day_1)

#Unpack a collection of values in a list,tuple
Clothing = ['Shoes','Trousers','Jackets','Belt','Scarf']
loafer , jeans, xUk,Maasai,green_scarf = Clothing

print(loafer) #  Prints Shoes
print(jeans) # Prints Trousers
print(xUk) # Prints Jacket
print(green_scarf) #  Prints Scarf
print(Maasai) #Prints Belt


# Differnce between Lists,Tuples,Dictionaries,Sets

#Tuple
course = ('IT','Comp Science','Comp Technology','SE')
print(course[0],course[1],course[2],course[3])
print(type(course))


#Set
names = {'James','Philip','Ken','Chris'}
print(names)
print(type(names))


#Dictionary
langs = {"frontend":"Js","backend":"Python"}
print(langs['frontend'],langs['backend'])
print(type(langs))


#List
location = ['Nairobi','Nakuru','Kisumu','Mombasa']
print(location[0],location[2],location[3],location[1])
print(type(location))


# Generating Random Numbers
import random
generate_random_number = random.randrange(1,100) #Generates a single random no eg,17,75
show_random_number = random.randrange(1,4)
print(show_random_number)
print(generate_random_number)


#Casting
#Casting is done using Python constaructor functions // Similar to converting variables to other datatypes
added = 3 +40 #43

print(type(added)) #Int

print(float(added)) #Float

print(str(added)) #String


#Strings
doc = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(doc)
print(type(doc)) #str

message = 'Learning Python Programming Language'
print(message[2],message[7],message[8],message[9]) #r ,g ,empty space,P
print(len(message)) # 36 Characters
for data in message:
    print(data) #Learning Python Programming Language(Vertically)


#Check String
if 'Python' in message:
    print('Python is present in the string  message') #True
else:
    print('Python is not present in the string msessage')    

print('good' in message) #False
print('good' not in message) #True


#Slicing Strings
sliced = message[2:7] #Skip the start and end of the letters/values to be sliced  #arnin
print(sliced) #arnin

sliced_1 = message[:5] #Skip the  value ofelement indicated to slice upto 
print(sliced_1)  #Learn

sliced_2 = message[4:] #Starts from the value index of the 4th element till the end 
print(sliced_2) #ning Python Programming Language

sliced_3 = message[-5:-3] #Include the 5th elemnt from the right and while ommitimg the 3rd element from the right
print(sliced_3) #gu


#Modifying Strings
review= 'I like the Product '
print(review.upper()) #I LIKE THE PRODUCT
print(review.lower()) #i like the product
print(review.strip()) #Removes the whitespaces at the start or the end of the string


#Replacing Strings
print(review.replace('like','dislike')) #I dislike the Product
print(review.replace('I','We')) #We like the Product


#Split
print(review.split('li')) #['I ', 'ke the Product ']


#String Concatenation
Movie_1 = 'Hannah'
review_1 = ' is a Thriller Movie'
review_2 = 'is a Good movie'
view = Movie_1 + review_1
view_2 = Movie_1 + " " + review_2
print(view)
print(view_2)


#Formating Strings
hobby = 'Coding'
say = 'I love {}'
print(say.format(hobby))

product = 'Book'
price_2 = 200
day = 'Monday'
print('I bought a {} that costs Ksh{} on {}'.format(product,price_2,day))


#Escape Characters
team_1 = 'We are Manchester United and We are the \'reds\' ' #\' or \" is used to print the quotation symbol
team_2 = 'We are \\Chelsea,\n the Blues' #Prints the blues on a new line
print(team_1)
print(team_2)



#Boolean DataTypes
#Often are True or False

print(90>3) # Returns True
print(90<3) # Returns False
print(90==90) #Returns True
print(90=='90') # Returns False
print(90==30) #False

print(bool('hello')) #True
print(bool(355)) #True

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))# False


#Functions using Booleans ,Example 1
#Part 1
def name():
    return True
print(name()) #True

#Part 2 
# def name():
#     return False
# print(name()) #False

if name():
    print("The name function has a Bool of type True ") #Prints part 1 of the name function since it is of type  True
else:
    print("The name function has a bool of type False ")  #Prints this line once you Uncomment  part 2 of the name function since it is of type False  


#Functions using Booleans ,Example 2
def register(is_logged_in:bool):      
    if is_logged_in == True:
        return 'Logged In'  
    return "Not logged In"    

print(register(is_logged_in=False)) #Not logged In
print(register(is_logged_in=True)) #Logged In