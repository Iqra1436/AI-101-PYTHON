# # Login System
# data_base : list[tuple[str,int]] = [("Iqra",123),
#                                     ("Fatima",345),
#                                     ("Uzima",567)
#                                     ]
# user_input : str = input("Enter Your Name : ")
# password_input : str = input("Enter Your Password : ")

# for row in data_base:
#   user,password = row
#   if user_input == user and password_input == password:
#     print(f" Successfuly Login ")
#     break
#   elif user_input == user and password_input != password:
#     print("Invalid Pasword")
#     break
#   elif user_input != user and password_input == password:
#     print("Invalid User")
#     break
#   else:
#     print("Invalid user and password ")
# else:
#   print("you are not registered pleas sign up first and try again")
  
  
table : str = input("Enter Number for table printing : ")
for i in range(1,11):
  print(f"{table} X {i} = {int(table) * i}")
    