# Function to get valid input for a single integer between 1 and 26
def get_valid_input():
    while True:
        num = input("Enter an integer between 1 and 26: ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 26:
                return num
        print("Invalid input. Please enter a valid integer between 1 and 26.")

# Get user input for a list of five integers between 1 and 26
user_input = [get_valid_input() for _ in range(5)]

# Convert numbers to letters and join them to form a word
result_word = ''.join(chr(num + ord('a') - 1) for num in user_input)
print(f"The word corresponding to the numbers {user_input} is: {result_word}")
