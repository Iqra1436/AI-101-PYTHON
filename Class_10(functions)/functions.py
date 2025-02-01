# Example 01
# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
# Example 2
# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
# Example 03
# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Example 04
# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# Example 05
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Exampla 06
# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

# Example 07
# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
# Example 08
# Return Values
# To let a function return a value, use the return statement:
# Example 09
# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.


# Example 01
def my_01(fname):
    print(fname + "Jahangir")
my_01("Iqra ")
my_01("Fatima ")
my_01("Uzma ")
my_01("Kishwar ")
my_01("Kosar ")
# Example 02
def my_02(firstname,lastname):
    print(firstname + "Daughter of " + lastname)
my_02("Iqra "," Jahangir")
# Example 03
def my_03(*kids):
    print("the yougest child is " + kids[2])
my_03("Iqra","Fatime","Uzma","kishwar")
# Example 04
def my_04(stud1,stud2,stud3,stud4):
    print("the yougest student is " + stud2)
my_04(stud1="Zara",stud2="Abbas",stud3="Enaya",stud4="Umar")
# Example 05
def my_function_1(**kid):
    print("her last name is " + kid["lname"])
my_function_1(fname="Iqra",lname="Jahangir")

# Example 06
def my_function(country="Pakistan"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function("Brazil")
my_function()

# Example 07
def my_07(food):
    for x in food:
        print(x)
fruits=["Apple","Banana"]
my_07(fruits)

# Example 08
def my_08(x):
    return 4 / x
print(my_08(2))
print(my_08(4))
print(my_08(5))



# def average():
#     a=int(input("First Number "))
#     b=int(input("Second Number "))
#     c=int(input("Third Number "))
#     print(a+b+c/3)
# average()

# a=int(input("1st Number "))
# b=int(input("2nd Number "))
# # Addition
# def add():
#     print("Addition ",a+b)
# add()
# # Substraction
# def sub():
#     print("subtraction ",a-b)
# sub()
# # Multiplication
# def multiply():
#     print("multiply ",a*b)
# multiply()
# # division
# def division():
#     print("division ",a/b)
# division()








# Addition
def add(a,b):
    print("Addition ",a+b)
# Substraction
def sub(a,b):
    print("subtraction ",a-b)
# Multiplication
def multiply(a,b):
    print("multiply ",a*b)
# division
def division(a,b):
    print("division ",a/b)