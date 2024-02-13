prime_numbers = {2, 3, 5, 7, 11, 13}

# TODO - Add a prime number lower than 100 to the set
prime_numbers.add(17)
print(prime_numbers)

# ================================================================
prime_numbers = {2, 3, 5, 7, 11, 13}

# TODO - Create a new set with three numbers that are not in the set 'prime_numbers'
# TODO - Add the values in new_set to the set 'prime_numbers'

new_set = {19, 23, 29}
prime_numbers.update(new_set)

print(prime_numbers)
