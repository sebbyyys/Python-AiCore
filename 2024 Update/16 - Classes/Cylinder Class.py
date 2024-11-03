from math import pi

class Cylinder:
    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()
    
    # TODO - Define the surface area method.     
    def get_surface_area(self):
        surface_area = (2 * pi * self.radius * self.height) + (2 * pi * (self.radius**2))
        return round(surface_area, 2)
    
    # TODO - Define the volume method.
    def get_volume(self):
        volume = pi * (self.radius**2) * self.height
        return round(volume, 2)
        
    
    
    
# TODO - Create a cylinder object with height = 10 and radius = 5
my_cylinder = Cylinder(10, 5)
print(my_cylinder.radius)

# TODO - Create a cylinder object with height = 20 and radius = 10
my_cylinder_2 = Cylinder(20, 10)


my_cylinder_3 = Cylinder(2, 3)
print(my_cylinder_3.volume)
print(my_cylinder_3.surface_area)