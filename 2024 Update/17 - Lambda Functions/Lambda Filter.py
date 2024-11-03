# TODO: Create a list named `data` with 10 strings

data = ['hello', 'oorld', 'Python', 'is', 'awesome', 'AI', 'programming']

# TODO: Create a lambda function called `length_check` that takes in a string and returns `True` if the string is longer than 5 characters, and `False` if it is not. Then use `filter` and the lambda function to filter out all strings that are longer than 5 characters into a new list named `filtered_data`
length_check = lambda x : len(x) > 5
filtered_data = list(filter(length_check, data))

print(filtered_data)

# TODO: Create a lambda function called `length_vowel_check` that takes in a string and returns `True` if the string is longer than 5 characters and starts with a vowel, and `False` if it is not. Then use `filter` and the lambda function to filter out all strings that are longer than 5 characters and start with a vowel into a new list named `new_filtered_data`

data = ['hello', 'world', 'Python', 'is', 'awesome', 'AI', 'programming']

length_vowel_check = lambda x: len(x) > 5 and x[0].lower() in 'aeiou'
filtered_vowel = list(filter(length_vowel_check, data))

print(filtered_vowel)