PYTHON DOCUMENTATION 
#comments in Python begin with the hash sign.(This is a Python comment). 
“”” However if a comment takes more than one line,triple speech marks are used This is also a comment””” 
#Comments in Python are used to explain the functionality of the code 
#below are just sample codes with well explained comments for better understanding 
#Copying the complete file in an ide,and running it,it will execute correctly 
“””However spelling errors may occur in the comments sections since comments are not executed when running our codes.But this wont affect the functionality of the code.””” 
print("To print in python ide use the word print and write your message in paranthesis") #To print two lines,you just have to follow the same procedure as shown below print("This will be the second line") 
#To print a similar line two times use *2 as shown below print("Hello word \n" *2) 
#variables are containers to store information #Below is a variable to store my name 
name = "Muuo" #every string must be enclosed in oppenning and closing speech marks 
#To print items stored in variables you dont need to include the opening and closing speech marks as shown 
print(name)#This wiil print the item stored in variable name which is Muuo 
#Combine strings with variables as shown below print("Hello"" "+ name) name2 = "Muumbi" 
print(name+ " " +name2) #and by the way,you have to include the speech marks so  as to separate the words 
#To find the type of the iten either string , integer... use the type key word as shown below print(type(name))#This will print str because muuo is in the data type is  str number = 3 
print(type(number))#example 2 showing the data type int 
#unlike in string data type to combine a string and a data type,,,do as shown below #however if 3 was enclosed in speechmarks it would print data type str as shown below number2 = "3" print(type(number2)) 
#Variables can still be combined explicitly,,,lets combine variable name2 and name explicitly full_name = name2+" "+name print(full_name) 
age = 20 #example of a variable storing a int data type 
age += 1#the age is added to one so as to produse 21 as the result,,,this will be studied in deep later print(age) 
#unlike in string data type to combine a string and a data type,,,do as shown below print("Hello mr"+ " " +name2+ " "+"you are"+ " "+str(age)+ " " +"years old") 
#Multiple assingnment allows one assign items to variables at the saME line as shown below school,teacher,years = "Multimedia university","Mocheche",20 print(school,teacher,age) 
#However you can print them in different lines as shown below print(school) print(teacher) print(age) 
#Different variables with similar item can be assigned using an equal sign in a single line as shown below for students with same age Felix = Stephen = Christine = 30 
print("He is"+ " " +str(Stephen)+ " "+str(Felix)+ " " +str(Christine)) 
#To print them in different lines use this format though it will be discussed deeply later print(f"He is\n{Stephen}\n {Felix}\n{Christine}") 
#You can still find the length of your item stored in a certain variable using the keyword "len" as shown below 
print(len(name))#This will print 4 since my name Muuo has four letters.However when there is space between your name it is still printed 
#Python can also find the index or position of a letter.For example lets find the position of letter 
"0" in my variable name 
print(name.find("o"))#This code will print 3 since indexing starts with 0.Incase two letters are similar like the letter u in my name,the indexing will consider the letter which comes first 
#You can capitalise your string.Note that capitalisation considers only the first letter 
#lets initialize another variable called warker and another called worker warker,worker = "alex","PAUL" print(warker.capitalize())#The first letter will be capitalized. 
#You can also make all letters to be in uppercase print(warker.upper())#All letters will be capitalized #To make them lower case use the keyword lower print(worker.lower()) 
#To check weather a string is made up of digits or letters/alphabets use the keyword "isdigit" or 
"isalpha" 
print(warker.isalpha())#This will print True 
#You can also count how many particular characters are in a String using the keyword count print(name.count("u"))#This will print 2 since we have two u's in the name "Muuo" 
#This is different from the keyword "find"  since keyword find finds the exact index of a letter #You can still change your characters to be something else using the keyword replace print(name.replace("u","a"))#my name was Muuo so it will change to Maao and it will be displayed 
#How to display items in diferent number of times,use the asteric * print(name*3) 
 
