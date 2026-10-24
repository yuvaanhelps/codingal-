# create a class
class Vehicle:
    def __init__(self, max_speed, mileage):
        # bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
# object creation
car = Vehicle(240, 18)
# access the variables in the init method
print("car.max_speed:", car.max_speed)
print("car.mileage:", car.mileage)