student_score = input().split()
for n in range(0,len(student_score)):
    student_score[n]= int(student_score[n])
highest_scre = 0
for score in student_score:
    if score > highest_scre:
        highest_scre = score

print(highest_scre)