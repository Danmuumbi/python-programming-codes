numbers = [1, 2, 3, 4, 5]

for index, value in enumerate(numbers):
    numbers[index] = value**2

print(numbers)  # This will print the entire list of squared numbers

for index, value in enumerate(['banana', 'apple', 'pear', 'quince']):
    print (index, value)