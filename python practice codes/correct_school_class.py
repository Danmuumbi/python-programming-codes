class School:
    def __init__(self):
        self._name = ""
        self._age = ""
        self._course = ""
        self._grade = ""

    @property
    def name(self):
        print("retrieving name: ")
        return self._name
    
    @name.setter
    def name(self, value):
        if value.isalpha():
            self._name = value
        else:
            print("Enter alphabetical characters only for the name")
            self._name = input("Student's name is: ")
            self.name = self._name  # Recursively call the setter to validate again
    
    @property
    def age(self):
        print("retrieving age...")
        return self._age
    
    @age.setter
    def age(self, digit):
        if digit.isdigit():
            self._age = digit
        else:
            print("Enter a valid digit for age")
            self._age = input("Enter student's age: ")
            self.age = self._age  # Recursively call the setter to validate again
    
    @property
    def course(self):
        print("retrieving the course...")
        return self._course
    
    @course.setter
    def course(self, typee):
        if typee.isalpha():
            self._course = typee
        else:
            print("Invalid course. Use alphabetical characters only")
            self._course = input("Course: ")
            self.course = self._course  # Recursively call the setter to validate again
    
    @property
    def grade(self):
        print("retrieving grade...")
        return self._grade
    
    @grade.setter
    def grade(self, marks):
        if marks.isdigit():
            self._grade = marks
        else:
            print("Enter valid marks in digits")
            self._grade = input("Enter valid marks: ")
            self.grade = self._grade  # Recursively call the setter to validate again

def main():
    students = School()
    
    students.name = input("Student's name is: ")
    students.age = input("Enter student's age: ")
    students.course = input("Course: ")
    
    print(f"{students.name} is {students.age} years old specializing in {students.course}")

main()
