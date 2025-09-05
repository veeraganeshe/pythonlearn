def greet_person(name):
  print("Hello " + name)

personExample = {
  "name": "Sandip",
  "age": 20,
  "country": "India"
}#normal module useage example
# print("Normal module useage")
# import custom_module_example
# custom_module_example.greet_person("Sandip")

#Using alias and accessig variable
print("Using alias and accessig variable")
import custom_module_example as cme
a = cme.personExample["age"]
print(a)

# use dir() function to get all the variables and functions
print("Using dir() function to get all the variables and functions of custom_module_example")
import custom_module_example
x = dir(custom_module_example)
print(x)#handling simple error
# print(x)
print("Handling simple error")
try:
  print(x)
except:
  print("An exception occurred")

# #handling multiple error cases
print("Handling Multiple errors")
try:
  print("hi" + 3)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# #else keyword example
print("Handling errors with else keyword when no error foud ")
try:
  print(Hi)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# #fially keyword example
print("Handling errors with finally keyword")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# get type of exception
print("Get type of exception")
import sys

try:
  print("hi" + 10)
except:
   print("Oops!", sys.exc_info()[0], "occurred.")#normal loop example in python
# print("normal example")
colors = ["red", "green", "blue"]
for x in colors:
  print(x)

#we can loop though a strig
print("Loop through string")
str = "Hello World"
for x in str:
  print(x)

# loop break statement example in python
print("break statement example")
colors = ["red", "green", "blue"]
for x in colors:
    if(x == "green"):
        break
    print(x)

#loop continue statement example in python
print("continue statemet example")
colors = ["red", "green", "blue"]
for x in colors:
    if(x == "green"):
        continue
    print(x)

# else block loop example in python
print("else block example")
colors = ["red", "green", "blue"]
for x in colors:
    print(x)
else:
    print("All Items processed")

# # Range function loop example in python
print("Range function example")
for x in range(100):
  print(x)#Define a fuction
# def my_hello_world_function():
#   print("Hello World from a function")

#calling a function
# my_hello_world_function()

#Define a function with sigle parameter
# def greet_person(name):
#   print("Hi "+ name)
# greet_person("Sandip")

#Define a function with Multiple parameter
# def greet_full_name(first_name, last_name):
#   print("Hi "+ first_name + " " + last_name)
# greet_full_name("Sandip", "Das")

#Arbitrary Arguments, *args whe not sure how much parameters will be there
# def my_colours(*colours):
#   print("The second colours is " + colours[1])
# my_colours("Red", "Green", "Blue")

#Arbitrary Arguments, *args whe not sure how much parameters will be there
# def my_named_colours(**colours):
#   print("The first colours is " + colours["red"])
# my_named_colours(red = "Red Colour", blue = "Blue Colour", green = "Green Colour")

# Use return statement to return a value from a function
def sum(a, b):
  return a + b
sumValue = sum(5, 10)
print("The Sum is", sumValue)
print("Type of sumValue is", type(sumValue))

print("Hello, World!")a = 50
b = 20
# checking only if statement
if b > a:
 print("b is greater than a")

#checking if else statement
a = 20
b = 10
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")

#checking if elif else statement
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")a = int(input("Enter first number "))
b = int(input("Enter second number "))
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")import platform
x = platform.system()
print(x)a = True
b = False
print(type(a))
print(type(b))person = {
"name": "Sandip",
"age": 30,
"location" : "Kolkata"
}
print(type(person))
print(type(person['name']))
print(type(person["age"]))

#get values in disctionary by key
print(person["name"])

# We can check key of a dictionary using the in keyword
print("name" in person)

#chage value of a dictionary
person["age"] = 31
print(person["age"])

person.update({"age": 29})
print(person["age"])

#addig value of a dictionary
person["eye_color"] = "brown"
print(person)

person.update({"hair_color": "black"})
print(person)

#delete particular key from dictionary
person.pop("hair_color")
print(person)

#delete last item from dictionary
person.popitem()
print(person)

#delete particular key from dictionary usig del keyword
del person["age"]
print(person)

#empty dictionary usig clear method
person.clear()
print(person)

person = {
"name": "Sandip",
"age": 30,
"location" : "Kolkata"
}
#Loop dictionary
for x in person:
  print("key: ",x)
  print("value: ",person[x])

#Loop dictionary key 
for x in person.keys():
  print("Key",x)

#Loop dictionary value
for x in person.values():
  print("Value",x)

#Loop dictionary key and value
for x,y in person.items():
  print(x,y)


simpleList = ["red", "green", "blue", 4, 5, 6]
print(simpleList)
print(type(simpleList))

#simpleList[1] = green type is str 
print("simpleList[1] = ", simpleList[1])

print(type(simpleList[1]))

#simpleList[4] = 5 type is int 
print("simpleList[4] = ", simpleList[4])