#Type casting = it is the conversion of one data type to another 
x,y,z = 1,2.6,"7"#an integer,a float umber and a string.Any number.character inside speechmarks it becomes a string print(str(x)) 
print(int(y))#This will print 2,,due to conversion from a float number to ana integer number print(float(1))#This will convert the integer to a float number and print 1.0 
#The technique above is useful especially when content in one line since you cant mix different data types in the same string as shown below 
#print(x+ is +z)#this code automatically prints an error since x was an integer and y is a string.Thats why I will comment it. 
#Review the purpose of comments and understand why I have used it here.So to correct our code and make it execute make the data types similar as shown below print(str(x)+ " "+"is"+" " +str(y)+ " " +"and"+ " "+z) 
#Accepting user input.This is done using the keyword input,It allows user to input data that he / she wants 
#NAME = input("What is your name:")#This allows user to input Aything,for example Daniel #Print function 
#print("Hello"+ " " +NAME)#This prints what has been inputed plus The word Hello.So in my case it will print Hello Daniel 
#You can instruct on what kind of Data type to input like.. 
#LENGTH = float(input("What is the length of your class :"))#inputing data type of class float 
#print("the length of my class is"+ " " +str(LENGTH)) 
#Maths tools.You have to import this math tools first 
#To round off a number import math PI = -3.142 
print(round(PI))#This will print -3,This is because it rounds off the number print(abs(PI))#This prints the absolute value of PI 
print(math.floor(PI))#This rounds the number to the nearest integer print(math.ceil(PI)) 
print(pow(PI,2))#This is called power,it raises the number to the indicated tpower print(math.sqrt(420))#This finds the square root of the nuber 
#The max function finds the largest value wheres the min function finds the minimum value a,b,c = 12,45,64 
print("The maximum value is"+ " " +str(max(a,b,c)))#This prints the maximum value which is 
64.However replacing "max" with "min" then it will display the minimum  value 
 
#SLICING = it is creating a substring by extracting elements from another string full_name = name[1]#Making the variable name 
print(full_name)#prints the character in the first index which is "u" in the name Muuo 
#In slicing,you can instruct the starting and the stopping point of printing the string as shown below 
FULL_NAME = name[0:3]#Its good to understand that the number in index zero or any other starting index  is inclusive. 
#However,the number or character in the last index is exclussive. print(FULL_NAME)#This will print the characters between zero and third character exclusivelly 
#You can still print your item stored in a variable step wise as shown below parent = "Paul and Monicah" 
print(parent[0:17:2])#This will print "pu n oia" since we have instructed it to print steps of 2[2] from the first character[0] to the last character [17] 
#So the first index determines the starting point,the second index determines the stoping point and the third index determines the step by step to be printed 
#Following the guidance above,you can be able to print your name in reversed order as shown below 
#if statement = it is a block of code that executes when the statement is true print(name[::-1])#This will print ouuM.Since the counting is in decreasing order 
 
#if statement = it is a block of code that executes when the statement is true aged = int(input("Number of years:" ))#Initializing the variable aged 
if aged <= 18:print("You are not eligible for voting")#However note that if you enter aged an integer greater than 18,it will not display any message 
#so an else statement comes in as shown else: print("You are eligible for voting") 
#However when the conditions are more than 2,,elif statement comes in student = int(input("Student age is: ")) 
if age < 18:print("you are are not eligible for voting") 
elif student < 0:print("You are not yet born") else:print("You are eligible for voting") 
#However you can still have multiple elif statements to check different conditions.Remember this if,else and elif starts with the if statement)executed first #This is the example code for multiple elif statements legend = int(input("My age is :")) 
if legend == 100:print("Your age is not allowed to vote") elif legend < 18:print("You are not eligible for voting") elif legend < 0 :print("You are not yet born") else:print("You can vote") 
#Remember after the elif keyword,you are not suppossed to put a colon as in if and else keywords 
 
