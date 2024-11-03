class Car:
    def __init__(self, model, year=2024):
        self.model = model
        self.year = year
        self.miles_driven = 0
        
    def drive(self):
        print("vroom")
        self.miles_driven += 1
        
    def info(self):
        print(f"{self.miles_driven} miles driven, {self.model}, {self.year}")
        
    
my_car = Car("Tesla", 2019)
for i in range(5):
    my_car.drive()
my_car.info()