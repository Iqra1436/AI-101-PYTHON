# 1. String (str) (text)

name = "Iqra Jahangir"
print(name) # print
print(type(name)) # type
print(id(name)) # physical address
# print(dir(name)) 
# print([i for i in dir(name) if "__" not in i ]) # methods & attributes

# 2.  Int (Number)

num : int = 100
print(num) # print
print(type(num)) # type 
print(id(num)) # physical address
# print(dir(num)) 
# print([i for i in dir(name) if "__" not in i ]) # methods & attributes

# 3. Float (Decimal Number)

f : float = 2.5
print(f) # print
print(type(f)) # type
print(id(f)) # physical address
# print(dir(f)) 
# print([i for i in dir(name) if "__" not in i ]) # methods cls
# & attributes

# 4. Boolean (Bool) (True , False)

b : bool = True
print(b) # print
print(type(b)) # type
# print(dir(b)) 
# print([i for i in dir(name) if "__" not in i ]) # methods & attributes

# 5.List

l : list[str] = ["Iqra", "Jahangir"]
print(l) # print
print(type(l)) # type
# print(dir(l)) 
# print([i for i in dir(name) if "__" not in i ]) # methods & attributes

# 6. Tupple

tup : tuple[str,int,float] = ("a",34,2.5)
print(tup) # print
print(type(tup)) # type
# print(dir(tup)) 
# print([i for i in dir(name) if "__" not in i ]) # methods & attributesh




# DATA TYPES OF PYHTON 
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# 1.Text Type:	str
# 2.Numeric Types:	int, float, complex
# 3.Sequence Types:	list, tuple, range
# 4.Mapping Type:	dict
# 5.Set Types:	set, frozenset
# 6.Boolean Type:	bool
# 7.Binary Types:	bytes, bytearray, memoryview
# 8.None Type:	NoneType


# Getting the Data Type
# You can get the data type of any object by using the type() function:
# Example
# Print the data type of the variable x:
# x = 5
# print(type(x))

# 1. Text Type:
# a) str
# var2 = "double" 
# var3 = 'Single'
# print('\n hello I am string with ', var2, ' couts')
# print('\n hello I am string with ',var3, 'couts')


# 2. Numeric Types:	
# a)int
# var1 = 3847
# print('\nhello I am integer', var1)
# print(type(var1))

# b)float 
# var6 = 66.6
# print('\n','hello I am float with', var6)
# print(type(var6))

# c)complex  
# x = 1j
# print('\n','hello I am complex with',x)
# print(type(x))

# 3.Sequence Types:
# a. list(Emuted = Changeable)
# list1 = ["String with double cots",'String with Single cots',"'String with Single cots'",1010,True,False,99.9]
# print("this is list",list1)
# print(type(list1))

 # b. tuple(muted = Unchangeable)
# Tup = ("String with double cots",'String with Single cots',1010,True,False,99.9)
# print("this is tuple",Tup)
# print(type(Tup))

# c.range
# x = range(10)
# print("This is range",x)
# print(type(x)) 

# 4. Mapping Type:	
# a.dictionary
# (keys and value pairs like an object)
# dict = {1:55,2:45,3:35,4:66}
# print("this is dict",dict)
# print(type(dict)) 

# 5.Set Types:
# a.set
# sett = {"apple", "banana", "cherry"}
# print("this is set",sett)
# print(type(sett)) 

# b.frozenset
# x = frozenset({"apple", "banana", "cherry"})
# print("this is frozenset",x)
# print(type(x)) 

# 6.Boolean Type:	
# var4 = True
# var5 = False
# print('\nhello I am boolean with ', var4)
# print(type(var4))
# print('hello I am boolean with', var5)
# print(type(var5)) 

# 7.Binary Types:
# a.bytes
# y = bytes(6)
# print('Example with',y,type(y))

# b.bytearray
# x = bytearray(5)
# print('Example with',x,type(x))

