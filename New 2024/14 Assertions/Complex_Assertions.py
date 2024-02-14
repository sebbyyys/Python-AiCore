name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))

# Add your code below this line
# TODO - Assert that the name is John
assert name == "John","You are not John"
print("Hello, John")
if age >= 18:
    print("You are old enough to vote")
else:
    raise ValueError("You are not old enough to vote")
# TODO - Add an else statement
    # TODO - Raise a ValueError if the age is less than 18
