set_1 = {15, 25, 35, 45, 55}
set_2 = {35, 45, 55, 65, 75}

# TODO - Find common items in both sets
common_items = set_1.intersection(set_2)
print(common_items)

# TODO - Find items in set_1 but not in set_2
set_1_only = set_1.difference(set_2)
print(set_1_only)

# TODO - Find items in set_2 but not in set_1
set_2_only = set_2.difference(set_1)
print(set_2_only)

# TODO - Find all items in either set_1 or set_2
set_1_and_2 = set_1.union(set_2)
print(sorted(set_1_and_2))

# TODO - Find items in set_1 or set_2 but not both
set_1_or_2 = set_1.symmetric_difference(set_2)
print(sorted(set_1_or_2))