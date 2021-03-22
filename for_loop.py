#Q1. write a program to print 1 to 10 using foor loop and while loop.
# using foor loop
'''for i in range(1,11,1): #first starting point second end point and third step point
    print(i)

# using while loop.
i = 1
while i<=10:
    print(i)
    i = i+1 

#Q2. write a program to find 10 to 1 using for loop.
for i in  range(10,1,-1):
    print(i) 

#Q3. Write a program to print table of given number.

x = int(input("Enter number to find table:"))
for y in range(1,11):
    print(x,"*",y,"=",(x*y))

# using while loop
x = int(input("Enter a number:"))
y = 1
while y<=10:
    print(x,"*",y,"=",(x*y))
    y = y+1 

# Nested loop
i = 1
while i<=5:
    j = 1
    while j<=i:
        print("*",end="")
        j=j+1
    print()    
    i=i+1    

i = 1
while i<=5:
    j = 1
    while j<=i:
        print(j,end="")
        j=j+1
    print()    
    i=i+1 


i = 1
while i<=5:
    j = 1
    while j<=i:
        print(i,end="")
        j=j+1
    print()    
    i=i+1


i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1          


i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1 

i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    print()
    i=i+1  

k = 1
i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=k:
        print("*",end="")
        j=j+1
    print()
    k=k+2
    i=i+1 

k = 1
i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=k:
        print(j,end="")
        j=j+1
    print()
    k=k+2
    i=i+1

k = 1
i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=k:
        print(i,end="")
        j=j+1
    print()
    k=k+2
    i=i+1                             


k = 1
i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=k:
        print(k,end="")
        j=j+1
    print()
    k=k+2
    i=i+1 ''' 

n = int(input("Enter number of rows:"))
i = 1
while n>0:
    b = 1
    while b<i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=(n*2)-1:
        print("*",end="")
        j=j+1
    print()
    n=n-1
    i=i+1            


