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

    # Method to increase the travelled distance based on current speed and time
    def drive(self, hours):
        if self.current_speed > 0:
            distance = self.current_speed * hours  # Calculate distance travelled
            self.travelled_distance += distance  # Update travelled distance


# Main program
def main():
    # Create a new Car object with registration number 'ABC-123' and maximum speed 142 km/h
    my_car = Car("ABC-123", 142)

    # Increase the speed by +60 km/h
    my_car.accelerate(60)
    print(f"Speed after +60 km/h: {my_car.current_speed} km/h")

    # Drive for 1.5 hours
    my_car.drive(1.5)
    print(f"Travelled distance after driving 1.5 hours: {my_car.travelled_distance} km")

    # Increase the speed by +30 km/h
    my_car.accelerate(30)
    print(f"Speed after +30 km/h: {my_car.current_speed} km/h")

    # Drive for 2 hours
    my_car.drive(2)
    print(f"Travelled distance after driving 2 hours: {my_car.travelled_distance} km")

    # Apply emergency brake (-200 km/h, speed should not go below 0)
    my_car.accelerate(-200)
    print(f"Speed after -200 km/h (emergency brake): {my_car.current_speed} km/h")

    # Try driving with 0 speed (should not increase distance)
    my_car.drive(1)
    print(f"Travelled distance after trying to drive at 0 speed: {my_car.travelled_distance} km")


# Call the main function to run the program
if __name__ == "__main__":
    main()
