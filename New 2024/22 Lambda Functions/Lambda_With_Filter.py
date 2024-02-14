# TODO: Create a list named `data` with 10 strings
data = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon"
]

# TODO: Create a lambda function called `length_check` that takes in a string and returns `True` if the string is longer than 5 characters, and `False` if it is not. Then use `filter` and the lambda function to filter out all strings that are longer than 5 characters into a new list named `filtered_data`
length_check = lambda x: True if len(x) > 5 else False
filtered_data = list(filter(length_check,data))
print(filtered_data)

# TODO: Create a lambda function called `length_vowel_check` that takes in a string and returns `True` if the string is longer than 5 characters and starts with a vowel, and `False` if it is not. Then use `filter` and the lambda function to filter out all strings that are longer than 5 characters and start with a vowel into a new list named `new_filtered_data`
length_vowel_check = lambda x: True if len(x) > 5 and x[0] in ["a","e","i","o","u"] else False
new_filtered_data = list(filter(length_vowel_check,data))
print(new_filtered_data)
