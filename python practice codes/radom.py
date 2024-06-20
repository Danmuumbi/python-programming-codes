import random
number = random.randint(1,30)
if number<10:
    print(f"{number} is too small")
elif number >10 and number<20:
    print(f"{number} almpst there")
else:
    print(f"{number}correct range")