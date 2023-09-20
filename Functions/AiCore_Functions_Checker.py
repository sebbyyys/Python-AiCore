def in_range(lower_bound, upper_bound, number):
    if lower_bound < number < upper_bound:
        print(f"{number} is between {lower_bound} and {upper_bound}")
    else:
        print(f"{number} is NOT between {lower_bound} and {upper_bound}")
        
in_range(50, 200, 75)