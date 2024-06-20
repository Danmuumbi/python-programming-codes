#comments in python begin with the hash sign.This is a python comment
print("To print in python ide use the word print and write your message in paranthesis")
#To print two lines,you just have to follow the same procedure as shown below
print("This will be the second line")
#To print a similar line two times use *2 as shown below
print("Hello word \n" *2)
#variables are containers to store information
#Below is a variable to store my name
name = "Muuo" #every string must be enclosed in oppenning and closing speech marks
#To print items stored in variables you dont need to include the opening and closing speech marks as shown
print(name)#This wiil print the item stored in variable name which is Muuo
#Combine strings with variables as shown below
print("Hello"" "+ name)
name2 = "Muumbi"
print(name+ " " +name2) #and by the way,you have to include the speech marks so  as to separate the words
#To find the type of the iten either string , integer... use the type key word as shown below
print(type(name))#This will print str because muuo is in the data type is  str
number = 3
print(type(number))#example 2 showing the data type int
#unlike in string data type to combine a string and a data type,,,do as shown below
#however if 3 was enclosed in speechmarks it would print data type str as shown below
number2 = "3"
print(type(number2))
#Variables can still be combined explicitly,,,lets combine variable name2 and name explicitly
full_name = name2+" "+name
print(full_name)
age = 20 #example of a variable storing a int data type
age += 1#the age is added to one so as to produse 21 as the result,,,this will be studied in deep later
print(age)
#unlike in string data type to combine a string and a data type,,,do as shown below
print("Hello mr"+ " " +name2+ " "+"you are"+ " "+str(age)+ " " +"years old")
#Multiple assingnment allows one assign items to variables at the saME line as shown below
school,teacher,years = "Multimedia university","Mocheche",20
print(school,teacher,age)
#However you can print them in different lines as shown below
print(school)
print(teacher)
print(age)
#Different variables with similar item can be assigned using an equal sign in a single line as shown below for students with same age
Felix = Stephen = Christine = 30
print("He is"+ " " +str(Stephen)+ " "+str(Felix)+ " " +str(Christine))
#To print them in different lines use this format though it will be discussed deeply later
print(f"He is\n{Stephen}\n {Felix}\n{Christine}")
#You can still find the length of your item stored in a certain variable using the keyword "len" as shown below
print(len(name))#This will print 4 since my name Muuo has four letters.However when there is space between your name it is still printed
#Python can also find the index or position of a letter.For example lets find the position of letter "0" in my variable name
print(name.find("o"))#This code will print 3 since indexing starts with 0.Incase two letters are similar like the letter u in my name,the indexing will consider the letter which comes first
#You can capitalise your string.Note that capitalisation considers only the first letter
#lets initialize another variable called warker and another called worker
warker,worker = "alex","PAUL"
print(warker.capitalize())#The first letter will be capitalized.
#You can also make all letters to be in uppercase
print(warker.upper())#All letters will be capitalized
#To make them lower case use the keyword lower
print(worker.lower())
#To check weather a string is made up of digits or letters/alphabets use the keyword "isdigit" or "isalpha"
print(warker.isalpha())#This will print True
#You can also count how many particular characters are in a String using the keyword count
print(name.count("u"))#This will print 2 since we have two u's in the name "Muuo"
#This is different from the keyword "find"  since keyword find finds the exact index of a letter
#You can still change your characters to be something else using the keyword replace
print(name.replace("u","a"))#my name was Muuo so it will change to Maao and it will be displayed
#How to display items in diferent number of times,use the asteric *
print(name*3)

#Type casting = it is the conversion of one data type to another
x,y,z = 1,2.6,"7"#an integer,a float umber and a string.Any number.character inside speechmarks it becomes a string
print(str(x))
print(int(y))#This will print 2,,due to conversion from a float number to ana integer number
print(float(1))#This will convert the integer to a float number and print 1.0
#The technique above is useful especially when content in one line since you cant mix different data types in the same string as shown below
#print(x+ is +z)#this code automatically prints an error since x was an integer and y is a string.Thats why I will comment it.
#Review the purpose of comments and understand why I have used it here.So to correct our code and make it execute make the data types similar as shown below
print(str(x)+ " "+"is"+" " +str(y)+ " " +"and"+ " "+z)
#Accepting user input.This is done using the keyword input,It allows user to input data that he / she wants
#NAME = input("What is your name:")#This allows user to input Aything,for example Daniel
#Print function
#print("Hello"+ " " +NAME)#This prints what has been inputed plus The word Hello.So in my case it will print Hello Daniel
#You can instruct on what kind of Data type to input like..
#LENGTH = float(input("What is the length of your class :"))#inputing data type of class float
#print("the length of my class is"+ " " +str(LENGTH))
#Maths tools.You have to import this math tools first
#To round off a number
import math
PI = -3.142
print(round(PI))#This will print -3,This is because it rounds off the number
print(abs(PI))#This prints the absolute value of PI
print(math.floor(PI))#This rounds the number to the nearest integer
print(math.ceil(PI))
print(pow(PI,2))#This is called power,it raises the number to the indicated tpower
print(math.sqrt(420))#This finds the square root of the nuber
#The max function finds the largest value wheres the min function finds the minimum value
a,b,c = 12,45,64
print("The maximum value is"+ " " +str(max(a,b,c)))#This prints the maximum value which is 64.However replacing "max" with "min" then it will display the minimum  value

#SLICING = it is creating a substring by extracting elements from another string
full_name = name[1]#Making the variable name
print(full_name)#prints the character in the first index which is "u" in the name Muuo
#In slicing,you can instruct the starting and the stopping point of printing the string as shown below
FULL_NAME = name[0:3]#Its good to understand that the number in index zero or any other starting index  is inclusive.
#However,the number or character in the last index is exclussive.
print(FULL_NAME)#This will print the characters between zero and third character exclusivelly
#You can still print your item stored in a variable step wise as shown below
parent = "Paul and Monicah"
print(parent[0:17:2])#This will print "pu n oia" since we have instructed it to print steps of 2[2] from the first character[0] to the last character [17]
#So the first index determines the starting point,the second index determines the stoping point and the third index determines the step by step to be printed
#Following the guidance above,you can be able to print your name in reversed order as shown below
#if statement = it is a block of code that executes when the statement is true
print(name[::-1])#This will print ouuM.Since the counting is in decreasing order

#if statement = it is a block of code that executes when the statement is true
aged = int(input("Number of years:" ))#Initializing the variable aged
if aged <= 18:print("You are not eligible for voting")#However note that if you enter aged an integer greater than 18,it will not display any message
#so an else statement comes in as shown
else: print("You are eligible for voting")
#However when the conditions are more than 2,,elif statement comes in
student = int(input("Student age is: "))
if age < 18:print("you are are not eligible for voting")
elif student < 0:print("You are not yet born")
else:print("You are eligible for voting")
#However you can still have multiple elif statements to check different conditions.Remember this if,else and elif starts with the if statement)executed first
#This is the example code for multiple elif statements
legend = int(input("My age is :"))
if legend == 100:print("Your age is not allowed to vote")
elif legend < 18:print("You are not eligible for voting")
elif legend < 0 :print("You are not yet born")
else:print("You can vote")
#Remember after the elif keyword,you are not suppossed to put a colon as in if and else keywords



