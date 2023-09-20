my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
print(my_list)

def unique_list(rList):
    x = (set(rList))
    return(list(x))

unique_output = unique_list(my_list)
print(unique_list(my_list))