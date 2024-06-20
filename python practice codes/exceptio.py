while True:#initialize a loop to execute forever
    try:
        number = int(input("the number is:"))#if use eters a character it will e wrog
        break
    except ValueError:
        print("value error occured")
    except:#if the error is ot kow
        print("unknown error")
print("thank you for entering umer")