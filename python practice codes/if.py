num1,num2,operator = input("2 numbers are").split()
num2 = int(num2)
num1= int(num1)
if operator == "+":
 print("{}+{}={}".format(num1,num2,num1+num2))
elif operator == "-":
 print("{}-{}={}".format(num2,num1,num2-num1))
else:
 print("invalid operator")
