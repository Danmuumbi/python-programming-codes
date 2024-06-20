num1 = int(input("enter the first numer: "))
num2 = int(input("enter the second numer "))
operator = input("enter the operator: ")
match operator:
    case '+':
        print(f"the sum is {num1+num2}")
    case '-':
        print(f"the differece is {num1-num2}")
    case '*':
        print(f"the differece is {num1*num2}")
    case '/':
        print(f"the differece is {num1/num2}")
    case _:
        print("invalid")