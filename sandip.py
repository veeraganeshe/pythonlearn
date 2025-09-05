# python directories

#get current working directory
import os
currentWorkingDirectory = os.getcwd()
print("Current Working Directory is : ",currentWorkingDirectory)

#check directories and file list
import os
print(os.listdir())
print("Lit of Directories and files", os.listdir())

#create new directory
# import os
# if os.path.exists("my_new_sample_directory"):
#     print("The Folder already exists")
# else:
#     os.mkdir("my_new_sample_directory")
#     print("The Folder is created")


#change directory to any path such as /var/logs 
# import os
# os.chdir('/var/logs')
# print("Changed to Directory: ",os.getcwd())
# os.chdir(currentWorkingDirectory)
# print("Current Working Directory: ",os.getcwd())


# # file handling just adding the content on the file

# #we can remove file by usnig inbild os module
# # import os
# # os.remove("sample_file_2.txt")

# #delete file if exist

# import os
# if os.path.exists("sample_file_2.txt"):
#   os.remove("sample_file_2.txt")
# else:
#   print("The file does not exist")

# #file write mode example
# # f = open("sample_file_2.txt", "a")
# # f.write("This is a line just overwritten the existing file three\n")
# # f.close()
# # f = open("sample_file_2.txt", "r")
# # print(f.read())
# # f.close()

# # f= open("custom_module_example.py", "a")
# # f.write("this is adding the content\n")
# # # print(f.read())
# # f.close()

# # f= open("test.txt", "a")
# # f.write("this is adding the content to new test.txt\n")
# # # print(f.read())
# # f.close()

# # f= open("custom_module_example.py", "a")
# # f.write("this is adding a  content to append three \n")
# # print(f.read())
# # f.close()
# # f= open("custom_module_example.py", "r")
# # for x in f:
# #      print("line: ",x) 
# # f.close()

# # check file is exists or not 1st
# # import os
# # if os.path.exists("test.py"):
# #     f= open("test.py", "r")
# # # f.write("this is adding a  content to write\n")
# #     print(f.read())
# #     f.close()
# # else:
# #     print("The file does not exists")    

# # import os
# # if os.path.exists("custom_module_example.py"):
# #     f= open("custom_module_example.py", "r")
# # # f.write("this is adding a  content to write\n")
# #     print(f.read())
# #     f.close()
# # else:
# #     print("The file does not exists")  





# # # #decorator example adding function to existing function
# # def formatGreet(func):
# #     def innerfunc(name):
# #         print("***************")
# #         func(name)
# #         print("***************")
# #     return innerfunc

# # # def greetFirstName(name):
# # #         print("Hello ",name)

# # # prettyGreet = formatGreet(greetFirstName)
# # # prettyGreet("Veera")

# # #or represent with @ as it's a syntactic sugar to implement decorators

# # # @formatGreet
# # # def greetFirstName(name):
# # #         print("Hello ",name)

# # # greetFirstName("Viewer")

# # # def formatGreet(func):
# # #     def wrapper(name):
# # #         print("Decorator is working:")
# # #         func(name)
# # #         print("Have a nice day!")
# # #     return wrapper

# # @formatGreet
# # def greetFirstName(name):
# #     print("Hello", name)

# # greetFirstName("Viewer Have nice day!!")



# # # factorial calculation using recursion
# # # def calculateFactorial(x):
# # #     if x == 1:
# # #         return 1
# # #     else:
# # #         return (x * calculateFactorial(x-1))
# # # num = 4
# # # facorial_number = calculateFactorial(num)
# # # print("Factorial of ", num, "is 1 * 2 * 3 * 4 = ", facorial_number)


# # # doSum = lambda a,b: a + b
# # # print(doSum(10,20))

# # # def doSum(a,b):
# # #     return a + b
# # # print (doSum(10,40))

# # #list filter example to list values greater than 15
# # # my_custom_list = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]

# # # my_filtered_list = list(filter(lambda x: (x > 8) , my_custom_list))

# # # print(my_filtered_list)

# # # #use lambda to manipulate data set and do vaue doubler using map
# # # my_custom_list = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
# # # my_manipulated_list = list(map(lambda x: x + x , my_custom_list))
# # # print(my_manipulated_list)

