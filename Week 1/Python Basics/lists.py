#Lists 
#Part of Python Arrays
#List items are ordered, changeable, and allow duplicate values.
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created
#Since lists are indexed, lists can have items with the same value

days = ['Sunday','Tuesday','Wednesday','Thursday','Friday']
print(days) #['Sunday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#Adding a new item
days.append('Saturday')
print(days)  #['Sunday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#Adding duplicate values
days.append('Sunday')
print(days) #['Sunday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#Getting the list length
print(len(days)) #7


# A list can contain different data types
items  = ['James',23,'Male',True,'Nairobi']
print(type(items)) #<class 'list'>
print(items) #['James',23,'Male',True,'Nairobi']


#The List Constructor
# It is possible to use the list() constructor when creating a new list
item = list(('love','live'))
print(item)

#Add a new Item
item = list(('love','live','laugh'))
print(item)


#Accessing Items in a List
names = ['James','Ken','Joy','Tracy']
print(names[2]) #Joy
print(names[-2]) #Joy
print(names[-1]) #Tracy
print(names[-0]) #James
print(names[0]) #James
#Range of Indexes
names = ['James','Ken','Joy','Tracy','Rose','Peter','Joseph','Quicny','Lilian']
print(names[2:5]) #['Joy', 'Tracy', 'Rose']
print(names[4:8]) #['Rose', 'Peter', 'Joseph', 'Quicny']
print(names[:8]) # ['James', 'Ken', 'Joy', 'Tracy', 'Rose', 'Peter', 'Joseph', 'Quicny']
print(names[5:]) # ['Peter', 'Joseph', 'Quicny', 'Lilian']


#Check if item exists
if 'Lilian' in names:
    print('Present') #Result
else:
    print("Not Present")   

if 'Alex' in names:
    print('Present')
else:
    print("Not Present") #Result


#Change Item Value
courses = ['IT','Comp Science','Comp Tech']
print(courses) #['IT', 'Comp Science', 'Comp Tech']
courses[1] = 'SE' #Change Comp Science to SE    
print(courses) #['IT', 'SE', 'Comp Tech']

fruits = ['Mango','Apple','Ovacado','Pineapple','Pears']
print(fruits) #['Mango', 'Apple', 'Ovacado', 'Pineapple', 'Pears']
fruits[1:4] = ['Banana','Orange','Kiwi']
print(fruits) #['Mango', 'Banana', 'Orange', 'Kiwi', 'Pears']
fruits[1:2] = ['Watermelon']
print(fruits) #['Mango', 'Watermelon', 'Orange', 'Kiwi', 'Pears']

#Insert Items Using Append Method => Specifies a particular index to insert elements
furniture = ['Chair','Bed','Table','Stool']
print(furniture) #['Chair', 'Bed', 'Table', 'Stool']
furniture.insert(3,'Wardrobe')
print(furniture)  #['Chair', 'Bed', 'Table', 'Wardrobe', 'Stool']
furniture.insert(2,'Spoon')
print(furniture)  #['Chair', 'Bed', 'Spoon', 'Table', 'Wardrobe', 'Stool']

#Adding Items Using the Append Method
furniture.append('Couch') #Adds an item at the end of the list
print(furniture) #['Chair', 'Bed', 'Spoon', 'Table', 'Wardrobe', 'Stool', 'Couch']

#Combining two lists using the extend function
common_units = ['Networking','OS','Programming']
other_units =['AI','Ml']
hard_units = ('IOT','Web3')
common_units.extend(other_units)
print(common_units) # ['Networking', 'OS', 'Programming', 'Ai', 'Ml']
common_units.extend(hard_units)
print(common_units) #['Networking', 'OS', 'Programming', 'AI', 'Ml', 'IOT', 'Web3']


#Remove List Items
print(common_units) #['Networking', 'OS', 'Programming', 'AI', 'Ml', 'IOT', 'Web3']
common_units.remove('Web3')
print(common_units) #['Networking', 'OS', 'Programming', 'AI', 'Ml', 'IOT']

#Remove a Specified Index
common_units.pop(0)
print(common_units) #['OS', 'Programming', 'AI', 'Ml', 'IOT']

#Remove the Last Item
common_units.pop()
print(common_units) #['OS', 'Programming', 'AI', 'Ml']

#Use The Del Keyword to Delete Items
del common_units[0]
print(common_units) #['Programming', 'AI', 'Ml']

# del common_units
# print(common_units) #Items already Deleted


#Using the Clear() to delete the entire List
common_units.clear()
print(common_units) #[]