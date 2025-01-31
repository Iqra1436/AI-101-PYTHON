# 1st Topic Zip Function
# list=[2,3,1,4,5,6,7,8,9,10]
# list2=[9,8,7,6,5,4,3,2,1,2]
# for i,q in zip(list,list2):
#     print(f" list 1 {i} \n list 2 {q}")

# Task 
# list=[]
# # create input 
# i=int(input("Create list "))
# # using for loop 
# for i in range(0,i):
#     add=int(input("Add list "))
# # use append for add value in list
#     list.append(add)
# print("your list is created ","=",list)

# 2nd Topic
# List Comprehension
# l=[x for x in range(0,5)]
# print(l)

# with user input
# user=input("Create list in one line on command prompt ")
# l=[(x) for x in user.split()]
# print(l)


# list=[1,2,3,4,5,6,7,8,9,10]
# print("1.Even Number\n2.Odd Number")
# num=int(input("Enter your number "))
# def even():
#     for num in list:
#         if num%2==0:
#             print(num,"Even Number")
# def odd():
#     for num in list:
#         if num%2==1:
#             print(num,"odd")
# match num:
#     case 1:
#         even()
#     case 2:
#         odd()
# Practice
# l=[]
# i=int(input("Create list "))
# for i in range(0,i):
#     ad=int(input("Add list "))
#     l.append(ad)
# print("your list is created ","=",l)




# list=[1,2,3,4,5,6,7,8,9,10]
# for num in list:
#     if num%2==0:
#         print(num,"Even Number")


# List method
# 1) Append
name =["Iqra","Razia"]
name.append("Uzma") # addd last value from list 
print(name) 
# 2) Remove
num =[2,4,5,6,7,8]
print(f"{num} List before using Remove function")
num.remove(6)
print(f"{num}  list after remove index 6")
# # 3) pop
pops=["Iqra","Fatima","Uzma"]
pops.pop() # remove last value from list

# 4) del
d=[12,34,54,77,78]
del d[3]
print(d)

# 5) reverse
R=[12,34,54,77,78]
R.reverse()
print(R)

# 6)sort
S=[12,11,45,10,5]
S.sort()
print(S)

# 7)Extend
S.extend(R)
print(S)


