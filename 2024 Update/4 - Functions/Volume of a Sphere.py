# TODO - Create a function that calculates the volume of a sphere given its radius
import math

def volume_of_sphere(radius):
    calc = (4/3) * math.pi * (radius**3)
    return round(calc, 2)

volume_of_sphere(2)
