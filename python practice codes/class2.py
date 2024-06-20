class Dog:
    def __init__(self,name="",height="",age=""):
        #you begin by defining attributes.in laymans language they are the haracteristics which are unique to the members of the class
        self.name = name
        self.height = height
        self.age = age
        #now define  the methods.this are the characteristics which are siilar to all memers of the same group
    def walk(self):
        print("{} the dog walks".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def bark(self):
        print("{} the dog barks".format(self.name))

def main():
    spot = Dog("spot",32,10)#this are sttriutes of dog oe
    spot.bark()
    bowser = Dog("bowser",65,5)
    bowser.eat()
main()