# TODO: Create a generator named `cycle` that infinitely cycles through a list of items in order

def yes_no():
    while True:
        yield "yes"
        yield "no"
        
yn = yes_no()
print(next(yn))
print(next(yn))


