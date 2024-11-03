# TODO: Create a list named `data` with 5 tuples containing a name formatted as a string, and a number formatted as an integer

data = [("Vahin", 21), ("Amelia", 222), ("Jack", 11), ("Matt", 20), ("Seb", 23)]

# TODO: Sort the list by the number in each tuple by creating a lambda function called `sort_num` and using it as the key in `data.sort()`

sort_num = lambda x: x[1]
data.sort(key=sort_num)

print(data)

# TODO: Sort the list by the name in each tuple by creating a lambda function called `sort_name` and using it as the key in `data.sort()`
sort_name = lambda a : a[0]
data.sort(key=sort_name)

print(data)

# TODO: Sort the list by the length of the name in each tuple by creating a lambda function called `sort_name_len`
sort_name_len = lambda b : len(b[0])
data.sort(key=sort_name_len)

print(data)

# TODO: Sort the list by the length of the name but in reverse by using `sort_name_len`
sort_name_len_rev = lambda c : len(c[0::-1])
data.sort(key=sort_name_len_rev) # Can also use reverse = True at the end in the key

print(data)