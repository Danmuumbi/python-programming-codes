#this program checks if someones height is greater than 120,if true then it will check wheather the person is above 18,orbelow 18 or above 35 and execute the ier loops
#however if persons height is less than 120 then it will mve to the second if statement and  print that he/she cannot ride
height = int(input("Enter height "))
if height >= 120:
    print("can ride check conditions here")
    age =int(input("enter his/her age: "))
    if age < 18:
        print("pay $30 to ride.")
    elif age >= 18 and age <= 45:
        print("pay $40 to ride.")
    else:
        print("pay $50 to ride.")
else:
    print("cant ride ")
print("welcome!")