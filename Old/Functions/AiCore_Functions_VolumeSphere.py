def volume_of_sphere(radius):
    pi = 3.14
    volume = 4/3*pi*(radius**3)
    return(round(volume,2))

v = volume_of_sphere(2)
print(v)