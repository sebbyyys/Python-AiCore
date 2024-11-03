"""x = -1

# x = int(input("Enter a number: ")) # Comment this out to try this cell out with different values
if x < 0:
    raise ValueError("x must be positive")"""


name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))

# Add your code below this line
# TODO - Assert that the name is John
assert name == "John", "You are not John"
print("Hello, John")
if age >= 18:
    print("You are old enough to vote")
# TODO - Add an else statement
else:
    raise ValueError("You are not old enough to Vote")
    # TODO - Raise a ValueError if the age is less than 18
