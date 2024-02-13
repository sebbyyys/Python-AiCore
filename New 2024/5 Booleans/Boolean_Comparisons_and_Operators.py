# TODO - Create a variable `int_1` and assign it the value `5`.
# TODO - Create a variable called `int_2` and assign it the value `10`.
# TODO - Evaluate `int_2` > `int_1`
int_1 = 5
int_2 = 10
print(bool(int_2 > int_1))
print()

# TODO - Cast `int_2` - `int_1` - `int_1` as a Boolean.
# TODO - Cast `int_2` - `int_2` - `int_1` as a Boolean.
print(bool(int_2 - int_1 - int_1))
print(bool(int_2 - int_2 - int_1))
print()

#==========================================================

string_1 = "abcd"
string_2 = "efgh"

print(string_1 > string_2)
print(string_2 > string_1)
print()

#==========================================================

# TODO - Create three variables `A`, `B` and `C`. Assign them the values `2`,`5` and `10` respectively.
A = 2
B = 5
C = 10

# TODO - Write a python statement that `C` is bigger than `B` but not bigger than `A`. It should evaluate to `False`.
C_bigger = C > A
C_A = bool(not C > A)
print(C_A)


# TODO - Make the python statement that `A` is not equal to `B`
A_not_B = A != B
print(A_not_B)

# TODO - Make the python statement that `A` is not equal to `B`. It should evaluate to `False`.
A_B = bool(not A != B)
print(A_B)