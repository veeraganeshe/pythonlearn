# # # # print("Hello veera")
# # # language = ["Tamil", "Kannada", "English", "Malayalam"]
# # # print(language[-1])

# # # numbers = range(1,6)
# # # print (numbers)
# # # # print(list(numbers))
# # # # print(tuple(numbers))
# # # # print(set(numbers))

# # # print(dict.fromkeys(numbers,8))
# # numbers1 = range(1,6,1)
# # print(list(numbers1))
# # numbers1 = range(1,6,2)
# # print(list(numbers1))
# # numbers1 = range(5,0,-1)
# # print(list(numbers1))

# # if else  statement

# # num = int(input("enter a value to check negative or 0 "))
# # if num > 0:
# #     print("positive number")
# # elif num == 0:
# #     print("zero")
# # else:
# #     print("Negative number")        

# # while loop
# # n = 100

# # sum = 0
# # i = 1

# # while i <= n:
# #     sum = sum + i
# #     i = i+1
# # print("The sum is", sum)    

# # for loop

# # numbers = [6,5,3,8,4,2]
# # sum = 1
# # for val in numbers:
# #     sum = sum + val
# # print ("The sum is ", sum)    

# # # break statement

# # for val in "string":
# #     if val == "i":
# #         break
# #     print(val)
# # print("The end")    

# # # continue statement like skip
# # for val in "string":
# #     if val == "r":
# #         continue
# #     print(val)
# # print("The end")

#             # Function
# # def print_lines():
# #     print("I am line1.")
# #     print("I am line2.")
# # print_lines()    


# # def add_numbers(a,b):
# #     sum = a + b
# #     print(sum)
# # add_numbers(4,5)

# # def add_numbers(a,b):
# #     sum = a + b
# #     return sum
# # result = add_numbers(4,5)
# # print(result)

#         #recursive Function
# # factorial of number

# # def calc_factorial(x):
# #     if x == 1:
# #         return 1
# #     else:
# #         return(x * calc_factorial(x-1))
# # print(calc_factorial(6))

#         # # lambda function

# # square = lambda x: x ** 2
# # print(square(5))

# #       modules  vera file/script kula irukura function a access pana use panurathu than modules
# # def add (a,b):
# #     return a + b # saved as example.py


# # def add (a,b):
# #     return a + b # saved as example.py and will access from this script
# #add.py

# # import sample
# # #accsing the function from another script by . operator example(example.py) name is sample name to access
# # print(sample.add(5, 5)) # add here is function name from another script

# # import math

# # result = math.log2(50)
# # # return the base-2 logarithm
# # print(result)
# # from math import pi
# # print ("The value of pi is", pi)


#             # open file



# # f = open("test.txt",'a')
# # #  to specifying full path C:\Users\veera.ganesan\Documents\Documents\py-tamil-hacks
# # f.write("\n the new line from JVL code channel4")
# # f.close()
# # # print(f.read())

# # f = open("test.txt",'r')
# # #  to specifying full path C:\Users\veera.ganesan\Documents\Documents\py-tamil-hacks
# # print(f.read())
# # f.close()

# # f= open("test.txt",'r')
# # print(f.read())

# # f= open("try.txt", 'w')
# # f.write("\n new try on the text file create and write")
# # f.close()

# # f = open("test.txt",'r',encoding = 'utf-8')
# # print(f.read(4))

# # f = open("test.txt",'r')
# # print(f.read(4))

# # f = open ("test.txt",'a')
# # f.write("\n new line adding for the same nth time ")
# # f.close
# # f = open("test.txt", 'r')
# # print(f.read())


# # f=  open("test.txt", "a+")
# # f.write("\n new line adding for the same with append and read 3rd time")
# # f.seek(0)           # Move pointer to start so you can read the whole file
# # print(f.read())
# # f.close()

# # Open file and read contents
# # with open("test.txt", "r") as file:
# #     content = file.read()

# # # Modify the text
# # content = content.replace("read 2md time", "read 2nd time")

# # # # Write modified content back to file
# # # with open("test.txt", "w") as file:
# # #     file.write(content)

# # # print("Text replaced successfully.")

# #              # open the file modify and read the file        
# # # Open file and read contents
# # with open("test.txt", "r") as file:
# #     content = file.read()

# # # Modify the text
# # content = content.replace("read 2md time", "read 2nd time")

# # # Write modified content back to file
# # with open("test.txt", "w") as file:
# #     file.write(content)

# # print("Text replaced successfully.")

# # # Reopen file to read and print the updated content
# # with open("test.txt", "r") as file:
# #     updated_content = file.read()

# # print("Updated File Content:\n", updated_content)


#             #Exception handling
# # import module sys to get  the type of exception

# import sys

# randomlist = ['a', 0,2]
# for entry in randomlist:
#     try:
#         print("The entry is ",entry)
#         r = 1/int(entry)
#         break
#     except:
#         print("oops!",sys.exc_info()[0],"occured")
#         print("Next entry.")
#         print()
# print("The reciprocal of",entry, "is",r)        

                #directory operations



# import os

# os.getcwd() #present working directory 
# os.chdir ('D://Downloads') # changing the directory 
# # os.listdir() #list the files/folders from current directory
# # os.mkdir('veera')  #creating new dirc by the name of veera
# # os.rename('veera','sundar') # renaming  the folder 
# # os.remove('old.txt') #deleting the old.txt file

# import os
# print("Current directory:", os.getcwd())  # Shows current directory
# os.chdir('Downloads')  # Change to the "Downloads" folder inside current directory
# print("New directory:", os.getcwd())  # Confirm the directory has changed

        #class  & objects

            # class  
# class Myclass:
#     "This is my class"
#     a = 10
#     def func(self):
#         print('hello')
# print (Myclass.a)
# print(Myclass.func)  
# print(Myclass.__doc__)      

            # object
# class Myclass:
#     "This is my class"
#     a = 10
#     def func(self):
#         print('hello')

# obj1 = Myclass()
# print(obj1.a)

# obj2 = Myclass()
# print(obj1.a+5)

        # Inheritance
class Mammal:
    def displayMammlFeatures(self):
        print('Mammal is warm-blooded animal')
class Dog(Mammal):
    def displayDogFeatures(self):
        print("Dog has 4 legs")

d = Dog()  # in here d is the variabled for the object for  dog class
d.displayDogFeatures()
d.displayMammlFeatures()












[O




