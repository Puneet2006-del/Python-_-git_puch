a = int(input("Enter a number:"))
b = int(input("Enter second number:"))

if (b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero")
print(f"The division of a/b is {a/b}")

