# Add your code below this line
# TODO - Create a variable called my_list
my_list = [1, 2, 3, 3]

# TODO - Create the if/else statement to check if all elements in the list are unique
if len(set(my_list)) == len(my_list):
    print("All elements are unique")
else:
    print("There are duplicate elements")