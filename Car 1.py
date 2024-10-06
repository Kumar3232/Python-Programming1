# Define the Car class
class Car:
    # Class initializer (constructor)
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number  # Set registration number
        self.maximum_speed = maximum_speed  # Set maximum speed
        self.current_speed = 0  # Initialize current speed to 0
        self.travelled_distance = 0  # Initialize travelled distance to 0

    # Method to change the speed of the car
    def accelerate(self, change_of_speed):
        # Adjust the speed and make sure it stays between 0 and the maximum speed
        self.current_speed += change_of_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed  # Speed cannot exceed the maximum
        elif self.current_speed < 0:
            self.current_speed = 0  # Speed cannot be less than 0


# Main program
def main():
    # Create a new Car object with registration number 'ABC-123' and maximum speed 142 km/h
    my_car = Car("ABC-123", 142)

    # Increase the speed by +30 km/h
    my_car.accelerate(30)
    print(f"Speed after +30 km/h: {my_car.current_speed} km/h")

    # Increase the speed by +70 km/h
    my_car.accelerate(70)
    print(f"Speed after +70 km/h: {my_car.current_speed} km/h")

    # Increase the speed by +50 km/h (should not exceed maximum speed)
    my_car.accelerate(50)
    print(f"Speed after +50 km/h: {my_car.current_speed} km/h")

    # Apply emergency brake (-200 km/h, speed should not go below 0)
    my_car.accelerate(-200)
    print(f"Speed after -200 km/h (emergency brake): {my_car.current_speed} km/h")


# Call the main function to run the program
if __name__ == "__main__":
    main()
