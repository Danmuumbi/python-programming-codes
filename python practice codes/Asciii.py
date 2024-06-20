# Using a single loop to iterate over ASCII values of lowercase alphabet
for i in range(97, 123):
    if i != 122:  # For all characters except the last one, add a space after the character
        print(f"{chr(i)}", end=" ")#opposite of chr is ord
    else:
        print(f"{chr(i)}", end="")
