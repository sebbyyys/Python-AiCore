my_dict = {
    "key_1" : 1,
    "key_2" : 2,
    "key_3" : 3
}

# TODO - Use the del keyword to remove the key "key_1" from the dictionary
del my_dict["key_1"]
print(my_dict)

my_value = my_dict.pop("key_2")
print(my_dict)
print(my_value)