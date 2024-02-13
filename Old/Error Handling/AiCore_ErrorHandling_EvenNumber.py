# TODO - write a function that takes in an integer as an input, returns True if it is even,
# raises a ValueError if it is not, and a TypeError if the input is not an integer

def evenNumber(integer):
    try:
        if integer % 2 == 0:
            return True
        else:
            return ValueError
    except:
        return TypeError
    
evenNumber(2)