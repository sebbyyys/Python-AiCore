from datetime import date

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.miles_driven = 0
        
    def drive(self):
        self.miles_driven += 1
        return self.miles_driven
    
    def info(self):
        print("You've Driven: " + str(self.miles_driven) + " miles in your " + str(self.year) + " " + str(self.model))
  


car = Car('Tesla', 2019)

for drives in range (5):
    car.drive()

car.info()