a=int(input("Enter First Value "))
b=int(input("Enter Secong Value "))

try: 
    print (a/b)
except ValueError as v:
    print("Value Error", v)
except ZeroDivisionError as z:
    print("ZeroDivisionError",z)
else:
    print("Error")
finally:
    print("End")

#  Pracice with Dictionary
d={1:"Iqra",2:"karachi"}
try:
    x=int(input("Key enter "))
    print(d[x])
except KeyError as k:
    print(k,"key error")
except ValueError as i:
    print("Value error ")

#raise
name=str(input("Enter Your Name "))
age=int(input("Enter Your Numer "))
if name == "huzaifa" and age == 18:
    raise Exception("Welcome Huzaifa")
print("Failed")


# SyntaxError
# try:
#     print("Hello)
# except SyntaxError as e:
#     print(e)
# TypeError
# try:
#     a="10"
#     b=10
#     print(a+b)
# except TypeError as c:
#     print("Type Error ",c)
# ValueError
# try:
#     name=int("iqra")
#     print(name)
# except Exception as n:
#     print(n)
# IndexError
# l=[1,2,3]
# print(l[4])
# KeyError:
# d={"name":"Iqra"}
# print(d["age"])
# NameError:
# myName="Iqra"
# print(age)
# AttributeError
# message="welcome"
# print(message.capital())
# ZeroDivisionError
# print(5/0)
# MemoryError
# m=[10]*1000000000
# print(m)
# ModuleNotFoundError:
# import ab


