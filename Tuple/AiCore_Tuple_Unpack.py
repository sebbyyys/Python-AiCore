my_tuple = (70, "AiCore", 10, "Programming", 70)

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
x, *y, z = my_tuple
print(x)
print(y)
print(z)

