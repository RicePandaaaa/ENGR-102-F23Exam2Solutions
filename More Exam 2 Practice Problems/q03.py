import numpy as np

# Make our x values
x_values = np.linspace(-3, 5, 1000000)

# Function to calculate y
def y(x):
    return x**3 - (3 * x**2) - (5.5 * x) + 25

# Get y values
y_values = y(x_values)

# Locate either local minima or maxima
points = []

for i in range(1, len(y_values)-1):
    # Local maxima
    if y_values[i-1] < y_values[i] > y_values[i+1]:
        points.append((x_values[i], y_values[i]))
    # Local minima
    if y_values[i-1] > y_values[i] < y_values[i+1]:
        points.append((x_values[i], y_values[i]))

print(points)