# TODO - Create a list with 4 elements of different types

list_1 = ["Seb", 25.0, True, 25]

for i in list_1:
    print(type(i))
    
# TODO - Create a list with 10 elements, all of which are 0

list_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list_2 = list_2 * 2
print(len(list_2))

# TODO - Create a list with two elements, list_1 and list_2
list_3 = list_1 + list_2
print(list_3)

# TODO - Create a list with two elements, the 4th element of list_1 and the 4th element of list_2
list_4 = [list_1[3], list_2[3]]
print(list_4)