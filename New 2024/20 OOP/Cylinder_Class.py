
from math import pi

class Cylinder:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.surface_area = Cylinder.get_surface_area(self)
        self.volume = Cylinder.get_volume(self)
   # TODO - Define the surface area method.     
    def get_surface_area(self):
        surface_area = round((2 * pi * self.radius) * (self.height + self.radius),2)
        return(surface_area)
    
    # TODO - Define the volume method.
    def get_volume(self):
        volume = round(pi * (self.radius**2) * self.height,2)
        return(volume)

my_cylidner=Cylinder(height = 2,radius = 3)
print(my_cylidner.get_surface_area())
print(my_cylidner.get_volume())

