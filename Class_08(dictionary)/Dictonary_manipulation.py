# subjects ={
#     "Sub1":"Maths",
#     "Sub2" : "Engish",
# }
# # clear
# # subjects.clear()
# # print(subjects)
# # # copy
# new=subjects.copy()
# print(new)
# # # get
# # gets=subjects.get("Sub1")
# # print(gets)
# # # items
# # n=subjects.items()
# # print(n)
# # keys
# # n = subjects.keys()
# # print(n)
# # # pop
# # n=subjects.popitem()
# # print(n)
# # # update
# # subjects.update({"Sub3":"Pyhton"})
# # print(subjects)
# # # value
# # n=subjects.value()
# # print(n)
# # t=("a",",e","i","o","u","s")
# # v="vowel"
# # di=dict.fromkeys(t,v)
# # print(di)


# ## 2.Assignment
# # Write a program for a login system using a dictionary with different users.
# def login(Users):
#     username=input('Enter Your UserName: ')
#     password=input('Enter Your PassWord: ')

#     if username in Users and Users[username]==password:
#         print('Succesfully Login!')
    
#     else:
#         print('Incorrect User or Password')
# def main():
#     Users = {
#             'Iqra':'2233',
#             'Fatima':'1122',
#             'Uzma' :'4455',
#     }
#     while True:
#         print('\n Welcome to the login system : ')
#         print('1. Login')
        
#         print('2. Exit')
#         choice=input('Please Choice (1 or 2 ): ')
        
#         if choice == '1':
#             login(Users)
#             break
#         elif choice  == '2' :
#             print('Exit ')
#             break
#         else:
#             print('Invalid Choice . Please try again. ')
# if __name__ == "__main__":
#     main()

# Another way 

# Users = {
#             'IqraJahangir':'2233',
#             'FatimaJahangir':'1122',
#             'Uzma' :'4455',
#     }
# while True:
#     username=input('Enter Your UserName: ')
#     password=input('Enter Your PassWord: ')

#     if username in Users and Users[username]==password:
#         print('Succesfully Login!')
#         break
#     else:
#         print('Incorrect User or Password')