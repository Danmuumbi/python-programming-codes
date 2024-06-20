# Illustrating isalnum() function
def demonstrate_isalnum():
    print("Demonstrating isalnum() function:")
    string1 = "Hello123"
    print("String:", string1)
    print("isalnum():", string1.isalnum())  # Output: True

    string2 = "Hello 123"
    print("String:", string2)
    print("isalnum():", string2.isalnum())  # Output: False (contains a space)


# Illustrating isdigit() function
def demonstrate_isdigit():
    print("\nDemonstrating isdigit() function:")
    string1 = "12345"
    print("String:", string1)
    print("isdigit():", string1.isdigit())  # Output: True

    string2 = "12345abc"
    print("String:", string2)
    print("isdigit():", string2.isdigit())  # Output: False (contains alphabetic characters)


# Illustrating the relationship between isalnum() and isdigit()
def illustrate_relationship():
    print("\nIllustrating the relationship between isalnum() and isdigit():")
    string3 = "Hello123"
    print("String:", string3)
    print("isalnum():", string3.isalnum())  # Output: True
    print("isdigit():", string3.isdigit())  # Output: False (contains both alphabetic and numeric characters)

    string4 = "12345"
    print("String:", string4)
    print("isalnum():", string4.isalnum())  # Output: True
    print("isdigit():", string4.isdigit())  # Output: True (contains only numeric characters)


# Main function to run the demonstration
def main():
    demonstrate_isalnum()
    demonstrate_isdigit()
    illustrate_relationship()


if __name__ == "__main__":
    main()
