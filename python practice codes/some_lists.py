fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits1 = fruits.count('apple')
print(fruits1)

fruits1 = fruits.count('tangerine')
print(fruits1)

fruits1 = fruits.index('banana')
print(fruits1)

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits1 = fruits.pop()
print(fruits1)
print(fruits)  # Print the modified list after popping
