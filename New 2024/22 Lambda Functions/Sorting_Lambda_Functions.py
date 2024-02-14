# TODO: Create a list named `data` with 5 tuples containing a name formatted as a string, and a number formatted as an integer
data = [
    ("Johnzwe", 11),
    ("Aliceaa", 40),
    ("Bob", 12),
    ("Zarveastrodamus", 2),
    ("Yatterrius", 45)
]

# TODO: Sort the list by the number in each tuple by creating a lambda function called `sort_num` and using it as the key in `data.sort()`
sort_num = lambda x: x[1]
data.sort(key=sort_num)
print(data)

# TODO: Sort the list by the name in each tuple by creating a lambda function called `sort_name` and using it as the key in `data.sort()`
sort_name = lambda x: x[0]
data.sort(key = sort_name)
print(data)

# TODO: Sort the list by the length of the name in each tuple by creating a lambda function called `sort_name_len`
sort_name_len = lambda x: len(x[0])
data.sort(key = sort_name_len)
print(data)