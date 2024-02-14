# TODO - write a function that takes in an integer as an input, returns True if it is even,
# raises a ValueError if it is not, and a TypeError if the input is not an integer

def even_check(integer):
    try:
        if integer % 2 == 0:
            print(True)
        else:
            return ValueError
    except:
        return TypeError
    
even_check("Seb")