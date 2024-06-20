def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

operations = {"+": add, "-": subtract, "/": divide, "*": multiply}
def calculator():
    a = int(input("Enter first number: "))

    print("Available operations:")
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation = input("Enter operation to use: ")
    
        if operation not in operations:
            print("Invalid operation. Please try again.")
            continue

        b = int(input("Enter second number: "))
        calculation = operations[operation]
        answer = calculation(a, b)

        print(f"{a} {operation} {b} = {answer}")
   
        if input("Enter 'y' to continue or 'n' to exit: ") == "y":
            a = answer
        else:
            should_continue = False
            calculator()

calculator()
