from collections import deque

# Create an empty deque
my_deque = deque()

# Append elements to the right end of the deque
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# Append elements to the left end of the deque
my_deque.appendleft(0)

# Extend deque with elements from an iterable (adds elements to the right end)
my_deque.extend([4, 5, 6])

# Extend deque with elements from an iterable (adds elements to the left end)
my_deque.extendleft([-1, -2, -3])

# Pop an element from the right end of the deque
popped_element = my_deque.pop()

# Pop an element from the left end of the deque
popped_left_element = my_deque.popleft()

# Access elements by index
print(my_deque[0])  # prints the first element

# Iterate over the deque
for item in my_deque:
    print(item)

# Convert deque to a list
my_list = list(my_deque)
print(my_list)
