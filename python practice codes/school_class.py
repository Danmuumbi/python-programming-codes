class School:
    def __init__(self,name="",age="",course="",grade=""):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
    @property
    def name(self):
        print("retrievig ame: ")
        return self.__name
    @name.setter
    def name(self,value):
        if value.isalpha():
            self.__name = value
        else:
            print("enter alphabetical character ")
    @property
    def age(self):
        print("retrieving age..")
        return self.__age
    @age.setter
    def age(self,digit):
        if digit.isdigit():
            self.__age = digit
        else:
            print("enter a digit ")
    @property
    def course(self):
        print("retrievig the course..")
        return self.__course
    @course.setter
    def course(self,typee):
        if typee.isalpha():
            self.__course = typee
        else:
            print("invalid course ")
    @property
    def grade(self):
        print("retrievig grade")
        return self.__grade
    @grade.setter
    def grade(self,marks):
        if marks.isdigit():
            self.__grade = marks
        else:
            print("enter valid marks")

def main():
    students = School()
    Name = input("students name is:")
    Age = input("enter students age ")
    Course = input("course ")
    students.age = Age
    students.course=Course
    students.name=Name
    print(f"{students.name} is {students.age} old specializing in {students.course}")
main()
