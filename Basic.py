# print function is used to print the message and value
print("Hello World")
print("-----------------------------------------")
x = 7
y = 5
print((x*y))
print("-----------------------------------------")
a = 10
b = 20
c = a+b
print("Addition of",a,"and",b,"=",c)
print("-----------------------------------")

name = "Ajaz Ahmad"
print("Welcome",name)
print("-------------------------------------")


# IDENTIFY OPERATORS
#identify operators in python are used to determine 
# whether a value is of a certain class or type

# is : Returns true if both variable are the same object
# is not : Return true if both variable are not the same object 
x = 5
if type(x) is int:
    print("Correct")
else: 
    print("incorrect")  

a = 5.8
if type(a) is not float:
    print("correct") 
else:
    print("Incorrect")  

print("-------------------------------")  

# in : This returns true if the element is found otherwise false
# not in : This return true if the element is not found otherwise true
a = 10
li = [12,45,67,11,27]
if a in li:
    print("Yes a is present in list")
else:
    print("No a is not present in list")    

print("------------------------------------------")  

x = 5
li2 = [13,14,17,18,12]
if x not in li2:
    print("x is not present in list")
else:
    print("x is present in list") 

print("------------------------------------")   

units = int(input("How many units consumed this month :"))
total_price = (5*units)
Discount = (total_price*10)/100
print("After Discount total bill price",Discount)


print("---------------------------------------")

a = int(input("Enter first value "))
b = int(input("Enter second value "))
c = a
a = b
b = c
print("After swaping",a)
print("After swaping",b)