#Logical operators = used to check if two statements are true.They are and ,or & not Temperature = int(input("The temperature is :")) 
if Temperature > 0 and Temperature <= 36:print("The wheather is good")#if test condition with logical operator "and" 
else:print("The temperature is not good")#For the and operator to execute true,,both statements must be true 
#Logical operator and negates the statement,,ie it gives the opposite of the statement x = 5 y = 7 
comparison = x < y #in real sense,this statement is true,lets use the logical operator not and see weather the execution will have been negated 
print(not(comparison))#This will print false since the statement is true and we have used the logical operator not to negate it 
#The or operator executes when one of the statements is true a,b = 5,9 A = a > b or a < b 
print(A)#This will print true since we have used the operator or and one of the statement is true (a > b) 
 
#While loop = The statement continues to execute as long as the condition is true 
#while 1==1:print("I am unable to skip this while loop")#This will execute to infinity 
# Lets try a while loop that can enable us escape the whole loop chairman = input("Chairmans age is:") 
while int(chairman) == 50:print(f"He can lead us since he is {chairman} years old")#This is the loop which will execute to infinity if you place value 50.However if you input a differnt value,it will terminate immidiately 
else:print("This guy is too young to lead us") 
#For loop = it executes a given code in a given number of times.ie limited times for i in range(50,100):print(i)#This will print all numbers between 50 and 100 
#As we said earlier,the first index is always inclusive whereas the last one is exclussive as you can see the code above when you run it,,the last word to display  wll be 109 #in for loop ,you can add count up the characters the way you need as shown 
for i in range(50,100,2,):print(i)#This will display numbers between 50 and 100 in counts of 2 #For loop for timing a number of seconds.Remember you have to import time modules import time 
for seconds in range(10,0,-1):print(seconds)#This is the for loop to display numbers between 10 and 0,As said earliear,for a for loop,The first number is inclusive while the last one is not inclusive ie 0.The negative 1(-1)indicates that the count is decreasing with a count of 1. 
time.sleep(1)# This line follows, which pauses the execution of the script for 1 second using the sleep function from the time module. 
print("The winner is Muuo") 
#Nested loops = is a loop made up of multiple loops as shown #The code below uses for nested loop to display  a rectangle 
columns = int(input("Number of columns is: "))#Initialization of number of columns rows = int(input("Number of rows is: "))#Initialization of number of rows symbol = input("Symbol is: ")#Initializing the symbol to use 
 
for i in range(rows): 
    for j in range(columns):         print(symbol, end=" ")     print() 
#Loop control statements = They are used to change loops execution.They are break,continue and pass 
named = "MuumbimuuoMumo" for i in named: 
    if i == "u":continue 
    print(i)#This will print "mmbimoMmo" since continue statement allows one skip an ileteration 
#Break control statement while True: 
    NAME = input("My name is:")     if NAME != "": 
        break#This is a break statement that checks if the string is empty. 	It executes until the name string is not empty and then it breaks 
#pass control statement for i in range(0,10):     if i == 8: 
        pass#This is the statement that does nothing.It will eliminate the given condition     else: 
        print(i)#numbers between 1 and 10 will be printed except 8 
         
