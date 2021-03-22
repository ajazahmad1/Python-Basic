# Looping statement is a control statement which keeps on executing a single statement of block of statement N times till the condition is true.
# Every looping statement has three part.
# initialization
# condition
# increment/decreament

#Q1. Write a program to find 1 to n.

'''n = int(input("Enter a number which you want to print:"))
i = 1
while i<=n:
    print(i)
    i=i+1 

#Q2. Write a program to find sum of 1 to n.

n = int(input("Enter a number :"))
i = 1
sum = 0
while i<=n:
    sum=sum+i
    i=i+1

print("Sum = ",sum) 

#Q3. write a program to 10 to 1 in reverse order
i = 10
while i>=1:
    print(i)
    i=i-1   

#Q4. write a program to print sum of Square from 1 to n

n = int(input("Enter a number"))
i = 1
sum = 0
while i<=n:
    sum = sum+(i*i)
    i=i+1
print("Sum of square",sum)

#Q5. write a program to print only even number from 1 to n

n = int(input("Enter  a number :"))
i = 1
while i<=n:
    if i%2==0:
        print(i)
    i=i+1
# Q6.
n = int(input("Enter  a number :"))
i = 1
sum = 0
while i<=n:
    if i%2==0:
        sum = sum+i
    i=i+1 
print("Sum of even number:",sum) 

#Q6. write a program to find sum of first n even number.

n = int(input("Enter  a number :"))
i = 1
sum = 0
count = 1
while count<=n:
    if i%2==0:
        sum = sum+i
        count = count+1
    i=i+1 

print("sum of even number:",sum) 

#Q7. write a program to find sum of digit of given number.

n = int(input("Enter a number:"))
sum = 0
while n>0:
    sum = sum+(n%10)
    n=n//10
print("Sum of digit of given Number",sum)

#Q8. Write a program to find product of given number.
n = int(input("Enter a number:"))
prod = 1
while n>0:
    prod = prod*(n%10)
    n=n//10
print("product of given Number",prod)

#Q9

n = int(input("Enter a number:"))
sum = 0
while n>0:
    sum = sum+(n%10)*(n%10)
    n=n//10
print("Sum of square of given Number",sum)

#Q10. WRITE A PROGRAM TO CHECK WHEATHER A GIVEN NUMBER IS ARMSTRONG OR NOT

n = int(input("Enter a number:"))
orignal = n
sum = 0
while n>0:
    sum = sum+(n%10)*(n%10)*(n%10)
    n=n//10
if orignal == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

#Q11.REVERSE OF THE NUMBER
n = int(input("Enter a number:"))
rev = 0
while n>0:
    rev = (rev*10)+(n%10)
    n=n//10
print("Reverse of a number",rev)

#Q12. PALINDROM OR NOT like 525 reverse 525

n = int(input("Enter a number:"))
orignal = n
rev = 0
while n>0:
    rev = (rev*10)+(n%10)
    n=n//10
if orignal == rev:
    print("Palindrom number")
else:
    print("Not Palindrom number")

#Q13 Factorial of given number like 5 = 5*4*3*2*1

n = int(input("Enter a number:"))
fac = 1
while n>0:
    fac = fac*n
    n = n-1
print("Factorial of given number is ",fac)   

#Q14. FIBBONACCI SERIES

n = int(input("Enter a number:"))
x = 0
y = 1
z = 0
while z<=n:
    print(z)
    x=y
    y=z
    z=x+y '''