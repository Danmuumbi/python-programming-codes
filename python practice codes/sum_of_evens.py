number = int(input("enter the range "))
total = 0
for n in range(number+1):
    if n % 2 == 0:
        total += n
print(total)