#Lists= They are used to store multile elements.square brackets are used to enclose the items in a list      
food = ["Pizza","Chapati","Githeri" ] print(food)#This prints all items in the list food 
print(food[1])#This prints the element in index one  in the list of food 
#while using lists ;you can append,clear,sort,insert,pop as well as remove 
#append =it adds an element/item to the list 
food.append("ice cream") print(food) 
#insert = this allows one insert an item at a certain element food.insert(0, "cake")#This will insert cake at the first index print(food) 
#Remove = this removes an item from a list 
food.remove("cake")#This will print the whole list without cake print(food) 
#Pop deletes the last element while clear clears all the elements food.sort()#This arrages the items alphabetically print(food) 
#Multidimensional lists = They are lists made up f lists as shown food = ["Pizza","Chapati","Githeri" ] drinks = ["soda","Coffee","Yohgurt"] Food = [food,drinks] 
print(Food)#This prints all elements in the two lists of food and drinks print(Food[0])#This prints all the elements in the list food print(Food[1][2])#This prints element in the second list in third index #Turple = holds unchangible items.We use normal paranthesis to enclase them student = ("Bro","age","Mutua","Bro","Mulinge") 
print(student.count("Bro"))#This counts how many times the word Bro appears print(student.index("age"))#This gives the index of age 
#set = a collection of elements .enclosed by {}brackets.When displaying them they dont follow any order at all 
#A set still doesnt allow multiple similar items like knife and knife.one item will appear 
#Sets can be used to remove ,clear,update(add elements in another list not in a crtain list),add and find the differences and simlarities 
students = {"stephen","Felix","Christine","Daniel","Jacinta"} parents = {"paul","Monicah","bonface","stephen","Jacinta"} parents.add("mumo")#Adds Mumo to parent set print(parents) 
students.update(parents)#adds the elements of set parent to set students print(students) 
students_difference = students.difference(parents)#displays the different items in students and parents set 
print(students_difference) x = students.intersection(parents) 
print(x)#Finds the common elements in the two sets 
#dictionaries = stores unordered collection of unique key values capitals = {"kenya":"Nairobi","Tanzania":"mogandishu"} print(capitals["kenya"])#prints the capital of kenya print(capitals.keys())#Gives keys of capitals print(capitals.get("Tanzania")) 
#Sequebnce operator = it gives access to different elements in a string,turple  or lists.The operator is [] 
NaMe = "daniel Muuo" 
if(NaMe[0].islower()):#Checks weather the character in index 0 is in lower case    NaMe = NaMe.capitalize()#If the character is in lower case,it is now capitalized    print(NaMe) 
first_name = NaMe[0:6].upper()#This code takes characters from index 0 of variable NaMe and prints them in upper case print(first_name) 
# Function = it is a block of code that executes only when it is called 
def hello():#Hello is the  function name.A pair of paranthesis must be included,,this is  where parameters are kept.The function has to be defined still using the keyqword def     print("Hello") 
hello()#Calling of the function hello.You can still call the function multiple times and this will make it execete in that given number  of times. 
def greetings(name,secondname,age):#This is a function called greetings which takes three parameters 
    print("Hello"+" "+name+" "+"and"+" "+secondname+" "+" "+"you both have"+" "+str(age)+" 
"+"years old") 
    print("you are good boys") 
greetings("Muuo","Daniel",22)#The parameters to be printed are written here.They can still be defined  directly using the parameters as the variables,By the way,this are called arguments and they should allign with their parameters 
greetings("Muuo","Daniel",22)#It prints the same thing two times 
 
#Nested function calls = this are function calls inside another function call #The execution of this function calls begins with the innermost function as shown num = print(round(abs(float(input("Enter a whole number:")))))#This is a code that will allow user input a number,convert it to float number,find its absolute value,round it off and print it.It follows the sequence of execution from inside 
#The scope = its the region where a variable is recognized.It can be either global or local variable 
#Global variabvles are available outside the function unlike local variables name = "Muuo"#Global variable initialization def display_name(name):     name = "Muumbi" 
    print(name)#prints the local variable display_name("Muumbi") 
 
print(name) 
#*args = is the parameter that allows a function take all parameters.The asterick sign must be used def add(*args): 
    sum = 0     for i in args:         sum += i     return sum print(add(1,4,5)) 
#Kwargs = takes parameters of dictionaries def names(**kwargs): 
    print("hello"+" "+kwargs["first"]+" "+kwargs["last"]) names(first = "Bro",last = "Dan") 
 
#Str.format() = it is a optional method that gives users more control  overdisplaying output NamE = "Muuo"#Normal variable initialization secondname = "Mutua"#Normal variable initialization 
print("The boys are:{} and {}".format(NamE,secondname))#A string format.It's east since it doesn't bother you to cancantenate strings which may even cause errors easiy 
print("The boys are:{} and {}".format(secondname,NamE))#Perfoms the same as the code above but the variable secondname is printed before the variable NamE 
#However the str.format method may be controlled using indexes as shown below 
print("The boys are:{0} and {1}".format(secondname,NamE))#This will print only values stored in variable in ndex 0 
print("The boys are:{1} and {0}".format(secondname,NamE))#This will print values starting with the one stored in variable in index 1 followed by the one stored in variable at index 0 
#Using the str.format method,it is still not important to initialize variables as obvious 
print("Our school captain is called {NAME} {SECONDNAME}".format(SECONDNAME = "Muumbi",NAME = "Muuo"))#Second name and name are called keyword arguments which acts as variables in this case 
#You can still use it for spacing 
NamE = "Muuo" secondname = "Mutua" 
print("My name is {:10} and i am good".format(NamE))#This will print the string aS "My name is Muuo       and i am good"This is because we have instructed it to live 10 spaces after displaying the variable name 
#The method above,you can display the space either after,before or center it. 
print("My name is {:<10} and i am good".format(NamE)) 
print("My name is {:>10} and i am good".format(NamE))#This will leave the space on the left side 
print("My name is,,, {:^10},,, and i am good".format(NamE))#This will center the space 
#Formatting numbers pi = 3.1423 
print("The number pi is {:.2f}".format(pi))#This will display pi like 3.14.2f means to display the  number into twa decimal places number = 1000 
print("The number is {:,}".format(number))#This adds a comma to the thousands digit print("The number is {:b}".format(number))#Displaying the number as a binary number print("The number is {:o}".format(number))#Display the number as octal print("The number is {:X}".format(number))#Display the number as hexadecimal print("The number is {:x}".format(number))#Display the number as hexadecimal but in small letters 
print("The number is {:e}".format(number))#Display the number in scientific notification but in small letters 
print("The number is {:E}".format(number))#Display the number in scientific notification but in capital letters 
#Import random = it allows one get random choices 
import random#Tis is a math import which alllows a program choose randomly y = random.randint(3,8)#This chooses any number between 3 and 8 randomly print(y) 
cards = ["a",1,2,2,4,5,7.6,8,"e","t"]#This arrages the characters randomly random.shuffle(cards) print(cards) 
#Exception = they are events that occur to a program during its execution and affects its normal execution try: 
    number_numerator = int(input("The numerator is: "))     number_denominator = int(input("The denominator is: "))     result = number_numerator / number_denominator 
except ZeroDivisionError:#ZeroDivisionError,,a number cannot be divided by zero         print("Division by zero")#The exception message else: 
            print (result) finally: 
    print("This block always executes") 
 
#Files existence import os 
 
file_path = r"\C:\Users\USER\pythonintroductionpractice2.py" print("Full path:", os.path.abspath(file_path)) 
 
if os.path.exists(file_path):     print("The file exists.") else: 
    print("The file doesnt  exist") 
#Reading and opening a file 
#with open('test.tx'): as file#This opens file test.tx if it exists 
#print(file.read)#This reads the file test,tx if its in your computer 
 
#Writing files in python 
text = "my name  is Daniel \nFrom Multimedia university\nwith a degreee in Mathematics and computer science"  with open('test.txt','w')as file: 
    file.write(text) 
# Reading and printing the contents of the file with open('test.txt', 'r') as file: 
    file_contents = file.read()     print(file_contents) 
#Copying files 
#Copyfile() = copies contents of a file only 
#Copy() = copyfile() + permission file + destination can be a directory 
#Copy2() = copies meta data 
import shutil #Module that contains copying commands shutil.copyfile('test.txt','copy.txt')#Copying the files to copy.txt file 
 
#Moving files import os 
source = "pythonintroduction3.py" destination = "C:\\Users\\USER\\Desktop" try: 
    if os.path.exists(destination):print("This file is already moved")     else: 
        os.replace(source,destination)         print("file moved succesfully") except FileNotFoundError:     print("Cant process this") #Deleting files import os 
 
path = 'muuo' 
 
try: 
    os.remove(path)     print("File deleted") except FileNotFoundError: 
    print("File not in your computer") except Exception as e: 
    print(f"Ooops! An error occurred: {e}") 
#You can also delete a directory in the same way but using the keyword rmdir 
#Importing modules in python 
#Male sure you use the keyword import followed by name of the file you need to import its itrms.However dont include the extension ".py".     
import sys 
import practicepythonintroduction 
print(practicepythonintroduction.teacher)#The item to be imported fom practicepythonintroduction Traceback (most recent call last): 

     PYTHON CHEAT SHEET  
B A S I C S
Print
Prints a string into the console. 
Input	print("Hello World")
Prints a string into the console, and asks the user for a string input.
Comments	input("What's your name")
Adding a # symbol in font of text lets you make comments on a line of code. The computer will ignore your comments.
Variables	#This is a comment print("This is code")
A variable give a name to a piece of data. Like a box with a label, it tells you what's inside the box. 
The += Operator	my_name = "Angela" my_age = 12
This is a convient way of saying: "take the previous value and add to it. 	my_age = 12 my_age += 4 #my_age is now 16
D A T A T Y P E S
Integers
Integers are whole numbers.
Floating Point Numbers	my_number = 354
Floats are numbers with decimal places. When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always be a floating point number.
Strings	my_float = 3.14159
A string is just a string of characters.
It should be surrounded by double quotes.
String Concatenation	my_string = "Hello"
You can add strings to string to create a new string. This is called concatenation. It results in a new string.
Escaping a String	"Hello" + "Angela"
#becomes "HelloAngela"
Because the double quote is special, it denotes a string, if you want to use it in a string, you need to escape it with a "\"	speech = "She said: \"Hi\"" print(speech)
#prints: She said: "Hi"
F-Strings
You can insert a variable into a string using f-strings.
The syntax is simple, just insert the variable in-between a set of curly braces {}.
Converting Data Types	print(f"There are {days} in a year")
You can convert a variable from 1 data type to another.
Converting to float: float()
Converting to int: int()
Converting to string: str()
Checking Data Types	n = 354 new_n  = float(n) print(new_n) #result 354.0
You can use the type() function to check what is the data type of a particular variable.	n = 3.14159 type(n) #result float
days = 365 
M A T H S
Arithmetic Operators
You can do mathematical calculations with Python as long as you know the right operators.
The += Operator	3+2 #Add
4-1 #Subtract
2*3 #Multiply
5/2 #Divide
5**2 #Exponent
This is a convenient way to modify a variable. It takes the existing value in a variable and adds to it. 
You can also use any of the other mathematical operators e.g. -= or *=
The Modulo Operator	my_number = 4 my_number += 2 #result is 6
Often you'll want to know what is the remainder after a division. 
e.g. 4 ÷ 2 = 2 with no remainder but 5 ÷ 2 = 2 with 1 remainder
The modulo does not give you the result of the division, just the remainder.
It can be really helpful in certain situations,
e.g. figuring out if a number is odd or even.	5 % 2
#result is 1
 
E R R O R S
Syntax Error
Syntax errors happen when your code does not make any sense to the computer. This can happen because you've misspelt something or there's too many brackets or a missing comma.
print(12 + 4))
  File "<stdin>", line 1     print(12 + 4))                  ^
