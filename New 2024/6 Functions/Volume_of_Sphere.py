# TODO - Create a function that calculates the volume of a sphere given its radius
def volume_of_sphere(radius):
    pi = 3.14
    formula = (4/3)*pi*(radius**3)
    return(round(formula,2))

volume_of_sphere(2)