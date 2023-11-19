import numpy as np
from matplotlib import pyplot as plt

# Make our x and y values
x_values = np.linspace(0, 4, 10000000)
y_values = (0.1 * (x_values ** 3)) - (3 * np.cos(-2 * x_values))

# Graph the line
plt.title("Plot of x and y for y=0.1*x**3-3*cos(-2x)")
plt.xlabel("X data")
plt.ylabel("Y data")

plt.plot(x_values, y_values, "b")

# Graph the min and max
for i in range(1, len(y_values)-1):
    # Local maxima
    if y_values[i-1] < y_values[i] > y_values[i+1]:
        plt.plot(x_values[i], y_values[i], "o", color="orange")
    # Local minima
    if y_values[i-1] > y_values[i] < y_values[i+1]:
        plt.plot(x_values[i], y_values[i], "og")

plt.show()