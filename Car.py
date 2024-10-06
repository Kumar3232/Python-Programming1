# Define the Car class
class Car:
    def __init__(self, reg_num, max_speed):
        # Initialize the properties of the car
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Main program
# Create a new car with registration number ABC-123 and maximum speed 142 km/h
my_car = Car("ABC-123", 142)

# Print out all the properties of the car
print("Car registration number:", my_car.registration_number)
print("Car maximum speed:", my_car.maximum_speed, "km/h")
print("Car current speed:", my_car.current_speed, "km/h")
print("Car travelled distance:", my_car.travelled_distance, "km")