# # # #global scope example
# # # x = "I am a Global Variable"
# # # def someFunction():
# # #     print("x inside function:", x)
# # # someFunction()
# # # print("x outside function:", x)
  

# # # Global Scope conflict reslution: Treating global and local variables as different variable name

# # # x = "I am a Global Variable"
# # # def someFunction():
# # #     x = "I am a Local Variable"
# # #     print("x inside function:", x)
# # # someFunction()
# # # print("x outside function:", x)



# # # Global valiable using global keyword
# # # def someFunction():
# # #   global x
# # #   x = 500
# # #   print("x inside function:", x)
# # # someFunction()
# # # print("x outside function:", x)




# #       #Try  Except
# # #handling simple error
# # # # print(x)
# # # print("Handling simple error")
# # # try:
# # #   print(x)
# # # except:
# # #   print("An exception occurred")

# # # # #handling multiple error cases
# # # print("Handling Multiple errors")
# # # try:
# # #   print("hi" + 3)
# # # except NameError:
# # #   print("Variable x is not defined")
# # # except:
# # #   print("Something else went wrong")

# # # # #else keyword example
# # # # print("Handling errors with else keyword when no error foud ")
# # # # try:
# # # #   print(Hi)
# # # # except:
# # # #   print("Something went wrong")
# # # # else:
# # # #   print("Nothing went wrong")

# # # # get type of exception
# # # print("Get type of exception")
# # # import sys

# # # try:
# # #   print("x")
# # # except:
# # #    print("Oops!", sys.exc_info()[0], "occurred.")

# # # print("Get type of exception")
# # # import sys

# # # try:
# # #   print("hi" + 3)
# # # except:
# # #    print("Oops!", sys.exc_info()[0], "occurred.")   

# # # # #fially keyword example
# # # print("Handling errors with finally keyword")
# # # try:
# # #   print(x)
# # # except:
# # #   print("Something went wrong")
# # # finally:
# # #   print("The 'try except' is finished")

# # # # get type of exception
# # # print("Get type of exception")
# # # import sys

# # # try:
# # #   print("hi" + 10)
# # # except:
# # #    print("Oops!", sys.exc_info()[0], "occurred.")

# #             #system Modules

# # # import platform
# # # x = platform.system()
# # # print(x)

# #             # return value

# # # def sum(a,b):
# # #     return a + b
# # # sumValue = sum(5,10)
# # # print("The sum is ", sumValue)



# #             # functions
# # #Define a fuction
# # # def my_hello_world_function():
# # #   print("Hello World from a function")
# # #   #calling a function
# # # my_hello_world_function()

# # #Define a function with Multiple parameter
# # # def greet_full_name(first_name, mid_name, last_name):
# # #   print("Hi "+ first_name + " " + mid_name + " " + last_name) 
# # # greet_full_name("Veera", "Sundara", "pandian")

# # #Arbitrary Arguments, *args whe not sure how much parameters will be there
# # # def my_colours(*colours):
# # #   print("The second colours is " + colours[1])
# # # my_colours("Red", "Green", "Blue")

# # # def my_colours(*colours):
# # #   print("The second colours is " + colours[1])
# # # my_colours("Red", "Green", "Blue")

# # #Arbitrary Arguments, *args whe not sure how much parameters will be there
# # # def my_named_colours(**colours):
# # #   print("The first colours is " + colours["red"])
# # # my_named_colours(red = "Red Colour", blue = "Blue Colour", green = "Green Colour")




# # # def my_colours(*colours):
# # #     for color in colours:
# # #         print(color)

# # # my_colours("Red", "Green", "Blue")


# # #  while loop
# # # # normal while loop example
# # # print("Normal While Loop example")
# # # i = 5
# # # while i < 10:
# # #   print(i)
# # #   i += 1

# # # #break statement example for while loop
# # # print("break statement example for while loop")
# # # i = 1
# # # while i < 10:
# # #   print(i)
# # #   if i == 5:
# # #     break
# # #   i += 1    

# #         ## continue statement current iteration only

