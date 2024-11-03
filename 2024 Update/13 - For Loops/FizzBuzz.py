# Add your code below this line
# TODO - Loop through the numbers from 1 to 100
# TODO - Check if the number is divisible by 3, 5 or both. The order of the conditions is important!

for i in range(1,101):
    if i % 15 == 0:
        print("Fizzbuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
         