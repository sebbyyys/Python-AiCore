# Code to generate 10 usernames
import random
import string

usernames = []

for i in range(10):
    length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    usernames.append(username)

print(usernames)


# TODO - print the type of the variable `usernames`
print(type(usernames))

# TODO - print the length of the variable `usernames`
print(len(usernames))

# TODO - Print the type of the first item in `usernames`
print(type(usernames[0]))

usernames_2 = usernames[-5:]

# TODO - Remove the 2nd element of usernames_2 from the list and assign it to a variable called user_example
# TODO - Print the list usernames_2
user_example = usernames_2.pop(1)
print(usernames_2)
print("The user example is " + user_example)

# ========================================================================

# TODO - Use the `.sort()` method to sort the elements of `usernames` alphabetically.
# TODO - Print `usernames`
usernames.sort()
print(usernames)

# ==========================================================================
# TODO - Using the `index()` method, find the index of `user_example` in `usernames` and assign it to a variable called `idx_user_example`.
# TODO - Using the index of `user_example`, retrieve the corresponding element from `usernames`, convert it to uppercase and assign it to a variable called `upper_user_example`.
# TODO - Using the index of `user_example`, replace the corresponding element in `usernames` with `upper_user_example`.
print()
idx_user_example = usernames.index(user_example)
upper_user_example = usernames[idx_user_example].upper()
usernames[idx_user_example] = upper_user_example


print(usernames)