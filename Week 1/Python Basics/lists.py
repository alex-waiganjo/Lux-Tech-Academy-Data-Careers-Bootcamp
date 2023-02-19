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