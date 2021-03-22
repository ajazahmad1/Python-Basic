# function :- A function is block of code and piece of code you can use it by calling function.
# Two main part of the function is 
# (1) Function definition
# (2) Function calling

'''def message():
     print("Hello Function")

message() # calling function

message()

# Program to find addition of two number using function

def add():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = a+b
    print("Addition",c)

add()

# Argument/Parameter :- This is the value which is supplied to the function to operate on.

def add(a,b):
    c = a+b
    print("Addition",c)

add(8,7) 

def add(a,b):
    c = a+b
    print("Addition",c)

x = int(input("Enter first number"))
y = int(input("Enter second number"))
add(x,y)

# return:- which we take from function
# argument:- we give to function

# Find a number a odd and even using function.

def odd_even(a):
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number") 

odd_even(6)

# Program no argument no return value.

def odd_even():
    a = int(input("Enter a number to check:"))
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number")

odd_even()

# Program With argument no return value

def odd_even(a):
    
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number")

x = int(input("Enter a number:"))
odd_even(x)  

# Program no argument with return value

def add():
    a = int(input("Enter a number to check:"))
    b = int(input("Enter second number"))
    c = a+b
    return c

z= add() 
print("Addition",z)

# Program with argument with return value.
# First method

def add(a,b):
    c = a+b
    return c

z = add(45,55) 
print("Addition",z)

# Second method

def add(a,b):
    c = a+b
    return c

x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = add(x,y) 
print("Addition",z)


# Default argument

def add(a,b,c=5):
     d = a+b+c
     print("Addition",d)

add(10,8,7)

###################

def add(a=20,b=10,c=30):
     d = a+b+c
     print("Addition",d)

add(10,5,5)

######################

def add(a,b=6,c=4):
     d = a+b+c
     print("Addition",d)

add(10)'''

######################

def add(a,b,c=5):
     d = a+b+c
     print("Addition",d)

add(10,50)
        