SyntaxError: unmatched ')'
 
Name Error
This happens when there is a variable with a name that the computer does not recognise. It's usually because you've misspelt the name of a variable you created earlier. 
Note: variable names are case sensitive!
my_number = 4 my_Number + 2
Traceback (most recent call last): File "<stdin>", line 1, NameError: name 'my_Number' is not defined
 
Zero Division Error
This happens when you try to divide by zero, This is something that is mathematically impossible so Python will also complain.
5 % 0
Traceback (most recent call last): File "<stdin>", line 1, ZeroDivisionError: integer division or modulo by zero
F U N C T I O N S
Creating Functions
This is the basic syntax for a function in Python. It allows you to give a set of instructions a name, so you can trigger it multiple times without having to re-write or copy-paste it. The contents of the function must be indented to signal that it's inside.
Calling Functions
You activate the function by calling it. This is simply done by writing the name of the function followed by a set of round  brackets. This allows you to determine when to trigger the function and how many times.
def my_function(): print("Hello") name = input("Your name:") print("Hello")
 
my_function() my_function() #The function my_function #will run twice.
Functions with Inputs
In addition to simple functions, you can 	
give the function an input, this way, each time the function can do something different depending on the input. It makes your function more useful and re-usable.	print(n1 + n2)
 add(2, 3)
