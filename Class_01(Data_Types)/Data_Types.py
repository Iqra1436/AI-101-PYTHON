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
