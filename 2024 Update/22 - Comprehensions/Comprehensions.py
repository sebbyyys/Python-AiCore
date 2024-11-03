# TODO - Create a variable called word_list, and assign the values `['hello', 'world']`
# TODO - Use list comprension to capitalise the first letter of every element in `word_list`. Assign to a variable called `capital_list`.

word_list = ["hello", "world"]
capital_list = [x.capitalize() for x in word_list]

print(capital_list)

# TODO - Use a list comprehension to filter out every multiple of 5 from a range of numbers up to 100
filter_multiple = [x for x in range(1,101) if x % 5 == 0]

print(filter_multiple)

# TODO - Use a dictionary comprehension to create a map between every integer up to 15 and it's value squared
squared_dict = {x: x**2 for x in range(1,16)}
print(squared_dict)

squared_dict_items = {value: key for key, value in squared_dict.items()}
print(squared_dict_items)
    
