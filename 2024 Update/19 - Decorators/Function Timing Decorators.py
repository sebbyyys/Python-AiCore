# TODO - Define a function to print "Inside our function!"

def inside():
    print("Inside our function")
    
# Create a decorator that prints "Start" and "End" at the start and end of a function call.

def print_start_end(function):
    def wrapper():
        print("Start")
        function()
        print("End")
    return wrapper

# TODO - put your decorator and custom function together, then call the output

x = print_start_end(inside)
x()


# TODO - Create a timer decorator function

def timer(function):
    def wrapper():
        import time
        start = time.time()
        function()
        end = time.time()
        print(end - start)
    return wrapper

x = timer(inside)
x()

