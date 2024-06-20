#Str.format() = it is a optional method that gives users more control  overdisplaying output
NamE = "Muuo"#Normal variable initialization
secondname = "Mutua"#Normal variable initialization
print("The boys are:{} and {}".format(NamE,secondname))#A string format.It's east since it doesn't bother you to cancantenate strings which may even cause errors easiy
print("The boys are:{} and {}".format(secondname,NamE))#Perfoms the same as the code above but the variable secondname is printed before the variable NamE
#However the str.format method may be controlled using indexes as shown below
print("The boys are:{0} and {1}".format(secondname,NamE))#This will print only values stored in variable in ndex 0
print("The boys are:{1} and {0}".format(secondname,NamE))#This will print values starting with the one stored in variable in index 1 followed by the one stored in variable at index 0
#Using the str.format method,it is still not important to initialize variables as obvious
print("Our school captain is called {NAME} {SECONDNAME}".format(SECONDNAME = "Muumbi",NAME = "Muuo"))#Second name and name are called keyword arguments which acts as variables in this case
#You can still use it for spacing
NamE = "Muuo"
secondname = "Mutua"
print("My name is {:10} and i am good".format(NamE))#This will print the string aS "My name is Muuo       and i am good"This is because we have instructed it to live 10 spaces after displaying the variable name
#The method above,you can display the space either after,before or center it.
print("My name is {:<10} and i am good".format(NamE))
print("My name is {:>10} and i am good".format(NamE))#This will leave the space on the left side
print("My name is,,, {:^10},,, and i am good".format(NamE))#This will center the space
#Formatting numbers
pi = 3.1423
print("The number pi is {:.2f}".format(pi))#This will display pi like 3.14.2f means to display the  number into twa decimal places
number = 1000
print("The number is {:,}".format(number))#This adds a comma to the thousands digit
print("The number is {:b}".format(number))#Displaying the number as a binary number
print("The number is {:o}".format(number))#Display the number as octal
print("The number is {:X}".format(number))#Display the number as hexadecimal
print("The number is {:x}".format(number))#Display the number as hexadecimal but in small letters
print("The number is {:e}".format(number))#Display the number in scientific notification but in small letters
print("The number is {:E}".format(number))#Display the number in scientific notification but in capital letters
#Import random = it allows one get random choices
import random#Tis is a math import which alllows a program choose randomly
y = random.randint(3,8)#This chooses any number between 3 and 8 randomly
print(y)
cards = ["a",1,2,2,4,5,7.6,8,"e","t"]#This arrages the characters randomly
random.shuffle(cards)
print(cards)
#Exception = they are events that occur to a program during its execution and affects its normal execution
try:
    number_numerator = int(input("The numerator is: "))
    number_denominator = int(input("The denominator is: "))
    result = number_numerator / number_denominator
except ZeroDivisionError:#ZeroDivisionError,,a number cannot be divided by zero
        print("Division by zero")#The exception message
else:
            print (result)
finally:
    print("This block always executes")

#Files existence
import os

file_path = r"\C:\Users\USER\pythonintroductionpractice2.py"
print("Full path:", os.path.abspath(file_path))

if os.path.exists(file_path):
    print("The file exists.")
else:
    print("The file doesnt  exist")
#Reading and opening a file
#with open('test.tx'): as file#This opens file test.tx if it exists
#print(file.read)#This reads the file test,tx if its in your computer

#Writing files in python
text = "my name  is Daniel \nFrom Multimedia university\nwith a degreee in Mathematics and computer science" 
with open('test.txt','w')as file:
    file.write(text)
# Reading and printing the contents of the file
with open('test.txt', 'r') as file:
    file_contents = file.read()
    print(file_contents)
#Copying files
#Copyfile() = copies contents of a file only
#Copy() = copyfile() + permission file + destination can be a directory
#Copy2() = copies meta data
import shutil #Module that contains copying commands
shutil.copyfile('test.txt','copy.txt')#Copying the files to copy.txt file

#Moving files
import os
source = "pythonintroduction3.py"
destination = "C:\\Users\\USER\\Desktop"
try:
    if os.path.exists(destination):print("This file is already moved")
    else:
        os.replace(source,destination)
        print("file moved succesfully")
except FileNotFoundError:
    print("Cant process this")
#Deleting files
import os

path = 'muuo'

try:
    os.remove(path)
    print("File deleted")
except FileNotFoundError:
    print("File not in your computer")
except Exception as e:
    print(f"Ooops! An error occurred: {e}")
#You can also delete a directory in the same way but using the keyword rmdir
#Importing modules in python
#Make sure you use the keyword import followed by name of the file you need to import its items.However dont include the extension ".py".    
import sys
import practicepythonintroduction
print(practicepythonintroduction.teacher)#The item to be imported fom practicepythonintroduction Traceback (most recent call last):
   