def add(n1, n2):
 
Functions with Outputs
In addition to inputs, a function can also have an output. The output value is proceeded by the keyword "return".
This allows you to store the result from a function.
Variable Scope
Variables created inside a function are destroyed once the function has executed. The location (line of code) that you use a variable will determine its value. Here n is 2 but inside my_function() n is 3. So printing n inside and outside the function will determine its value.
def add(n1, n2): return n1 + n2
 result = add(2, 3)
n = 2
def my_function(): n = 3 print(n)  print(n) #Prints 2 my_function() #Prints 3
 
Keyword Arguments
When calling a function, you can provide a keyword argument or simply just the value.
Using a keyword argument means that you don't have to follow any order when providing the inputs.
def divide(n1, n2):
result = n1 / n2
#Option 1: divide(10, 5) 
#Option 2: divide(n2=5, n1=10)
C O N D I T I O N A L S
If
This is the basic syntax to test if a condition is true. If so, the indented code will be executed, if not it will be skipped.
Else
This is a way to specify some code that will be executed if a condition is false.
n = 5 if n > 2: print("Larger than 2")
 
age = 18 if age > 16: print("Can drive")
else:
print("Don't drive")
 
 
Elif
In addition to the initial If statement condition, you can add extra conditions to test if the first condition is false. Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.
weather = "sunny" if weather == "rain":
print("bring umbrella") elif weather == "sunny":
print("bring sunglasses")
elif weather == "snow": print("bring gloves") and
This expects both conditions either side of the and to be true.
or
This expects either of the conditions either side of the or to be true. Basically, both conditions cannot be false.
not
This will flip the original result of the condition. e.g. if it was true then it's now false.
s = 58 if s < 60 and s > 50: print("Your grade is C")
 
