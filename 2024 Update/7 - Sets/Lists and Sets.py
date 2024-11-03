list_1 = [1, 5, 10, 20, 40, 80]
list_2 = [6, 7, 20, 80, 100]
list_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# TODO - create a set with the common elements between list_1 and list_2 and name it common_1_2
common_1_2 = set(list_1).intersection(set(list_2))
print(common_1_2)

# TODO - Find the common elements between common_1_2 and list_3 and name it common_1_2_3
common_1_2_3 = common_1_2.intersection(set(list_3))
print(common_1_2_3)