orig_string = input("convert ")
orig_string = orig_string.upper()
list_of_words = orig_string.split()#covert strig ito a list
for word in list_of_words:
    print(word[7],end="")
print()