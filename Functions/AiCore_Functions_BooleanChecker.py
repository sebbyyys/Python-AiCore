def in_range(lower_bound, upper_bound, number):
    if lower_bound < number < upper_bound:
        return True
    else:
        return False
    
in_range(1, 10, 5)