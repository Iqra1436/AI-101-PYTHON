# While Loop
# There are three types of while loops
# 1-initiali
# 2-condition
# 3-increment

# Example.01
# i=0
# while i<=10:
#     print(i)
#     i+=1
# Example.02
# d=20
# while d>=0:
#     print(d)
#     d-=1

# while(let i=1; i <=10; i++){
#     let num =5;
#     let sum =5*i
#     print(num +" X " + i + " = " + sum)
# }
    # Example.3
# num=int(input("Enter Your Value "))
# i=1
# while i <=10:
#     sum=i*num
#     print(num, "X" , i, "=", sum)
#     i+=1

# rows=int(input("Enter your value "))
# i=1
# while i<10:
#     print("*"*i)
#     i+=1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

# Example 01
# Exit the loop when i is 3:

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# Example.02
# i=input("input number ")
# i=0
# while i<=20:
#     if i==6:
#         print("break")
#         break
#     i+=1
#     if i==6:
#         print("continue")
#         continue
#     print(i)

# # The continue Statement
# Continue to the next iteration if i is 3:

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# 15-March-2024
# Number=20
# while True:
#     GuessNumber =int(input("Enter Number "))
#     if GuessNumber == Number:
#         print("Your number euqual to",Number)
#         break
#     elif GuessNumber >= Number:
#         print("Your Guess Number Greater then", Number)
#         continue
#     elif GuessNumber <=Number:
#         print("Your Guess Number Less then", Number)
# #         continue


# names =("Iqra","Fatima","Uzma","Kishwar","Kosar")

# a = "Fatima"
# b=  "Kishwar"
# i = 0
# while i < len(names):
#     if (names[i] == a):
#         print(f"student {a} found in index no {i}")
#     elif (names[i] == b):
#         print(F"student{b} found in index no {i}")
#     else:
#         print(names)
#     i+=1


# print odd number
# num = 1
# while  num <= 20 :
#     if num % 2 ==0:
#       print(num, "Even Number", end="\n")
#     num += 1
    
# print even number
# num = 1
# while num <= 20:
#   if num % 2 !=0:
#         print(num,"Odd Number", end="\n")
#     num += 1


# Write a program where the user has to guess a predefined number (e.g., 7). Keep asking for guesses until they get it right.

# Guess the Number Game

# num = 7
# while True:
#     user = int(input("Please Guess Number "))
#     if user == num:
#         print("Congratulation You Guess Right Number", num)
#         user+=1
#         break
#     else:
#         print("Sorry, You Guess Wrong")
   
# Even Numbers:
# Use a while loop to print all even numbers between 1 and 20.

# Solve
# while True:
#     user = int(input("All even & odd numbers between 1 and 20 "))
#     if user % 2 == 0:
#         print(user, "Even Numbers")
#     if user % 2 != 0:
#         print(user, "Odd Number")
#     user += 1

# Solve
# while True:
#     user = int(input("Even numbers between 1 and 20 "))
#     if user % 2 != 0:
#         print("Even Number",user)
#         break
#     user+=1

# Multiplication Table:
# Write a program to print the multiplication table of a number provided by the user using a while loop



# table = int(input("Enter your favourite table "))
# num = 1
# while num <= 10:
#     print(f"{table} X {num} = {table * num}")
#     num +=1

# Even Numbers:
# Use a while loop to print all even numbers between 1 and 20.

# num = 1
# while num <= 20:
#     if num % 2 == 0 :
#         print(f"{num}")
#     num += 1

# Use a while loop to print all reverse even numbers between 20 and 1
# num = 20 
# while num >= 1:
#     if num % 2 == 0:
#         print(f"{num}")
#     num -= 1

# Use a while loop to print all odd numbers between 1 and 20
# num = 1
# while num <= 20:
#     if num % 2 != 0:
#         print(f"{num}")
#     num += 1

# Use a while loop to print all reverse odd numbers between 20 and 1

# num = 20 
# while num >= 1:
#     if num % 2 != 0:
#         print(f"{num}")
#     num -= 1

# choice=input("1.While Loop \n2.For Loop \n")
# if choice== '1':
#      num=int(input("Print Table with While Loop "))
#      i=1
#      while i<=10:
#         print(num,"X",i,"=",num*i)
#         i+=1
# elif choice=='2':
#     num=int(input("Print Table with For Loop "))
#     for f in range(1,11):
#         print(num,"X",f,"=",num*f)