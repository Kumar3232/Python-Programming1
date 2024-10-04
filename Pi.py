import random

total_points = int(input("How many random points do you want to generate? "))

points_inside_circle = 0
points_generated = 0

while points_generated < total_points:

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Check if the point is inside the circle (x^2 + y^2 < 1)
    if (x * x + y * y) < 1:
        points_inside_circle += 1

    # Increase the number of points generated
    points_generated += 1

# Calculate pi approximation
pi_approx = 4 * points_inside_circle / total_points

print("The approximation of pi is:", pi_approx)
