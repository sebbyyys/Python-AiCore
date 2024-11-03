# TODO - Create a variable `int_1` and assign it the value `5`.
# TODO - Create a variable called `int_2` and assign it the value `10`.
# TODO - Evaluate `int_2` > `int_1`

int_1 = 5
int_2 = 10
bool(int_2 > int_1)

# TODO - Cast `int_2` - `int_1` - `int_1` as a Boolean.
# TODO - Cast `int_2` - `int_2` - `int_1` as a Boolean.
bool(int_2 - int_1 - int_1)
bool(int_2 - int_2 - int_1)

# Evaluation of strings
string_1 = "abcd"
string_2 = "efgh"

print(string_1 > string_2)
print(string_2 > string_1)

# TODO - Create three variables `A`, `B` and `C`. Assign them the values `2`,`5` and `10` respectively.
a = 2
b = 5
c = 10

# TODO - Write a python statement that `C` is bigger than `B` but not bigger than `A`. It should evaluate to `False`.
x = a > c > b

bool(x)

# TODO - Make the python statement that `A` is not equal to `B` and then negate it with not
d = not(a != b)
print(d)