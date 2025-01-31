# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# If statement:
# # 1.Example  with Grater then 
# x= 50
# if x >45:
#     print("Yes your given value is greater than",)
# else:
#     print("Sorry your given value is not greater than")
# # 2. Example 2
# name=input("Enter your first Name")
# if name =="Iqra Jahangir":
#     print("welcome Iqra")
# else:
#     print("Sorry your first name is not match")
# 3.Example

# a=input("Enter your value")
# b=int(a)
# if b == 20:
#     print("a equal is 20")
# else:
#     print("wrong")
# 4.Example


# Practice with Logical Operator
# 1.and
# 2.Or
# 3. not

# 1.Example with and
# firstname=input("Enter Your First Name ")
# lastname=input("Enter Your Last Name ")

# if  firstname=="Muhammad" and lastname== "Huzaifa":
#     print("Welcome",firstname,lastname)
# elif firstname !="Muhammad" and lastname=="Huzaifa":
#     print("Your First Name is not Correct")
# elif firstname =="Muhammad" and lastname!="Huzaifa":
#     print("your last name is not correct")
# else:
#  print("Your name is not match")

# UserName=str(input("Please Enter Your User Name "))
# Password=int(input("Please Enter Your Password "))

# if UserName=="Iqrasheikh" and Password==5567:
#     print("Log in")
# else:
#     print("Login Failed")

# 2.Or
# firstname=input("Enter Your First Name ")
# lastname=input("Enter Your Last Name ")
# if  firstname=="Muhammad" or lastname== "Huzaifa":
#     print("Welcome",firstname,lastname)
# else:
#  print("Your name is not match")

# Take input from the user finf is it even or odd
# num=int(input("Ener your number "))
# if num%2==0:
#       print("Even Number")
# else:
#     print("Odd Number")

# Percentage
math=int(input("Enter Your Maths marks "))
english=int(input("Enter Your English marks "))
urdu=int(input("Enter Your urdu marks "))
total=((math+english+urdu)*100)/300
# print("Your Percentage is",total)

# Result
if total>=90 and 100:
    print(" Your Percentage is",total,"\n","Your Grade is A++")
elif total>=80 and 89:
    print(" Your Percentage is",total,"\n","Your Grade is A+")
elif total>=70 and 79:
    print(" Your Percentage is",total,"\n","Your Grade A")
elif total>=60 and 69:
    print(" Your Percentage is",total,"\n","Your Grade is B")
elif total>=50 and 59:
    print(" Your Percentage is",total,"\n","Your Grade is C")
elif total>=40 and 49:
    print(" Your Percentage is",total,"\n","your Grade is D")
elif total<=39:
    print(" Your Percentage less then 40",total,"\n","Sorry you are fail")
else:
    print(" Sorry your grade is not found")

# Vowels are: a, e, i, o, u . Consonants are the rest of the letters in the alphabet: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y and z .

# Checking Vowels and Consonants
# v=str(input("Please Enter Your Value "))
# if v == "a" or v=="e" or v=="i" or v=="o" or v=="u":
#     print("Your given Alphabet is Vowel ")
# else:
#     print("Your given Alphabet is Consonant ")

