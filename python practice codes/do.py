#guuess a umere etwee oe ad te
secret_number = 7
while True:
    try:
        value = int(input("gues the correct number"))
    except ValueError:
        print("value error occured")
    if value == secret_number:
     print("you got it")
     break