x = 10
y = 0

# TODO: Create a divide function that uses a try-except block to return a 0 in case of a ZeroDivisionError
try:
    a = x
    b = y
    print(a / b)
except ZeroDivisionError:
    print(0)
    
# TODO: Create a user_input_divide function that asks for two user input for a and b, and returns a/b, handling the ZeroDivisionError by requesting new input

x = input("Please enter a number")
y = input("Please enter another number")

while True:
    try:
        a = int(x)
        b = int(y)
        print(a / b)
        break
    except ZeroDivisionError:
        x = input("Please enter the numbers again")
        y = input("And again")