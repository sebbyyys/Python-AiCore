# TODO - Create a variable called even_sum and set it to 0
# TODO - Create a for loop that iterates over the numbers 1 to 100
    # TODO - Check if the number is even
        # TODO - If the number is even, add it to the even_sum
even_sum = 0

for i in range(1,101):
    if i % 2 == 0:
        even_sum += i
        
print(f"The sum of even numbers is: {even_sum}")

# TODO - Create a variable called odd_sum and set it to 0
# TODO - Create a for loop that iterates over the numbers 1 to 100
    # TODO - Check if the number is odd
        # TODO - If the number is odd, add it to the odd_sum
odd_sum = 0

for i in range(1,101):
    if i % 2 == 1:
        odd_sum += i
        
print(f"The sum of odd numbers is: {odd_sum}")