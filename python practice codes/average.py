number_of_studebts = int(input("enter number of students: "))
print("student heights are:")
student_heights = []
for i in range(0,number_of_studebts):
    heights = int(input())
    student_heights.append(heights)
total = sum(student_heights)
averange = total/number_of_studebts
print(f"the average height is {averange}")