age = 12 if age < 16 or age > 200: print("Can't drive")
 
if not 3 > 1:
print("something")
#Will not be printed.
 
comparison operators
These mathematical comparison operators allow you to refine your conditional checks.
> Greater than
< Lesser than
>= Greater than or equal to
<= Lesser than or equal to
== Is equal to
!= Is not equal to
L O O P S
While Loop
This is a loop that will keep repeating itself until the while condition becomes false.
For Loop
For loops give you more control than while loops. You can loop through anything that is iterable. e.g. a range, a list, a dictionary or tuple. 
_ in a For Loop
If the value your for loop is iterating through, e.g. the number in the range, or the item in the list is not needed, you can replace it with an underscore.
n = 1 while n < 100:
n += 1
all_fruits = ["apple",
"banana", "orange"] for fruit in all_fruits: print(fruit)
 
for _ in range(100):
#Do something 100 times.
 
break
This keyword allows you to break free of the loop. You can use it in a for or while loop.
scores = [34, 67, 99, 105] for s in scores:
if s > 100: print("Invalid") break print(s)
continue
This keyword allows you to skip this iteration of the loop and go to the next. The loop will still continue, but it will start from the top.
continue
print(n)
#Prints all the odd numbers
Infinite Loops
n = 0 while n < 100: n += 1 if n % 2 == 0:
 
