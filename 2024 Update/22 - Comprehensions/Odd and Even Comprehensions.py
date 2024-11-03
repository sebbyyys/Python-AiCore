# TODO - Create a list comprehension that squares even arguments, and squares odd arguments after adding one to them. Test it on `my_list`.
my_list = [1, 5, 8, 6, 21]

odd_even = [x ** 2 if x % 2 == 0 else (x + 1) **2 for x in my_list]

print(odd_even)