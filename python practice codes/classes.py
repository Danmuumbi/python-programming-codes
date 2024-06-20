class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        name_pieces = name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

user=User("muuo muumbi",26)
print(f"my name is {user.name} and i am {user.age} old")
print(f"my first name is {user.first_name}")
print(f"my last name is {user.last_name}")