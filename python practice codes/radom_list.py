import random  # Correct spelling of random module

for i in range(10):
    rand_list = [random.randint(1, 100) for _ in range(i)]  # Generate a list of random numbers
    for num in rand_list:  # Iterate over the elements of the rand_list
        print(num)
