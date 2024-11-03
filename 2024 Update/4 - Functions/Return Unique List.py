# TODO - Create a function called unique_list that takes a list as an argument and returns a list with all the unique elements of the list.

def unique_list(arg_list):
    x = set(my_list)
    return(list(x))
    
my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]

unique_output = unique_list(my_list)
print(unique_output)
