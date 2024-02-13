my_dict = {
    "key 1" : 1,
    "key 2" : 2,
    "key 3" : 3
    }
#use del to delete key3
del my_dict["key 3"]
#use pop to delete key 2
my_value = my_dict.pop("key 2")

print(my_dict)
print(my_value)