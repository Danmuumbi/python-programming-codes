# Allows us to define private/hidden/secured attributes
class Square:
    def __init__(self, height="", width=""):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving height...")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Enter integers")

    @property
    def width(self):
        print("Retrieving width...")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Enter integers")

    def get_area(self):
        return int(self.__width) * int(self.__height)

def main():
    a_square = Square()
    height = input("Enter height: ")
    width = input("Enter width: ")
    a_square.height = height
    a_square.width = width
    print("Height: ", a_square.height)
    print("Width: ", a_square.width)
    print("Area: ", a_square.get_area())

main()
