class calc:
    def add(x,y):
        return x+y;
    def sub(x,y):
        return x-y;
    def multiply(x,y):
        return x*y;
    def divide(x,y):
        if y==0:
            raise ValueError("No division by zero")
        return x/y;