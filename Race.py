import random

# Define the Car class
class Car:
    # Class initializer (constructor)
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number  # Set registration number
        self.maximum_speed = maximum_speed              # Set maximum speed
        self.current_speed = 0                          # Initialize current speed to 0
        self.travelled_distance = 0                     # Initialize travelled distance to 0

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
        distance = self.current_speed * hours  # Calculate distance travelled
        self.travelled_distance += distance    # Update travelled distance

# Main program
def main():
    # Create a list of 10 cars with random maximum speed between 100 and 200 km/h
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)  # Random maximum speed between 100 and 200 km/h
        reg_num = f"ABC-{i}"  # Registration number like "ABC-1", "ABC-2", etc.
        car = Car(reg_num, max_speed)
        cars.append(car)

    # Start the race
    race_over = False
    while not race_over:
        for car in cars:
            # Change the speed by a random value between -10 km/h and +15 km/h
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            # Drive for one hour
            car.drive(1)

            # Check if any car has travelled at least 10,000 km
            if car.travelled_distance >= 10000:
                race_over = True
                break  # End the race once one car reaches the target distance

    # Print out the properties of each car in a table format
    print(f"{'Car':<10} {'Max Speed (km/h)':<20} {'Current Speed (km/h)':<20} {'Distance Travelled (km)':<20}")
    print("-" * 70)
    for car in cars:
        print(f"{car.registration_number:<10} {car.maximum_speed:<20} {car.current_speed:<20} {car.travelled_distance:<20.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