# # # #continue statement example for while loop  skip pana continue use panalam
# # # print("continue statement example for while loop")
# # # i = 0
# # # while i < 10:
# # #   i += 1
# # #   if i == 5:
# # #     continue
# # #   print(i)


# #              # #else statement example for while loop
# # # print("else statement example for while loop")

# # # i = 1
# # # while i < 10:
# # #   print(i)
# # #   i += 1
# # # else:
# # #   print("i is no longer less than 10")


# #             # # FOR LOOP:

# # # # print("normal for loop example")
# # # # colors = ["red", "green", "blue"]
# # # # for x in colors:
# # # #     print(x)

# # # # else block loop example in python
# # # # print("else block example")

# # # # colors = ["red", "green", "blue"]
# # # # for x in colors:
# # # #     print(x)
# # # # else:
# # # #     print("All Items processed")


# # # # print("else block example")

# # # # colors = ["red", "green", "blue"]
# # # # for x in colors:
# # # #     print(x)
# # # #     if (x == "green"):
# # # #         break
# # # # else:
# # # #     print("All Items processed")

# # # # Range  function in loop example

# # # print("Range function example")
# # # for x in range(4):
# # #     print(x)
# # # # ## Range  function in loop example between numbers
# # # # print("Range function example")
# # # # for x in range(1,3):
# # # #     print(x)






# # # # # loop break statement example in python
# # # # print("break statement example")
# # # # colors = ["red", "green", "blue"]
# # # # print (colors)
# # # # for x in colors:
# # # #     if(x == "green"):
# # # #         break
# # # #     print(x)

# # # #loop continue statement example in python
# # # # print("continue statemet example")

# # # # colors = ["red", "green", "blue"]
# # # # print(colors)
# # # # for x in colors:
# # # #     if(x == "green"):    
# # # #         continue
# # # #     print(x)






# # # # IF ELSE statement

# # # # if condition

# # # # a = 5
# # # # b = 10
# # # # if b>a:
# # # #     print("b is greater than a")
# # # # elif a==b:
# # # #     print("a and b are equal")
# # # # else:
# # # # #     print("a is greater than b")        

# # # # a = int(input("Enter the number for a value: "))

# # # # b = int(input("Enter the number for b  value: "))
# # # # if b>a:
# # # #     print(f"{b} is greater than {a}")
# # # # elif a==b:
# # # #     print(f"{a} and {b} are equal")
# # # # else:
# # # #     print(f"{a} is greater than {b}")  

# # # # a = int(input("Enter number for a value: "))
# # # # b = int(input("Enter the number for b  value: " ))

# # # # if b>a:
# # # #     print("b is greater than a")
# # # # elif a == b:
# # # #     print("a and b are equal")
# # # # else:
# # # #     print("a is greater than b")        

# # # # # Dict

# # # # person = {
# # # # "name": "Veera",
# # # # "age": 30,
# # # # "location" : "Kolkata"
# # # # }
# # # # # print(type(person))
# # # # # print(type(person['name']))
# # # # # print(type(person["age"]))

# # # # #get values in disctionary by key
# # # # print(person["name"])
# # # # print(person["age"])

# # # # print("name" in person)
# # # # person.update({"age": 32})
# # # # print(person["age"])

# # # # person.update({"eyecolor": "black"})
# # # # print(person["eyecolor"])

# # # # person.pop("location")
# # # # print(person)



# # # # #             #set
# # # # # simpleSet2 = {1,2,3,2,3,4,3,3,2,1,5,5,5,3,5,5}
# # # # # print(simpleSet2)


# # # # # print("Hello World!!")

# # # # # simpleList = ["red", "green", "blue", 4, 5, 6]
# # # # # print(simpleList)
# # # # # print(type(simpleList))


# # # # # simpleList[2] = "yellow"
# # # # # print("value did changed", simpleList)

# # # # # print("last value =", simpleList[-1])

# # # # # simpleList.insert(6,"veera")
# # # # # print("New item added to the list",simpleList)

# # # # # simpleList.remove("veera")
# # # # # print("New item added to the list by value",simpleList)

# # # # # simpleList.pop(2)
# # # # # print("one item removed from list by idex",simpleList)
