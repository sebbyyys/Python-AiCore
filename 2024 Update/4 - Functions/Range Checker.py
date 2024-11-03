# TODO - Define a function called in_range that takes three parameters: lower_bound, upper_bound and number
    # TODO - Using if statements, check if the number is between the lower and upper bounds
        # TODO - If the number is between the lower and upper bounds, print "{number} is between {lower_bound} and {upper_bound}"
# TODO - If the number is not between the lower and upper bounds, print "{number} is NOT between {lower_bound} and {upper_bound}"

def in_range(lower_bound, upper_bound, number):
    if upper_bound > number > lower_bound:
        print(f"{number} is between {lower_bound} and {upper_bound}")
    else:
        print(f"{number} is NOT between {lower_bound} and {upper_bound}")
        
in_range(1, 10, 5)
in_range(1, 10, 11)
in_range(1, 10, 0)
