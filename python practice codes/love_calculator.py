first_name = input("enter first name ")
second_name = input("enter second name ")


combined_names = first_name.lower() + second_name.lower()


t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e1 = combined_names.count('e')
first_digit = t + r + u + e1


l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e2 = combined_names.count('e')
second_digit = l + o + v + e2

score = int(str(first_digit) + str(second_digit))
print(f"your score is {score}%")
if score < 25:
    print("make a good conversation with your patner")
elif score >= 25 and score <= 50:
    print("a small issue in your relationship")
else:print("do whatever you want god relationship!")
print("goodbye niggah!")
