import random
name = []  # Empty list to store the strings

while True:
    user_input = input("Enter a name (or 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break
    
    name.append(user_input)

print("List of names:", name)
random_person = random.choice(name)
print(f"{random_person} shouuld go for the milk")
##input_string = input("Enter names separated by spaces: ")
##names = input_string.split()//the iput will stop whe the user preses the eter key without ay writtig 

# If the input is separated by commas, you can use:
# names = [name.strip() for name in input_string.split(',')]

##print("List of names:", names)
