list_1 = [1, 5, 10, 20, 40, 80]
list_2 = [6, 7, 20, 80, 100]
list_3 = [3, 4, 15, 20, 30, 70, 80, 120]


set_1 = set(list_1)
set_2 = set(list_2)
set_3 = set(list_3)

common_1_2 = set_1.intersection(set_2)
print(common_1_2)

common_1_2_3 = common_1_2.intersection(set_3)
print(common_1_2_3)





