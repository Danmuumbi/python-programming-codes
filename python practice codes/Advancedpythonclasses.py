class Student:
    def __init__(self, student_id, name, student_class, fees_paid):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.fees_paid = fees_paid

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Class: {self.student_class}")
        print(f"Fees Paid: {self.fees_paid}")
        print("\n")


def main():
    # Create instances of the Student class for different students
    student1 = Student(1, "Stephen Muumbi", "Class A", 500)
    student2 = Student(2, "Felix Muumbi", "Class B", 700)
    student3 = Student(3, "Daniel Muumbi", "Class A", 600)

    # Store the student instances in a dictionary with the student ID as the key
    students = {
        student1.student_id: student1,
        student2.student_id: student2,
        student3.student_id: student3
    }

    # Accept user input for student ID
    user_input = int(input("Enter student ID to display information: "))

    # Display information if the student ID exists
    if user_input in students:
        students[user_input].display_info()
    else:
        print("Student ID not found.")

if __name__ == "__main__":
    main()
    
#Example 2 to display information of church christians
class Churchmembers:
    def __init__(self,memberid,name,church,hisparents,wife,numberofchildrens,children,Diocesscontribution,smallchristiangroupparticipation,mariagestatus):
        self.memberid = memberid
        self.name = name
        self.church = church
        self.hisparents = hisparents
        self.wife = wife
        self.numberofchildrens = numberofchildrens
        self.children = children
        self.Diocesscontribution = Diocesscontribution
        self.smallchristiangroupparticipation = smallchristiangroupparticipation
        self.mariagestatus = mariagestatus
    def display_info(self):
        print(f"Members id is: {self.memberid}")
        print(f"His name is: {self.name}")
        print(f"His church is : {self.church}")
        print(f"His parents are: {self.hisparents}")
        print(f"His wife is:{self.wife}")
        print(f"He has: {self.numberofchildrens}"+ " " +"childrens")
        print(f"His childrens are : {self.children}")
        print(f"He has contributed {self.Diocesscontribution}"+" " +"Kenya shillings in the current Diocess contribution")
        print(f"His contribution and participation to small christian group is {self.smallchristiangroupparticipation}")
        print(f"He is {self.mariagestatus}")

def main():
    churchmembers1 =  Stephen","Kaseve Catholic Church","Paul and Monicah","Jacinta",2,"William and Wilson",1500,"Quite excelent","yet to marry oficially in the church")
    churchmembers2 = Churchmembers(2,"Felix","Senda Catholic church","Paul and Monicah","Angella",1,"Abel",2000,"Commentable","Not oficially maried in the church")
    churchmembers3 = Churchmembers(3,"Daniel","Wote Catholic Church","Paul and Monicah","Not married","Not married","Not maried",200,"Excelent","Not married")
    
    churchmember = {churchmembers1.memberid:churchmembers1,
                churchmembers2.memberid:churchmembers2,
                churchmembers3.memberid:churchmembers3
                }
    # Accept user input for memeber ID
    user_input = int(input("Enter church member ID to display information: "))
# Display information if the member ID exists
    if user_input in churchmember:
        churchmember[user_input].display_info()
    else:
        print("Church member ID not found.")

if __name__ == "__main__":
    main()
    