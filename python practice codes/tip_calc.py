print("welcome to the tip calculator")
num = int(input("what was the total bill? $"))
give_tip = int(input("how much tip would you like to give? 10, 12, or 15?"))
people_to_split = int(input("how many people to split the bill? "))
to_pay = (num*(give_tip/100))/people_to_split
print(f"each person shuld pay: ${to_pay}")