print(type(simpleList[4]))

# simpleList[0:3] = ['red', 'green']
print("simpleList[0:3] = ", simpleList[0:3])

# simpleList[3:] = [4, 5, 6]
print("simpleList[3:] = ", simpleList[3:])

# chagig value of item in list
simpleList[2] = 3
print("value did changed", simpleList)

# get last value of list
print("simpleList[-1] = ", simpleList[-1])

#we can add value to list
simpleList.insert( 6,"new value")
print("New item added to list",simpleList)

#we can remove value from list by item value
simpleList.remove( "new value")
print("one item removed from list by value",simpleList)

#we can remove value from list by item index
simpleList.pop(2)
print("one item removed from list by index", simpleList)

#we can run for loop on list
for x in simpleList:
  print(x)






a = 7    # int
b = 3.8  # float
c = 5j   # complex
print(type(a))
print(type(b))
print(type(c))simpleSet = {4,2,5,8,1}
print(type(simpleSet))

#we can run for loop on set
for x in simpleSet:
  print(x)

#we can add or remove values

simpleSet.add(10)
print(simpleSet)

simpleSet.remove(10)
print(simpleSet)

#eliminate duplkicates

simpleSet2 = {1, 2,2, 3, 3, 3, 4, 4, 4,4, 5,5,5,5,5 }
print(simpleSet2)

#set can be used for mathematic set operations
#uninon
setA = {1, 2, 3, 4, 5, 6}
setB = {4, 5, 6, 7, 8, 9}
print(setA.union(setB))
print(setB.union(setA))
#intersection
print(setA.intersection(setB))
print(setB.intersection(setA))
#differece
print(setA.difference(setB))
print(setB.difference(setA))
#Symmetric difference 
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
name = "Sandip Das"
print(type(name)) 

# #check strig length
# print(len(name))


# # multilie string
# a = """This is,
# a 
# multi line
# strig 1"""
# print(a)

# a = '''This is,
# a 
# multi line
# strig 2'''
# print(a)

# #format variables in string

# age = 30
# txt = "My name is Sadip, and I am {}"
# print(txt.format(age))

# quantity = 14
# itemNo = 456
# price = 199.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemNo, price))

# #via index
# quantity = 14
# itemNo = 456
# price = 199.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemNo, price))
simpleList = ("red", "green", "blue", 4, 5, 6)
print(simpleList)
print(type(simpleList))

#simpleList[1] = green type is str 
print("simpleList[1] = ", simpleList[1])

print(type(simpleList[1]))

#simpleList[4] = 5 type is int 
print("simpleList[1] = ", simpleList[4])

print(type(simpleList[4]))

# simpleList[0:3] = ['red', 'green']
print("simpleList[0:3] = ", simpleList[0:3])

# simpleList[3:] = [4, 5, 6]
print("simpleList[3:] = ", simpleList[3:])

# chagig value of item in list
# simpleList[2] = 3
# print('value did not changed',simpleList)

# get last value of list
print("simpleList[-1] = ", simpleList[-1])

# #we can add value to list
# simpleList.insert( 6,"new value")
# print("New item added to list",simpleList)

# #we can remove value from list by item value
# simpleList.remove( "new value")
# print("one item removed from list by value",simpleList)

# #we can remove value from list by item index
# simpleList.pop(2)
# print("one item removed from list by index", simpleList)

#we can run for loop on list
for x in simpleList:
  print(x)






numberA = float(input("Please enter first Number: "))
numberB = float(input("Please enter second Number: "))
sumAB = numberA + numberB
#sumAB = int(numberA) + int(numberB)
print("A+ B :",sumAB)

# Implicit Type Conversion
numerInt = 123
numberFloat = 1.23

numNew = numerInt + numberFloat

print("datatype of numerInt:",type(numerInt))
print("datatype of numberFloat:",type(numberFloat))

print("Value of numNew:",numNew)
print("datatype of numNew:",type(numNew))

#explicit type conversion

numerInt = 123
numStr = "456"

print("Data type of numerInt:",type(numerInt))
print("Data type of numStr before Type Casting:",type(numStr))

numStr = int(numStr)
print("Data type of numStr after Type Casting:",type(numStr))

numSum = numerInt + numStr

print("Sum of numerInt and numStr:",numSum)
print("Data type of the sum:",type(numSum))name = "ok"# normal while loop example
# print("Normal While Loop example")
# i = 0
# while i < 10:
#   print(i)
#   i += 1

#break statement example for while loop
# print("break statement example for while loop")
# i = 1
# while i < 10:
#   print(i)
#   if i == 5:
#     break
#   i += 1

# #continue statement example for while loop
print("continue statement example for while loop")
i = 0
while i < 10:
  i += 1
  if i == 5:
    continue
  print(i)


# #else statement example for while loop
print("else statement example for while loop")

i = 0
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")