# c.memoryview
# x = memoryview(bytes(5))
# print('Example with',x,type(x))



# Collection Data type
# 1.List
# 2.tuple
# 3.sets
# 4.Dictionary

# 1.List
# Mylist=[5,6,7,"Double quotes","Single quotes"]
# print(Mylist)
# # # 2.tuple
# tp=(5,6,7,"Double quotes","Single quotes")
# print(tp)
# # # 3.sets
# set={10,20,25,15,25,30,10}
# print(set)
# # 4.Dictionary
# dic={1:"2.3",2:"44"}
# print(dic)


# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

# x = 1    # int
# #convert from int to float:
# a = float(x)
# print(a,type(a))

# y = 2.8  # float
# #convert from float to int:
# b = int(y)
# print(b,type(b))

# z = 1j   # complex
# #convert from int to complex:
# c = complex(x)
# print(c,type(c))

# Example 1 (int convert in float)
# a=32   
# print("Check type of",a,type(a))
# b=float(a)
# print("32 convert in float",b)
# # Example 2 (float convert in int)
# c=3.2
# print("Check type of",c,type(c))
# d=int(c)
# print("Float convert in int",d)
# # Example 3 (list Convert in set)
# I=[3,5,10,5,2.5]
# print("Check type of",I,type(I))
# J=set(I)
# print("list Convert in set",J)
# # Example 4 (List convert in tople)
# k=[3,5,10,5,2.5]
# print("Check type of",k,type(k))
# L=tuple(k)
# print("List convert in tople =",L)
# # Example 4 (tuple convert in list)
# m=(3,5,10,5,2.5)
# print("Check type of",m,type(m))
# n=list(m)
# print("tuple convert in list =",n)
# # Example 5 (Set convert in list)
# o={3,5,10,5,2.5}
# print("Check type of",o,type(o))
# p=list(o)
# print("set convert in list =",p)

# list 
# name=[5,4.5,"Iqra"]
# name[2]=23
# name[0]="fatima"
# print(name)

# Ditionary
# Ditionary={
#     "FirstName":"Sheikh",
#     "MiddleName":"Muhammad",
#     "LastName":"Jahangir"}
# print (Ditionary["FirstName"],Ditionary["MiddleName"],Ditionary["LastName"])

# change value
# Ditionary["FirstName"]="syed"
# print (Ditionary["FirstName"],Ditionary["MiddleName"],Ditionary["LastName"])



name=" Iqra Jahangir "
message="Hello! world"
# list=[2,4,5,6,7]
# print(name.split())
# print(len(list))
# print(name.upper())
# print(message.lower())
# print(name.capitalize())
# print(name.count('Iqra'))
# print(name.find("h"))
# print(message.replace("world","Universe"))
# print(message.endswith("!"))
# print(name.startswith(" "))

# city="Karachi"
# print(name.center(50))
# print(f"My name is {name} \n I'm from {message}")


# Days=str(input("Choose Days "))
# match Days:
#     case "Monday":
#         print(f"Today's {Days}")
#     case "Tuesday":
#         print("Today's Tuesday")
#     case "Wednesday":
#         print("Today's Wednesday")
#     case "Thursday":
#         print("Today's Thursday")
#     case "Friday":
#         print("Today's Friday")
#     case "Saturday":
#         print("Today's Saturday")
#     case "Sunday":
#         print("Today's Sunday")
#     case _:
#         print("Invalid")


# Days=str(input("Enter Days Name "))
# s="Today's is "
# match Days:
#         case "Monday":
#              print(s,"Monday")
#         case "Tuesday":
#             print(s,"Tuesday")
#         case "Wednesday":
#             print(s,"Wednesday")
#         case "Thursday":
#             print(s,"Thursday")
#         case "Friday":
#             print (s,"Friday")
#         case "Saturday":
#             print (s,"Saturday")
#         case "Sunday":
#             print(s,"Sunday")
#         case _:
#             print("Invalid Day")