Sometimes, the condition you are checking to see if the loop should continue never becomes false. In this case, the loop will continue for eternity (or until your computer stops it). This is more common with while loops.
while 5 > 1: print("I'm a survivor")
 
 
L I S T M E T H O D S
Adding Lists Together
You can extend a list with another list by using the extend keyword, or the + symbol.
Adding an Item to a List
If you just want to add a single item to a list, you need to use the .append() method.
List Index
To get hold of a particular item from a list you can use its index number. This number can also be negative, if you want to start counting from the end of the list.
list1 = [1, 2, 3] list2 = [9, 8, 7] new_list = list1 + list2 list1 += list2
all_fruits = ["apple",
"banana", "orange"] all_fruits.append("pear")
 
List Slicing
Using the list index and the colon symbol	
you can slice up a list to get only the portion you want.
Start is included, but end is not.	letters = ["a","b","c","d"] letters[1:3]
#Result: ["b", "c"]
#list[start:end]
letters = ["a", "b", "c"] letters[0] #Result:"a" letters[-1] #Result: "c"
B U I L T I N F U N C T I O N S
Range
Often you will want to generate a range of numbers. You can specify the start, end and step.
Start is included, but end is excluded: start <= range < end
Randomisation
The random functions come from the random module which needs to be imported.
In this case, the start and end are both 
included start <= randint <= end
Round
This does a mathematical round. So 3.1 becomes 3, 4.5 becomes 5 and 5.8 becomes 6.
# range(start, end, step) for i in range(6, 0, -2): print(i)
 # result: 6, 4, 2 # 0 is not included.
 
import random
# randint(start, end) n = random.randint(2, 5) #n can be 2, 3, 4 or 5.
abs
This returns the absolute value.
Basically removing any -ve signs.	abs(-4.6)
# result 4.6
round(4.6) # result 5
M O D U L E S
Importing
Some modules are pre-installed with python e.g. random/datetime
Other modules need to be installed from pypi.org
Aliasing
You can use the as keyword to give your module a different name.
import random n = random.randint(3, 10)
 
import random as r n = r.randint(1, 5)
 
Importing from modules
You can import a specific thing from a module. e.g. a function/class/constant You do this with the from keyword. It can save you from having to type the same thing many times.
from random import randint n = randint(1, 5)
 
Importing Everything
You can use the wildcard (*) to import everything from a module. Beware, this usually reduces code readability.
from random import * list = [1, 2, 3] choice(list) # More readable/understood
#random.choice(list)
 
C L A S S E S & O B J E C T S
Creating a Python Class
You create a class using the class keyword.
Note, class names in Python are PascalCased. So to create an empty class 
Creating an Object from a Class
You can create a new instance of an object by using the class name + ()
Class Methods	class MyClass:
#define class
 
class Car: pass my_toyota = Car()
You can create a function that belongs to a class, this is known as a method.
Class Variables	class Car:
def drive(self):
print("move")
my_honda = Car() my_honda.drive()
You can create a varaiable in a class. The value of the variable will be available to all objects created from the class.	class Car:
colour = "black"
car1 = Car()
print(car1.colour) #black
The __init__ method
The init method is called every time a new object is created from the class.	class Car:
def __init__(self):
print("Building car")
my_toyota = Car() #You will see "building car"
#printed.
Class Properties
You can create a variable in the init() of a class so that all objects created from the class has access to that variable.
Class Inheritance	class Car:
def __init__(self, name):
self.name = "Jimmy"
When you create a new class, you can inherit the methods and properties of another class.	class Animal:
def breathe(self):
print("breathing")
class Fish(Animal):
def breathe(self): super().breathe() print("underwater")
nemo = Fish() nemo.breathe()
#Result: 
#breathing
#underwater

