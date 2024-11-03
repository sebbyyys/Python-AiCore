my_number_1 = 1
my_number_2 = 2

result = my_number_1 == my_number_2
print(result)

result2 = my_number_1 is my_number_2
print(result2)

my_number_1 = 1
my_number_2 = 1

same = my_number_1 is my_number_2
print(same)


my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [1, 2, 3, 4, 5]

listCompare = my_list_1 == my_list_2
print(listCompare)

listCompare2 = my_list_1 is my_list_2
print(listCompare2)