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