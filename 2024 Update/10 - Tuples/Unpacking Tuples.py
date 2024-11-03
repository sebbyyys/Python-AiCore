my_tuple = (70, "AiCore", 10, "Programming", 70)

x, *y, z = my_tuple
print(x)
print(y)
print(z)

print("")

x, y, *z = my_tuple
print(x)
print(y)
print(z)