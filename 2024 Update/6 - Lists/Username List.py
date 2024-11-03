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
print(usernames[0])

# TODO - Create a new list called usernames_2, consisting of the last 5 elements of usernames.

usernames_2 = usernames[-5:]
print(f"This is the second list before {usernames_2}")
user_example = usernames_2.pop(1)
print(f"This is it after{usernames_2}")
print(user_example)

# TODO - Use the `.sort()` method to sort the elements of `usernames` alphabetically.
# TODO - Print `usernames`
usernames.sort()
print(usernames)

# TODO - Using the `index()` method, find the index of `user_example` in `usernames` and assign it to a variable called `idx_user_example`.
# TODO - Using the index of `user_example`, retrieve the corresponding element from `usernames`, convert it to uppercase and assign it to a variable called `upper_user_example`.
# TODO - Using the index of `user_example`, replace the corresponding element in `usernames` with `upper_user_example`.
idx_user_example = usernames.index(user_example)
upper_user_example = usernames[idx_user_example].upper()
usernames.insert(idx_user_example, upper_user_example)

print(usernames)