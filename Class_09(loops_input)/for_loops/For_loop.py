# end method
# a="Iqra"
# b="Jahangir"
# print(a,end=" ")
# print(b)

# sept Method
# a="Iqra"
# b="Jahangir"
# print(a,b, sep=" ")

# date=int(input("Date "))

# month=int(input("Month "))

# year=int(input("year "))

# print(date,month,year,sep="/")

# Example
# fruits=["Mango","Banana","Apple","Orange"]
# for fruit in fruits: 
#     if fruit == "Orange":
#         print("Orange is available")
#         break
#     elif fruit == "Apple":
#         print("Apple out of stock")
#         continue
#     elif fruit == "Mango":
#         print("Mango out of stock")
#         continue
#     elif fruit == "Banana": 
#         print("Banana Out Of stock")
#         continue

# Example 
# list=[1,2,3,4,5,6,7,8,9,10]
for num in range(50):
    if num%2==1:
        print(num,"odd Number")



# Break Statment
# With the break statement we can stop the loop before it has looped through all the items:
# Example
# Exit the loop when colors is "purple":

# colors=['Black','White','Brown','Purple','Orange']
# for c in colors:
#     print(c)
#     if c == 'Purple':
#         break

# Example
# Exit the loop when c is list, but this time the break comes before the print:

# colors=['Black','White','Brown','Purple','Orange']
# for c in colors:
#     if c == 'Purple':
#         break
#     print(c)

# 19-March-2024
# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
# Print each adjective for every name:

# name=['Iqra','Fatima','Uzma','Kishwar','Kosar']
# father=['Jahangir']
# for n in name:
#     for f in father:
#         print (n,f)

# i=int(input("Print Table "))
# for j in range(1,11):
#     print(i,"X",j,"=",i*j)