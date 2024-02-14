# x = 10
# y = 0

# # TODO: Create a divide function that uses a try-except block to return a 0 in case of a ZeroDivisionError
# try:
#     a = x
#     b = y
#     print(a/b)
# except ZeroDivisionError:
#     print(0)
    
# TODO: Create a user_input_divide function that asks for two user input for a and b, and returns a/b, handling the ZeroDivisionError by requesting new input
a = int(input("Please enter a number"))
b = int(input("Please enter a second number"))

def user_input_divide(a, b):
    while True:
        try:
            print(int(a/b))
            break
        except ZeroDivisionError:
            a = int(input("Cannot divide by 0. Please enter a new number"))
            b = int(input("Please enter the number to divide by"))
                    

user_input_divide(a, b)