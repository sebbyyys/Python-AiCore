set_1 = {15, 25, 35, 45, 55}
set_2 = {35, 45, 55, 65, 75}

common_items = set_1.intersection(set_2)
print(common_items)

set_1_only = set_1.difference(set_2)
print(set_1_only)

set_2_only = set_2.difference(set_1)
print(set_2_only)

set_1_and_2 = set_1.union(set_2)
print(set_1_and_2)

set_1_or_2 = set_1.symmetric_difference(set_2)
print(set_1_or_2)