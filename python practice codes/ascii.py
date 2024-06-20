original_string = input("Enter a string to hide: ")

# Encoding the original string
secret_string = ""
for char in original_string:
    secret_string += str(ord(char))

print("Secret message:", secret_string)

# Decoding the secret message
decoded_string = ""
for i in range(0, len(secret_string), 3):  # Extracting three characters at a time
    char_code = secret_string[i:i+3]  # Extracting three characters
    decoded_string += chr(int(char_code))  # Converting back to characters

print("Decoded string:", decoded_string)
