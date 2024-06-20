#Logical operators = used to check if two statements are true.They are and ,or & not
Temperature = int(input("The temperature is :"))
if Temperature > 0 and Temperature <= 36:print("The wheather is good")#if test condition with logical operator "and"
else:print("The temperature is not good")#For the and operator to execute true,,both statements must be true
#Logical operator and negates the statement,,ie it gives the opposite of the statement
x = 5
y = 7
comparison = x < y #in real sense,this statement is true,lets use the logical operator not and see weather the execution will have been negated
print(not(comparison))#This will print false since the statement is true and we have used the logical operator not to negate it
#The or operator executes when one of the statements is true
a,b = 5,9
A = a > b or a < b
print(A)#This will print true since we have used the operator or and one of the statement is true (a > b)

#While loop = The statement continues to execute as long as the condition is true
#while 1==1:print("I am unable to skip this while loop")#This will execute to infinity
# Lets try a while loop that can enable us escape the whole loop
chairman = input("Chairmans age is:")
while int(chairman) == 50:print(f"He can lead us since he is {chairman} years old")#This is the loop which will execute to infinity if you place value 50.However if you input a differnt value,it will terminate immidiately
else:print("This guy is too young to lead us")
#For loop = it executes a given code in a given number of times.ie limited times
for i in range(50,100):print(i)#This will print all numbers between 50 and 100
#As we said earlier,the first index is always inclusive whereas the last one is exclussive as you can see the code above when you run it,,the last word to display  wll be 109
#in for loop ,you can add count up the characters the way you need as shown
for i in range(50,100,2,):print(i)#This will display numbers between 50 and 100 in counts of 2
#For loop for timing a number of seconds.Remember you have to import time modules
import time
for seconds in range(10,0,-1):print(seconds)#This is the for loop to display numbers between 10 and 0,As said earliear,for a for loop,The first number is inclusive while the last one is not inclusive ie 0.The negative 1(-1)indicates that the count is decreasing with a count of 1.
time.sleep(1)# This line follows, which pauses the execution of the script for 1 second using the sleep function from the time module.
print("The winner is Muuo")
#Nested loops = is a loop made up of multiple loops as shown
#The code below uses for nested loop to display  a rectangle
columns = int(input("Number of columns is: "))#Initialization of number of columns
rows = int(input("Number of rows is: "))#Initialization of number of rows
symbol = input("Symbol is: ")#Initializing the symbol to use

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()
#Loop control statements = They are used to change loops execution.They are break,continue and pass
named = "MuumbimuuoMumo"
for i in named:
    if i == "u":continue
    print(i)#This will print "mmbimoMmo" since continue statement allows one skip an ileteration
#Break control statement
while True:
    NAME = input("My name is:")
    if NAME != "":
        break#This is a break statement that checks if the string is empty.	It executes until the name string is not empty and then it breaks
#pass control statement
for i in range(0,10):
    if i == 8:
        pass#This is the statement that does nothing.It will eliminate the given condition
    else:
        print(i)#numbers between 1 and 10 will be printed except 8
        
#Lists= They are used to store multile elements.square brackets are used to enclose the items in a list     
food = ["Pizza","Chapati","Githeri" ]
print(food)#This prints all items in the list food
print(food[1])#This prints the element in index one  in the list of food
#while using lists ;you can append,clear,sort,insert,pop as well as remove
#append =it adds an element/item to the list
food.append("ice cream")
print(food)
#insert = this allows one insert an item at a certain element
food.insert(0, "cake")#This will insert cake at the first index
print(food)
#Remove = this removes an item from a list
food.remove("cake")#This will print the whole list without cake
print(food)
#Pop deletes the last element while clear clears all the elements
food.sort()#This arrages the items alphabetically
print(food)
#Multidimensional lists = They are lists made up f lists as shown
food = ["Pizza","Chapati","Githeri" ]
drinks = ["soda","Coffee","Yohgurt"]
Food = [food,drinks]
print(Food)#This prints all elements in the two lists of food and drinks
print(Food[0])#This prints all the elements in the list food
print(Food[1][2])#This prints element in the second list in third index
#Turple = holds unchangible items.We use normal paranthesis to enclase them
student = ("Bro","age","Mutua","Bro","Mulinge")
print(student.count("Bro"))#This counts how many times the word Bro appears
print(student.index("age"))#This gives the index of age
#set = a collection of elements .enclosed by {}brackets.When displaying them they dont follow any order at all
#A set still doesnt allow multiple similar items like knife and knife.one item will appear
#Sets can be used to remove ,clear,update(add elements in another list not in a crtain list),add and find the differences and simlarities
students = {"stephen","Felix","Christine","Daniel","Jacinta"}
parents = {"paul","Monicah","bonface","stephen","Jacinta"}
parents.add("mumo")#Adds Mumo to parent set
print(parents)
students.update(parents)#adds the elements of set parent to set students
print(students)
students_difference = students.difference(parents)#displays the different items in students and parents set
print(students_difference)
x = students.intersection(parents)
print(x)#Finds the common elements in the two sets
#dictionaries = stores unordered collection of unique key values
capitals = {"kenya":"Nairobi","Tanzania":"mogandishu"}
print(capitals["kenya"])#prints the capital of kenya
print(capitals.keys())#Gives keys of capitals
print(capitals.get("Tanzania"))
#Sequebnce operator = it gives access to different elements in a string,turple  or lists.The operator is []
NaMe = "daniel Muuo"
if(NaMe[0].islower()):#Checks weather the character in index 0 is in lower case
   NaMe = NaMe.capitalize()#If the character is in lower case,it is now capitalized
   print(NaMe)
first_name = NaMe[0:6].upper()#This code takes characters from index 0 of variable NaMe and prints them in upper case
print(first_name)
# Function = it is a block of code that executes only when it is called
def hello():#Hello is the  function name.A pair of paranthesis must be included,,this is  where parameters are kept.The function has to be defined still using the keyqword def
    print("Hello")
hello()#Calling of the function hello.You can still call the function multiple times and this will make it execete in that given number  of times.
def greetings(name,secondname,age):#This is a function called greetings which takes three parameters
    print("Hello"+" "+name+" "+"and"+" "+secondname+" "+" "+"you both have"+" "+str(age)+" "+"years old")
    print("you are good boys")
greetings("Muuo","Daniel",22)#The parameters to be printed are written here.They can still be defined  directly using the parameters as the variables,By the way,this are called arguments and they should allign with their parameters
greetings("Muuo","Daniel",22)#It prints the same thing two times

#Nested function calls = this are function calls inside another function call
#The execution of this function calls begins with the innermost function as shown
num = print(round(abs(float(input("Enter a whole number:")))))#This is a code that will allow user input a number,convert it to float number,find its absolute value,round it off and print it.It follows the sequence of execution from inside
#The scope = its the region where a variable is recognized.It can be either global or local variable
#Global variabvles are available outside the function unlike local variables
name = "Muuo"#Global variable initialization
def display_name(name):
    name = "Muumbi"
    print(name)#prints the local variable
display_name("Muumbi")

print(name)
#*args = is the parameter that allows a function take all parameters.The asterick sign must be used
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,4,5))
#Kwargs = takes parameters of dictionaries
def names(**kwargs):
    print("hello"+" "+kwargs["first"]+" "+kwargs["last"])
names(first = "Bro",last = "Dan")
