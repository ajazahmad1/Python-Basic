#lambda function can take any number of arguments but can only have one expression.
# syntax :- lambda arguments : expression

'''x = lambda a:a+10
z = x(5)
print(z)

# A lambda function can take any number of arguments

a = lambda x,y:x+y
print(a(5,5))

# filter function

ages =[12,17,19,24,11,15]

def my_func(x):
    if x>=18:
        return True
    else:
        return False

capable = list(filter(my_func,ages)) 

for x in capable:
    print(x)

# Same program using lambda function
ages =[12,17,19,24,11,15]

xyz =list(filter(lambda a:a>=18,ages))
for x in xyz:
    print(x)

# odd even using lambda function

num =[12,17,19,24,11,15] 

result = filter(lambda a:a%2==0,num)
for x in result:
    print(x)

 #######################################

ages=[12,17,19,24,11,15]

def my_func(x):
    if x>=18:
        return True
    else:
        return False
def my_func1(x):
    return x*x

adult = filter(my_func,ages)
for x in adult:
    print(x)

result = map(my_func1,adult)
for x in result:
    print(x)

#using lambda fuction

ages =[12,17,19,24,11,15]
adult = filter(lambda a: a>18,ages)
square= map(lambda a:a*a,adult)
for x in square:
    print(x)

from functools import reduce

a = [1,2,3,4,5]
add = reduce(lambda a,b:a+b,a)
print(add)

# same program using function
from functools import reduce
a = [1,2,3,4,5]
def myFun(a,b):
    return a+b

add = reduce(myFun,a)
print(add)

# Maximum number of the list
from functools import reduce
li = [10,18,12,26,28]

max = reduce(lambda a,b: a if a>b else b,li)
print("Maximum number is = ",max)'''

# Same program using function
from functools import reduce
li = [1,2,3,4,5]
def func(a,b):
    if a>b:
        return a
    else: 
        return b
max =  reduce(func,li)
print("Maximum",max)            
