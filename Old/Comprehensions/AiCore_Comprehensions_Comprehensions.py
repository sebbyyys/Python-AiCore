word_list = ['hello', 'world']

# comprehension of first letter in list
newlist = [x.capitalize() for x in word_list ]
capital_list = newlist
# print(word_list, capital_list)

# TODO - Use a list comprehension to filter out every multiple of 5 from a range of numbers up to 100
fiveMultiple = [x for x in range(1,101) if x % 5 == 0]
# print(fiveMultiple)

# TODO - Use a dictionary comprehension to create a map between every integer up to 15 and it's value squared
squared_dict = {num: num*num for num in range(1,15)}

# {key: value for vars in iterable}    ----  how it should be formatted
# {num = num*num for num in range(1,15)}     ---- example used above
print(f"The square numbers from 1 to 15 are: {squared_dict}")


# inverse of squaring it all
import math
dict_items = squared_dict.items()
reversed_dict = {dict_items: round(math.sqrt(dict_items),2) for dict_items in range(1,15)}
print(f"The square root of numbers from 1 to 15 are: {reversed_dict}")