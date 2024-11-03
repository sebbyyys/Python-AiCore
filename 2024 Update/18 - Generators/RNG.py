# TODO: Create a generator named `rand` that yields random numbers between 0 and 1 using the random library's `random` function
import random

def rand():
    while True:
        # Random.uniform provides a range between the specified number and the other number. Alternatively you just use random()
        yield round(random.uniform(0, 1), 2)
        
r = rand()
print(next(r))