# TODO: Create a list of 5 numbers formatted as integers named `numbers`

numbers = [1, 2, 3, 4, 5]

# TODO: Create a lambda function named `square` that squares a number. Then use `map` to square each number in the list into a new list `numbers` called `squared_numbers`

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))

print(squared_numbers)

# TODO: Create a lambda function named `cube` that cubes a number. Then use `map` to cube each number in the list `numbers` into a new list called `cubed_numbers`

cube = lambda x: x ** 3
cubed_numbers = list(map(cube, numbers))

print(cubed_numbers)

# TODO: Create a lambda function named `func` takes in a number and returns that number squared if it is even, and cubed if it is odd. Then use `map` to apply the function to each number in the list `numbers` into a new list called `func_numbers`

func = lambda x: x ** 2 if x % 2 == 0 else x**3
func_numbers = list(map(func, numbers))

print(func_numbers)