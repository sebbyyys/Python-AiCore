## inputting number before function

x = 10
y = 5

def zeroDivisor(a, b):
        try:
            division = a/b
            return(division)
        except:
            return(0)

zeroDivisor(x, y)

## inputting number in the function

def noInputZeroDivisor():
        a = input("Please enter a number: ")
        b = input("Please enter a number:")
        a = float(a)
        b = float(b)
        try:
            division = a/b
            return(division)
        except:
            return("error occured")

noInputZeroDivisor()