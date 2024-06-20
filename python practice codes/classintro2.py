from classesintro import Car
car_1 = Car("Chevy","Normal",15,2023)
print("The cars model is"+" " +car_1.model)
print("It costs:"+ " "+str(car_1.cost))
print("It was manufactured on "+ " " +str(car_1.year))
print("Its shape is:"+ " " +car_1.shape)
print("The car has"+" "+str(car_1.wheels)+" " +"wheels")
car_1.drive()
#However class variables can be printed using the class names  as shown
print(Car.wheels,"\n\n")#This will print 4
#To be precise class variables are initialized in the class itsel,while instance variables must be in the __init__ method

#Inheritance in python = python allows a certan class to be applied to different subclasses as shown
print("             INHERITANCE IN PYTHON")
print("Inheritance in python = python allows a certan class to be applied to different subclasses as shown")
class Animal:#Initializing the class animal
    alive = True
    def eat(self):
        print("This animal is eating")
        
    def move(self):
        print("This animal is moving")
    
class Fish(Animal):#This is a class inherited from the class animal
    
    def swim(self):
        print("This fish is swimming")
        print("Those are attributes of our fish\n")

class Rabbit(Animal):#This is a class inherited from the class animal
#Inheritance allows one give an object different attributes which are different from common attributes like we know afish can swim unlike rabbit which can only run
#.Lets define an attribute for run as rabbit does.Remember to check the attribute of fish(swim) as in the class of fish
    def run(self):
        print("The rabbit is running")
        print("Those are attributes of our Rabbit","\n")
    pass
#Lastly,you need to call your functions as shown
fish = Fish()
rabbit = Rabbit()

print(fish.alive)
fish.eat()
fish.move()
fish.swim()

rabbit.eat()
rabbit.move()
rabbit.run()

#Multi level inheritance in python = this is the case where an inherited class inherits another class
#lets create class organism
class Organism:#This is the main class named Organism
    alive = True
class Animal(Organism):#This is a child class/subclass inherited from class organism
    def move(self):
        print("This animal can move")
    def eat(self):
        print("Like all animals ,this animal can eat")
class Dog(Animal):#This is what we mean by multi level inheritance,a child class named Dog that has inherited from another child class named Animal
    def bark(self):
        print("This Dog can bark","\n\n")
dog = Dog()
animal = Animal()
print(Organism.alive)

animal.move()
animal.eat()
dog.bark()

#Method chaining = This is calling several method subsequently
class Car:
    def turn_on(self):
        print("You turn on the engine")
        return self#This will enable method chaining
    def drive(self):
        print("Then the car moves")
        return self
    def brake(self):
        print("You apply brakes")
        return self
    def stop(self):
        print("Then the car stops""\n\n")
        return self
        
#Calling the functions
car = Car()
car.turn_on().drive().brake().stop()#calling subsequently the functions

#Super metod = this is a function that gives access to the methods of a parent class
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super(). __init__(length,width)#Using super class allows some attributes be initialized only once as we have done to length  and width
        self.height = height
    
    def area(self):
        return self.length*self.width*self.height
    
class Square(Rectangle):
    def __init__(self,length,height):
        super().__init__(length,height)
        self.height = height
    def area(self):
        return self.length*self.height

rectangle = Rectangle(4,5)
print(rectangle.area())

cube = Cube(3,3,3)
print(cube.area())

square =Square(5,5)
print(square.area(),"\n")

#Passing objects as arguments
class Car:
    colour = None

def change_colour(car, colour):
    car.colour = colour

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_colour(car_1, "red")
change_colour(car_2, "black")
change_colour(car_3, "blue")
print("the colour of the first car is:"+ " " +car_1.colour)
print("the colour of the second car is:"+ " " +car_2.colour)
print("the colour of the third car is:"+ " " +car_3.colour,"\n\n")

#Duck typing = is the concept where class has no great importance like the attributes
class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):\
        print("This duck is clucking")
class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")
class Person:
    def catch(self,duck):
        duck.walk()
        chicken.talk()
        print("We caught the creature")
duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)
        
#Lambda function = is a function weritten in one line using the keyword lambda
#lets have a function to add numbers and use the lambda function concept
add = lambda x,y:x + y#Using the lambda function
print(add(2,3),"\n\n")#Passing our arguments to the function

#sorting
Familly_members = ["stephen","Felix","Christine","Daniel"]
Familly_members.sort(reverse = True)#This will sort the turple in alphabetical order
for i in Familly_members:
    print(i)
#Sorting columns
    family_members = [("stephen",35),
                      ("Felix",33),
                      ("Daniel",20),
                      ("Christine",26)]
    years = lambda years:years[1]
    family_members.sort(key=years,reverse = True)#This wll allow sorting 0f items in family_members in reverse order from the oldest
    for i in family_members:
        print(i)
    
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        
#Filter= allws us filter ites in a iterable with certain characteristics
Citizens = [("Uhuru",74),
            ("Ruto",73),
            ("Daniel",16),
            ("Joseph",13),
            ("Joy",17),
            ("Raila",88)]
age = lambda x:x[1] >= 18
drinking_buddies = list(filter(age,Citizens))
if not drinking_buddies:
    print()
else:
    for i in drinking_buddies :
        print(i)

         


