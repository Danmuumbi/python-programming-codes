def double_stuff(a_list):
    for index, value in enumerate(a_list):
        a_list[index] = 2 * value
    print(a_list)

# Example usage
a_list = [2, 3, 4]
double_stuff(a_list)
