# String :- string is sequence of character which enclosed with quotes.

name = "mukesh"

# slicing of string

print(name[0])
print(name[2])
print(name[-2])

print(name[0:])
print(name[:10])
print(name[1:4])
print(name[-4:])

# String Function
name = "ajaz Ahmad"
print(len(name))
print(name.endswith("ad"))
print(name.count("a"))
print(name.capitalize())
print(name.find("Ahmad"))
print(name.find("m")) # it return index number
print(name.replace("Ahmad","Khan"))

print("--------------------------------------")

'''List:-list are container to store
   a set of value of any data type'''

li = ["Hello",23.1,56,False,3+4j]
print(li[0]) # list indexing just like string
print(li[-1])
print(li[2])

print("-----List Methods-------")
lis = [1,8,7,2,11,15]
lis.sort() 
print(lis)
lis.reverse()
print(lis)
lis.append(100) # add last in the list
print(lis)
lis.insert(3,200) # add 200 at three index
print(lis)
lis.pop(3) # delete element at index 3 and return its value
print(lis)
lis.remove(15) # will remove 15 from the list
print(lis)

print('----Tuples in python--------' )

# A tuple is an immutable data type means it can not change
# once defined a tuple element can not be change or manipulated
tup = (7,3,10,7,"hello",False,23.5)
print(tup)
print(tup[0]) # indexing of the tuple
print(tup[2])
print(tup[-1])
print('---Tuples methods-----'  )
new_tuple = tup.count(7)
print(new_tuple)
x = tup.index(10)
print(x)
print("---Update tuple----")

x = ("banana","apple","orange")
y = list(x)
y.append("kiwi")
x = tuple(y)
print(x)

print('-----Dictionary--------')

dic = {"Name":"Ajaz Ahmad","Roll":174030,"From":"India","Marks":[92,78,81,67]}
print(dic)
dic.items()
print(dic)

x = dic.keys()
print(x)

y = dic.values()
print(y)

dic.update({"Dept":"CSE"})
print(dic)
dic.pop("Dept")
print(dic)
# first method
x = dic.get("Name")
print(x)
#Second Method
print(dic["Name"])
# length of dictionary
print(len(dic))


print("---------- Set-------------")

s = {1,8,2,3,7,"hello",True,34.2}
print(s)
print(len(s))
s.remove(8)
print(s)
s.pop()
print(s)
s.clear()
print(s)
s.add(1)
s.add(2)
print(s)
print("-----Union-------")
x = {"apple","banana","orange"}
y = {"microsoft","google","apple","google"}
z = x.union(y) # it return both value for duplicate is not excepted
print(z)

print("-------------------------------------")
# using set constructor to make a set

# x = ("apple","banana","kiwi","orange") first method

set_constructor = set(("apple","banana","kiwi","orange"))#second method
print(set_constructor)
