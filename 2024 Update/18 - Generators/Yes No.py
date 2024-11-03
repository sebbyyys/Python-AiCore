# TODO: Using 2 yield statements, create a generator which alternatively yields `yes` and `no`

def yesno():
    list = ["yes", "no"]
    while list:
        for i in list:
            yield i
            
print(next(yesno()))
    