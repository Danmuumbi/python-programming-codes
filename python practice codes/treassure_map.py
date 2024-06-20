# Define the rows of the map
line1 = ["A", "B", "C"]
line2 = ["D", "E", "F"]
line3 = ["G", "H", "I"]

# Combine the rows into a map
treasure_map = [line1, line2, line3]

print("Hiding your treasure, mark with an 'x'")
# Get the position from the user input
position = input("Enter the position to hide the treasure (e.g., 'A1'): ")

# Extract the letter (column) from the position and convert it to lowercase
letter = position[0].lower()

# Define the list of column identifiers
abc = ["a", "b", "c"]

# Get the index of the letter in the column identifiers list
letter_index = abc.index(letter)

# Get the row number from the position and convert it to an index (0-based)
number_index = int(position[1]) - 1

# Mark the specified position with an 'x' in the map
treasure_map[number_index][letter_index] = 'x'

# Print the updated map
print(f"{line1}\n{line2}\n{line3}")
